# Project Enhancements Summary

## What's Been Created

### Core Planning
- ✅ `PLAN_CORE.md` - Your lean core planning document (v0.1)
- ✅ `README.md` - Quick start guide
- ✅ `SETUP.md` - Detailed setup instructions

### Project Structure
- ✅ Complete directory structure per PLAN_CORE.md
- ✅ `.gitignore` - Python/data science appropriate ignores
- ✅ `requirements.txt` - Core dependencies (geopandas, pandas, duckdb, jupyter, contextily, etc.)

### Code Foundation
- ✅ `src/data/loaders.py` - Data loading utilities for 4 anchor datasets
- ✅ `src/viz/maps.py` - Mapping utilities with basemap support
- ✅ `src/analysis/` - Placeholder for analysis functions
- ✅ `src/viz/` - Visualization utilities

### Starter Content
- ✅ `notebooks/00_exploratory/001_who_lives_where.ipynb` - First exploratory notebook template
- ✅ `stories/drafts/field_note_01.md` - Template for first field note
- ✅ `docs/data_sources.md` - Lightweight data catalog template
- ✅ `docs/ethics_positionality.md` - Ethics framework template

---

## Suggested Enhancements (Prioritized)

### High Priority (Next 2 Weeks)

1. **Data Acquisition Scripts**
   - Create `src/data/download.py` with functions to:
     - Download Census ACS data via `census` package
     - Fetch OSM data via Overpass API or GeoFabrik
     - Download city GIS data (if API available)
   - Add data validation checks

2. **City Limits Boundary**
   - Download Santa Fe city limits shapefile
   - Add to `src/data/loaders.py` as `load_city_limits()`
   - This is critical for clipping operations

3. **Data Processing Pipeline**
   - Create `notebooks/00_exploratory/000_data_prep.ipynb` for:
     - Downloading raw data → `data/raw/`
     - Cleaning and standardizing CRS
     - Joining datasets where needed
     - Saving processed versions → `data/processed/`

4. **Standardized CRS Configuration**
   - Add `src/config.py` with:
     - Default CRS for analysis (e.g., EPSG:3857 for web maps, EPSG:26913 for local)
     - Santa Fe bounding box
     - Color palettes for consistent theming

### Medium Priority (Weeks 3-4)

5. **Analysis Utilities**
   - `src/analysis/spatial.py`:
     - Distance calculations (to river, to services)
     - Spatial joins with standardized methods
     - Buffer operations
   - `src/analysis/demographics.py`:
     - Standardized demographic calculations
     - Percentages/rates (per your preference for choropleth maps)

6. **Enhanced Visualization**
   - `src/viz/charts.py` - Standardized chart functions
   - `src/viz/styles.py` - Consistent color schemes and map styles
   - Support for standardized values (percentages) in choropleth maps

7. **Notebook Templates**
   - Create `notebooks/_templates/` with:
     - Standard header cell (imports, config)
     - Map export workflow
     - Data citation cell

8. **Data Documentation**
   - Fill in `docs/data_sources.md` with:
     - Actual download URLs
     - Data dictionaries
     - Update frequencies
     - Known issues/limitations

### Lower Priority (As Needed)

9. **Testing & Validation**
   - Add `tests/` directory
   - Simple validation functions for data quality
   - CRS consistency checks

10. **Automation**
    - `scripts/update_data.py` - Refresh datasets on schedule
    - `scripts/build_notebooks.py` - Execute and export notebooks

11. **Publishing Workflow**
    - Template for moving drafts → published
    - Export scripts for static site generation (if desired)
    - Figure management (naming conventions, versioning)

12. **Advanced Analysis**
    - `src/analysis/equity.py` - Equity-focused metrics
    - `src/analysis/accessibility.py` - Service accessibility calculations
    - Integration with routing APIs if needed

---

## Quick Wins You Can Do Now

1. **Fill in data sources** - Update `docs/data_sources.md` with actual URLs as you find them
2. **Add your positionality** - Complete `docs/ethics_positionality.md` with your reflection
3. **Set up environment** - Run through `SETUP.md` to verify everything works
4. **Download first dataset** - Start with the easiest one (probably OSM or Census) to test the pipeline

---

## Recommended Workflow

1. **Week 1:** Set up environment + download 1-2 anchor datasets
2. **Week 2:** Complete data processing pipeline + run first exploratory notebook
3. **Week 3:** Create first map + draft first field note
4. **Week 4:** Refine and publish first field note

This keeps you on track for the v0.1 outcomes while building the foundation for deeper work.

---

## Notes on Tool Choices

Based on your preferences and the plan:

- ✅ **Python + venv** - Already set up per your preference
- ✅ **Standardized values** - Ready for percentage-based choropleth maps
- ✅ **Exploratory spatial data science** - Structure supports iterative exploration
- ✅ **Lean approach** - Minimal structure, expand as needed

The foundation is ready. Start small, iterate, and let the work guide what you build next.

