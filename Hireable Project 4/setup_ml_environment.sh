#!/bin/bash
# ============================================================
# ML Environment Setup Script for E-Commerce Recommendation System
# Ubuntu 22.04 + GTX 1660 Super + CUDA 13.0
# ============================================================

set -e  # Exit on any error

echo "============================================================"
echo "  ML Environment Setup Script"
echo "  For: Ubuntu 22.04 + GTX 1660 Super"
echo "============================================================"
echo ""

# Configuration
VENV_NAME="ml_env"
VENV_PATH="$HOME/$VENV_NAME"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

print_status() {
    echo -e "${GREEN}[✓]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[!]${NC} $1"
}

print_error() {
    echo -e "${RED}[✗]${NC} $1"
}

# Step 1: Check NVIDIA driver
echo ""
echo "Step 1: Checking NVIDIA driver..."
if command -v nvidia-smi &> /dev/null; then
    nvidia-smi --query-gpu=name,driver_version --format=csv,noheader
    print_status "NVIDIA driver detected"
else
    print_error "NVIDIA driver not found! Please install NVIDIA drivers first."
    exit 1
fi

# Step 2: Remove old virtual environment if exists
echo ""
echo "Step 2: Setting up virtual environment..."
if [ -d "$VENV_PATH" ]; then
    print_warning "Removing existing virtual environment at $VENV_PATH"
    rm -rf "$VENV_PATH"
fi

# Step 3: Create fresh virtual environment
python3 -m venv "$VENV_PATH"
print_status "Created virtual environment: $VENV_PATH"

# Step 4: Activate and upgrade pip
echo ""
echo "Step 3: Upgrading pip..."
source "$VENV_PATH/bin/activate"
pip install --upgrade pip setuptools wheel
print_status "pip upgraded"

# Step 5: Install PyTorch with CUDA support
# Using CUDA 12.4 wheels which work with CUDA 13.0 drivers (backward compatible)
echo ""
echo "Step 4: Installing PyTorch with CUDA support..."
echo "        (This may take a few minutes...)"
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
print_status "PyTorch installed"

# Step 6: Install core scientific packages (compatible versions)
echo ""
echo "Step 5: Installing core scientific packages..."
pip install "numpy>=1.26.0,<2.0.0"  # numpy 1.x for compatibility
pip install scipy pandas matplotlib seaborn
print_status "Core scientific packages installed"

# Step 7: Install scikit-learn
echo ""
echo "Step 6: Installing scikit-learn..."
pip install scikit-learn
print_status "scikit-learn installed"

# Step 8: Install surprise (recommender system library)
echo ""
echo "Step 7: Installing scikit-surprise..."
pip install scikit-surprise
print_status "scikit-surprise installed"

# Step 9: Install transformers and related packages
echo ""
echo "Step 8: Installing transformers and HuggingFace libraries..."
pip install transformers datasets accelerate tokenizers
print_status "Transformers installed"

# Step 10: Install Jupyter
echo ""
echo "Step 9: Installing Jupyter..."
pip install jupyter ipykernel ipywidgets
print_status "Jupyter installed"

# Step 11: Install additional useful packages
echo ""
echo "Step 10: Installing additional packages..."
pip install tqdm requests pillow
print_status "Additional packages installed"

# Step 12: Register the kernel with Jupyter
echo ""
echo "Step 11: Registering Jupyter kernel..."
python -m ipykernel install --user --name=$VENV_NAME --display-name="Python (ML Env)"
print_status "Jupyter kernel registered as 'Python (ML Env)'"

# Step 13: Verify installation
echo ""
echo "============================================================"
echo "  VERIFYING INSTALLATION"
echo "============================================================"
echo ""

python << 'EOF'
import sys
print(f"Python: {sys.version}")
print()

# Test imports
tests = []

try:
    import numpy as np
    tests.append(("numpy", np.__version__, True))
except Exception as e:
    tests.append(("numpy", str(e), False))

try:
    import pandas as pd
    tests.append(("pandas", pd.__version__, True))
except Exception as e:
    tests.append(("pandas", str(e), False))

try:
    import matplotlib
    tests.append(("matplotlib", matplotlib.__version__, True))
except Exception as e:
    tests.append(("matplotlib", str(e), False))

try:
    import seaborn as sns
    tests.append(("seaborn", sns.__version__, True))
except Exception as e:
    tests.append(("seaborn", str(e), False))

try:
    import scipy
    tests.append(("scipy", scipy.__version__, True))
except Exception as e:
    tests.append(("scipy", str(e), False))

try:
    import sklearn
    tests.append(("scikit-learn", sklearn.__version__, True))
except Exception as e:
    tests.append(("scikit-learn", str(e), False))

try:
    import surprise
    tests.append(("scikit-surprise", surprise.__version__, True))
except Exception as e:
    tests.append(("scikit-surprise", str(e), False))

try:
    import torch
    cuda_available = torch.cuda.is_available()
    cuda_info = f"{torch.__version__} | CUDA: {'✓ ' + torch.version.cuda if cuda_available else '✗ Not available'}"
    if cuda_available:
        cuda_info += f" | GPU: {torch.cuda.get_device_name(0)}"
    tests.append(("torch", cuda_info, cuda_available))
except Exception as e:
    tests.append(("torch", str(e), False))

try:
    import transformers
    tests.append(("transformers", transformers.__version__, True))
except Exception as e:
    tests.append(("transformers", str(e), False))

try:
    import datasets
    tests.append(("datasets", datasets.__version__, True))
except Exception as e:
    tests.append(("datasets", str(e), False))

# Print results
print("Package Verification:")
print("-" * 70)
all_passed = True
for name, version, passed in tests:
    status = "✓" if passed else "✗"
    print(f"  {status} {name:<20} {version}")
    if not passed:
        all_passed = False

print("-" * 70)
if all_passed:
    print("\n✓ ALL PACKAGES INSTALLED SUCCESSFULLY!")
else:
    print("\n✗ Some packages failed - see errors above")
    sys.exit(1)
EOF

echo ""
echo "============================================================"
echo "  SETUP COMPLETE!"
echo "============================================================"
echo ""
echo "To use this environment:"
echo ""
echo "  Option 1: In terminal:"
echo "    source ~/ml_env/bin/activate"
echo "    jupyter notebook"
echo ""
echo "  Option 2: In Jupyter:"
echo "    1. Open your notebook"
echo "    2. Kernel → Change Kernel → 'Python (ML Env)'"
echo ""
echo "  Option 3: Direct command:"
echo "    ~/ml_env/bin/jupyter notebook"
echo ""
echo "============================================================"
