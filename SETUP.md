# Setup Guide

## Requirements

- **Python 3.10 or 3.11** (recommended: 3.11)
- Virtual environment support (venv)

## Initial Setup

1. **Create Python virtual environment:**
   ```bash
   python3.11 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Optional: Create locked requirements file for reproducibility:**
   ```bash
   pip install pip-tools
   pip-compile requirements.txt -o requirements-lock.txt
   ```
   Then use `pip install -r requirements-lock.txt` for exact reproducibility.

3. **Set up Jupyter kernel (optional but recommended):**
   ```bash
   python -m ipykernel install --user --name santa-fe --display-name "Python (santa-fe)"
   ```

4. **Verify installation:**
   ```bash
   python -c "import geopandas; import pandas; import duckdb; print('✓ Core packages installed')"
   ```

5. **Run smoke tests:**
   ```bash
   pytest tests/ -v
   ```

## Data Setup

Before running notebooks, you'll need to download and process the anchor datasets:

1. **City Parcels + Zoning**
   - Source: City of Santa Fe GIS
   - Process and save to `data/processed/parcels_zoning.gpkg`

2. **Census Tracts + ACS Demographics**
   - Source: U.S. Census Bureau
   - Process and save to `data/processed/census_tracts_acs.gpkg`

3. **Hydrology (River + Arroyos)**
   - Source: TBD
   - Process and save to `data/processed/hydrology.gpkg`

4. **OSM Roads + POIs**
   - Source: OpenStreetMap (GeoFabrik or Overpass API)
   - Process and save to `data/processed/osm_roads_pois.gpkg`

See `docs/data_sources.md` for detailed links and instructions (to be filled in).

## First Steps

1. Start with the exploratory notebook:
   ```bash
   jupyter lab notebooks/00_exploratory/001_who_lives_where.ipynb
   ```

2. Update data loader paths in `src/data/loaders.py` once datasets are downloaded

3. Begin drafting your first field note in `stories/drafts/field_note_01.md`

## Project Structure

- `data/raw/` - Raw downloaded datasets
- `data/processed/` - Cleaned, analysis-ready datasets
- `notebooks/00_exploratory/` - Initial exploration
- `notebooks/10_analysis/` - Deeper analysis
- `src/` - Reusable Python modules
- `maps/static/` - Exported map figures
- `stories/drafts/` - Work-in-progress field notes
- `stories/published/` - Finished field notes
- `docs/` - Documentation

## Tips

- Keep raw data in `data/raw/` and never modify it directly
- Process data once and save to `data/processed/` for reuse
- Use the utility functions in `src/` to maintain consistency
- Export maps to `maps/static/` for use in field notes

