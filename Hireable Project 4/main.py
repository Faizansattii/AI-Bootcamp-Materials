from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import DistilBertForSequenceClassification, DistilBertTokenizer
import torch
import pickle
import pandas as pd
import os

from fastapi.middleware.cors import CORSMiddleware


# Initialize FastAPI app
app = FastAPI(title="E-Commerce Recommendation API", version="1.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global variables for models
svd_model = None
bert_model = None
bert_tokenizer = None
device = None
df_clean = None

# Function to parse the key-value format Amazon reviews file
def parse_amazon_reviews(file_path, max_rows=None):
    """
    Parse Amazon reviews from key-value format to DataFrame
    """
    print(f"Parsing data from: {file_path}")
    
    data = []
    entry = {}
    count = 0
    
    with open(file_path, 'r', encoding='latin1') as f:
        for line in f:
            line = line.strip()
            colon_pos = line.find(':')
            
            if colon_pos == -1:  # No colon means end of review entry
                if entry:
                    data.append(entry)
                    entry = {}
                    count += 1
                    
                    # Stop if we've reached max_rows
                    if max_rows and count >= max_rows:
                        break
                continue
            
            # Split at first colon
            key = line[:colon_pos]
            value = line[colon_pos+2:]  # Skip ': '
            entry[key] = value
        
        # Add last entry if exists and under limit
        if entry and (not max_rows or count < max_rows):
            data.append(entry)
    
    # Convert to DataFrame
    df = pd.DataFrame(data)
    print(f"✓ Parsed {len(df)} reviews")
    
    return df

# Load models on startup
@app.on_event("startup")
async def load_models():
    global svd_model, bert_model, bert_tokenizer, device, df_clean
    
    print("Loading models...")
    
    # Set device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")
    
    # Load SVD model
    with open('models/collab_filter.pkl', 'rb') as f:
        svd_model = pickle.load(f)
    print("✓ SVD model loaded")
    
    # Load BERT model
    bert_model = DistilBertForSequenceClassification.from_pretrained('models/sentiment_bert/')
    bert_tokenizer = DistilBertTokenizer.from_pretrained('models/sentiment_bert/')
    bert_model.to(device)
    bert_model.eval()
    print("✓ BERT model loaded")
    
    # Parse and load dataset (small sample for demo)
    df_clean = parse_amazon_reviews('data/amazon_reviews.csv', max_rows=50000)
    print(f"✓ Dataset loaded ({len(df_clean)} reviews)")
    
    print("All models ready!")

# Request/Response models
class SentimentRequest(BaseModel):
    review_text: str

class SentimentResponse(BaseModel):
    review_text: str
    predicted_rating: int
    confidence: float

class RecommendRequest(BaseModel):
    user_id: str
    n_recommendations: int = 10

class RecommendResponse(BaseModel):
    user_id: str
    recommendations: list

# Root endpoint
@app.get("/")
def read_root():
    return {
        "message": "E-Commerce Recommendation API",
        "endpoints": {
            "/docs": "API documentation",
            "/sentiment": "POST - Analyze review sentiment",
            "/recommend": "POST - Get product recommendations"
        }
    }

# Sentiment analysis endpoint
@app.post("/sentiment", response_model=SentimentResponse)
def analyze_sentiment(request: SentimentRequest):
    """
    Analyze sentiment of a review text and predict rating (1-5 stars)
    """
    try:
        # Tokenize
        encoding = bert_tokenizer(
            request.review_text,
            truncation=True,
            padding=True,
            max_length=128,
            return_tensors='pt'
        )
        encoding = {k: v.to(device) for k, v in encoding.items()}
        
        # Predict
        with torch.no_grad():
            outputs = bert_model(**encoding)
            logits = outputs.logits
            probabilities = torch.softmax(logits, dim=-1)
            predicted_class = torch.argmax(logits, dim=-1).item()
            confidence = probabilities[0][predicted_class].item()
        
        # Convert 0-4 to 1-5 stars
        predicted_rating = predicted_class + 1
        
        return SentimentResponse(
            review_text=request.review_text,
            predicted_rating=predicted_rating,
            confidence=round(confidence, 4)
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Helper function for sentiment score
def get_product_sentiment(product_id, df, model, tokenizer, device):
    """Get average sentiment score for a product"""
    product_reviews = df[df['product/productId'] == product_id]['review/text'].tolist()
    
    if len(product_reviews) == 0:
        return 3.0
    
    product_reviews = product_reviews[:5]  # Max 5 reviews for speed
    
    encodings = tokenizer(product_reviews, truncation=True, padding=True, 
                         max_length=128, return_tensors='pt')
    encodings = {k: v.to(device) for k, v in encodings.items()}
    
    with torch.no_grad():
        outputs = model(**encodings)
        predictions = torch.argmax(outputs.logits, dim=-1)
    
    sentiment_scores = predictions.cpu().numpy() + 1
    return float(sentiment_scores.mean())

# Recommendation endpoint
@app.post("/recommend", response_model=RecommendResponse)
def get_recommendations(request: RecommendRequest):
    """
    Get hybrid recommendations for a user (CF + Sentiment)
    """
    try:
        user_id = request.user_id
        n_recs = request.n_recommendations
        
        # Check if user exists
        if user_id not in df_clean['review/userId'].values:
            raise HTTPException(status_code=404, detail="User not found")
        
        # Get candidate products
        all_products = df_clean['product/productId'].unique()
        user_products = df_clean[df_clean['review/userId'] == user_id]['product/productId'].unique()
        candidates = [p for p in all_products if p not in user_products][:500]  # Limit for speed
        
        # Get CF scores
        cf_scores = {}
        for product in candidates:
            pred = svd_model.predict(user_id, product)
            cf_scores[product] = pred.est
        
        # Get top 30 from CF
        top_cf = sorted(cf_scores.items(), key=lambda x: x[1], reverse=True)[:30]
        
        # Get sentiment scores and combine
        recommendations = []
        for product, cf_score in top_cf:
            sentiment_score = get_product_sentiment(product, df_clean, bert_model, bert_tokenizer, device)
            hybrid_score = (0.7 * cf_score) + (0.3 * sentiment_score)
            
            recommendations.append({
                'product_id': product,
                'cf_score': round(cf_score, 2),
                'sentiment_score': round(sentiment_score, 2),
                'hybrid_score': round(hybrid_score, 2)
            })
        
        # Sort by hybrid score
        recommendations = sorted(recommendations, key=lambda x: x['hybrid_score'], reverse=True)[:n_recs]
        
        return RecommendResponse(
            user_id=user_id,
            recommendations=recommendations
        )
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Health check
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "models_loaded": svd_model is not None and bert_model is not None
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)