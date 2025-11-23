# Data Sources

Lightweight catalog of datasets used in this project.

## Anchor Datasets (v0.1)

### 1. City Parcels + Zoning
- **Source:** City of Santa Fe GIS Portal
- **URL:** https://www.santafenm.gov/gis
- **Download:** Manual download from GIS portal (search for "Parcels" or "Zoning")
- **Alternative:** ArcGIS Online - search "Santa Fe parcels"
- **Format:** Shapefile/GeoJSON
- **Update frequency:** Varies (check with city)
- **Processing:** See `notebooks/00_exploratory/000_data_prep.ipynb`
- **Notes:** Legal containers for land + zoning classifications

### 2. Census Tracts + ACS Demographics
- **Source:** U.S. Census Bureau
  - **Tracts:** TIGER/Line Shapefiles
  - **Demographics:** American Community Survey (ACS) API
- **TIGER URL:** https://www2.census.gov/geo/tiger/TIGER2022/TRACT/
- **ACS API:** https://api.census.gov/data/ (requires API key)
- **API Key:** Get from https://api.census.gov/data/key_signup.html
- **Format:** Shapefile + CSV/JSON (via API)
- **Update frequency:** Annual (TIGER), 5-year ACS estimates
- **FIPS Codes:** State: 35 (NM), County: 049 (Santa Fe), Place: 70490 (Santa Fe city)
- **Processing:** Automated via `src/data/download.py`

### 3. Santa Fe River + Hydrology
- **Source:** OpenStreetMap (default), with alternatives below
- **Primary:** OSM via Overpass API - automated download
- **Format:** GeoJSON → processed to GeoPackage
- **Update frequency:** Continuous (OSM updated daily)
- **Alternatives:**
  1. **NM State GIS** - https://www.nmgis.org/ (search "hydrology" or "water")
  2. **USGS 3D Hydrography Program (3DHP)** - https://www.usgs.gov/3d-hydrography-program/access-3dhp-data-products
     - Note: NHD was retired in October 2023, replaced by 3DHP
     - HUC Region: 1302 (Upper Rio Grande)
- **Processing:** See `notebooks/00_exploratory/000_data_prep.ipynb`
- **Notes:** OSM provides good coverage for Santa Fe area; includes rivers, streams, canals, and waterbodies

### 4. OSM Roads + POIs
- **Source:** OpenStreetMap
- **Methods:**
  1. **Overpass API** (custom area) - Used by default in download script
  2. **GeoFabrik** - New Mexico extract: https://download.geofabrik.de/north-america/us/new-mexico-latest-free.shp.zip
- **Format:** GeoJSON (Overpass) or Shapefile (GeoFabrik)
- **Update frequency:** Continuous (OSM is updated daily)
- **Processing:** See `notebooks/00_exploratory/000_data_prep.ipynb`
- **Notes:** Includes highways, roads, amenities, shops

### 5. City Limits Boundary
- **Source:** 
  1. Census TIGER/Line Places (automated)
  2. City of Santa Fe GIS (manual)
- **TIGER URL:** https://www2.census.gov/geo/tiger/TIGER2022/PLACE/
- **City GIS:** https://www.santafenm.gov/gis
- **Format:** Shapefile
- **Update frequency:** Annual (TIGER), varies (city)
- **Processing:** Automated - filters for Santa Fe city (PLACEFP=70490)

## Download Instructions

**Automated Download:**
Run `notebooks/00_exploratory/000_data_prep.ipynb` to download most datasets automatically.

**Manual Downloads:**
- City parcels: Requires manual download from city GIS portal
- Some datasets may need manual intervention if automated download fails

## Data Processing

All raw data goes to `data/raw/`. Processing (reprojection, clipping, joining) saves to `data/processed/`.

Processing steps:
1. Set CRS if missing (assumes EPSG:4326)
2. Clip to city limits (if available)
3. Reproject to NM State Plane (EPSG:32113)
4. Save as GeoPackage (.gpkg)

## Additional Datasets

*Add as discovered and used*

---

**Last updated:** December 2024

