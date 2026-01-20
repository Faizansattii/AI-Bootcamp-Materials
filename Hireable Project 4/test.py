# test_api.py
import requests

# Test sentiment analysis
print("="*50)
print("Testing /sentiment endpoint")
print("="*50)

sentiment_data = {
    "review_text": "This product is absolutely amazing! Best purchase ever!"
}

response = requests.post("http://localhost:8000/sentiment", json=sentiment_data)
print(response.json())

# Test recommendations
print("\n" + "="*50)
print("Testing /recommend endpoint")
print("="*50)

recommend_data = {
    "user_id": "A3SGXH7AUHU8GW",  # Use actual user from dataset
    "n_recommendations": 5
}

response = requests.post("http://localhost:8000/recommend", json=recommend_data)
print(response.json())