#!/bin/bash
# Quick check script for linting and tests

set -e

echo "🔍 Running project checks..."

# Check Python version
echo "Python version:"
python --version

# Run tests
echo ""
echo "🧪 Running tests..."
pytest tests/ -v

# Basic import check
echo ""
echo "📦 Checking imports..."
python -c "
import sys
from pathlib import Path
sys.path.insert(0, str(Path('src')))
try:
    from src.config import DATA_PROCESSED, DEFAULT_CRS
    from src.data.loaders import load_parcels, get_santa_fe_bounds
    from src.viz.maps import setup_basemap, save_map
    print('✓ All imports successful')
except ImportError as e:
    print(f'✗ Import error: {e}')
    sys.exit(1)
"

echo ""
echo "✅ All checks passed!"

