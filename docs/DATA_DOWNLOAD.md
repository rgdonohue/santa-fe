# Data Download Guide

## Overview

The data download system provides automated and semi-automated ways to acquire the 5 core datasets for Santa Fe geospatial analysis.

## Quick Start

**Run the data preparation notebook:**
```bash
jupyter lab notebooks/00_exploratory/000_data_prep.ipynb
```

This notebook will:
1. Download city limits (from Census TIGER/Line)
2. Download census tracts (from Census TIGER/Line)
3. Download OSM data (from Overpass API)
4. Download hydrology (from USGS NHD)
5. Guide you through downloading city parcels (manual)

## Datasets

### 1. City Limits ✅ Automated
- **Source:** Census TIGER/Line Places
- **Download:** Fully automated
- **Processing:** Filters for Santa Fe city (PLACEFP=70490)

### 2. Census Tracts ✅ Automated (Boundaries)
- **Source:** Census TIGER/Line
- **Download:** Fully automated
- **Processing:** Clips to city limits, reprojects to NM State Plane
- **Note:** ACS demographic data requires Census API key (see below)

### 3. OSM Roads + POIs ✅ Automated
- **Source:** OpenStreetMap Overpass API
- **Download:** Fully automated
- **Processing:** Raw JSON saved; can be converted to GeoDataFrame later
- **Note:** Consider using `osmnx` package for more sophisticated processing

### 4. Hydrology ⚠️ Automated (Large File)
- **Source:** USGS National Hydrography Dataset
- **Download:** Automated but large (~100MB+)
- **Processing:** Extracts flowlines and waterbodies, clips to city
- **Note:** Download may take several minutes

### 5. City Parcels ⚠️ Manual
- **Source:** City of Santa Fe GIS Portal
- **Download:** Manual (city GIS portals vary)
- **Instructions:** See notebook output or visit https://www.santafenm.gov/gis

## Census API Setup (for ACS Demographics)

To download ACS demographic data:

1. **Get API Key:**
   - Visit: https://api.census.gov/data/key_signup.html
   - Sign up and get your API key

2. **Set Environment Variable:**
   ```bash
   export CENSUS_API_KEY=your_key_here
   ```
   Or add to `.env` file:
   ```
   CENSUS_API_KEY=your_key_here
   ```

3. **Install Census Package:**
   ```bash
   pip install census
   ```

4. **Use in Code:**
   ```python
   from census import Census
   import os
   
   c = Census(os.getenv("CENSUS_API_KEY"))
   # Fetch ACS data for Santa Fe County tracts
   ```

## Manual Downloads

If automated downloads fail, see `docs/data_sources.md` for manual download links and instructions.

## Processing Pipeline

All datasets follow this processing pipeline:

1. **Download** → `data/raw/`
2. **Extract** (if zip file)
3. **Set CRS** (if missing, assumes EPSG:4326)
4. **Clip** to city limits (if available)
5. **Reproject** to NM State Plane (EPSG:32113)
6. **Save** → `data/processed/` as GeoPackage (.gpkg)

## Troubleshooting

### Download Fails
- Check internet connection
- Verify URLs are still valid (see `docs/data_sources.md`)
- Try manual download as fallback

### Processing Errors
- Ensure city limits are downloaded first (needed for clipping)
- Check that raw files are valid shapefiles/GeoJSON
- Verify CRS information in raw data

### Large Files
- NHD hydrology data is large (~100MB+)
- Be patient during download
- Consider downloading during off-peak hours

## Next Steps

After downloading all datasets:

1. **Verify:** Run the verification cell in `000_data_prep.ipynb`
2. **Explore:** Start with `001_who_lives_where.ipynb`
3. **Analyze:** Use the data loaders in `src/data/loaders.py`

## Files Created

- `src/data/download.py` - Download functions
- `notebooks/00_exploratory/000_data_prep.ipynb` - Download notebook
- `docs/data_sources.md` - Updated with URLs and instructions

