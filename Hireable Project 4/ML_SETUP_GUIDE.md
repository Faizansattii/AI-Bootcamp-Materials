# ML Environment Setup Guide

## Quick Start (Recommended)

### Step 1: Run the Setup Script
```bash
cd ~
chmod +x setup_ml_environment.sh
./setup_ml_environment.sh
```

This will:
- Create a clean virtual environment at `~/ml_env`
- Install all packages with compatible versions
- Set up a Jupyter kernel called "Python (ML Env)"

### Step 2: Start Jupyter
```bash
# Option A: Activate environment first
source ~/ml_env/bin/activate
jupyter notebook

# Option B: Run directly
~/ml_env/bin/jupyter notebook
```

### Step 3: Select the Correct Kernel
In your notebook:
1. **Kernel** → **Change Kernel** → **Python (ML Env)**
2. Run the cells

---

## Alternative: Fix Existing Environment (Riskier)

If you don't want a virtual environment, try these commands in order:

```bash
# Step 1: Downgrade numpy to 1.x (fixes scipy binary incompatibility)
pip install --user "numpy>=1.26.0,<2.0.0" --force-reinstall --break-system-packages

# Step 2: Reinstall scipy (recompiles against correct numpy)
pip install --user scipy --force-reinstall --no-cache-dir --break-system-packages

# Step 3: Reinstall packages that depend on numpy
pip install --user seaborn matplotlib pandas --force-reinstall --break-system-packages

# Step 4: Install urllib3 in user packages (fixes the import error)
pip install --user urllib3 --break-system-packages

# Step 5: Restart Jupyter completely (kill any running instances)
pkill -f jupyter
jupyter notebook
```

**Note:** This may still have issues due to system package conflicts.

---

## Troubleshooting

### "Unable to import Axes3D" Warning
This is just a warning and doesn't affect functionality. To suppress it:
```python
import warnings
warnings.filterwarnings('ignore')
```

### urllib3 Import Error
This happens when removing system paths. The fix is:
```bash
pip install --user urllib3 --break-system-packages
```

### numpy.dtype size changed Error
This means numpy version doesn't match compiled extensions. Fix:
```bash
pip install --user "numpy>=1.26.0,<2.0.0" --force-reinstall --break-system-packages
pip install --user scipy seaborn --force-reinstall --no-cache-dir --break-system-packages
```

### send2trash Parsing Error
This is a broken system package. You can ignore it or:
```bash
sudo apt remove python3-send2trash
pip install --user send2trash --break-system-packages
```

### torch.cuda.is_available() Returns False
1. Check NVIDIA driver: `nvidia-smi`
2. Reinstall PyTorch with CUDA:
```bash
pip install --user torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124 --force-reinstall --break-system-packages
```

---

## Package Versions (Known Working Combination)

| Package | Version |
|---------|---------|
| numpy | 1.26.4 |
| scipy | 1.14.x |
| pandas | 2.2.x |
| matplotlib | 3.9.x |
| seaborn | 0.13.x |
| scikit-learn | 1.5.x |
| torch | 2.5.x+cu124 |
| transformers | 4.46.x |
| scikit-surprise | 1.1.4 |

---

## Verify Your Setup

Run this Python code to verify everything works:

```python
import sys
print(f"Python: {sys.executable}")

# Test all imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
import sklearn
import surprise
import torch
import transformers
from datasets import load_dataset

print(f"\nnumpy:        {np.__version__}")
print(f"pandas:       {pd.__version__}")
print(f"matplotlib:   {plt.matplotlib.__version__}")
print(f"seaborn:      {sns.__version__}")
print(f"scipy:        {scipy.__version__}")
print(f"sklearn:      {sklearn.__version__}")
print(f"surprise:     {surprise.__version__}")
print(f"torch:        {torch.__version__}")
print(f"transformers: {transformers.__version__}")

print(f"\nCUDA available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"GPU: {torch.cuda.get_device_name(0)}")
    
print("\n✓ All imports successful!")
```

---

## Directory Structure After Setup

```
~/
├── ml_env/                    # Virtual environment
│   ├── bin/
│   │   ├── python
│   │   ├── pip
│   │   └── jupyter
│   └── lib/python3.10/site-packages/
├── setup_ml_environment.sh    # Setup script
└── e_commerce_recommendation.ipynb  # Your notebook
```
