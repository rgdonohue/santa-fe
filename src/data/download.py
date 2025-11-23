"""
Data download utilities for Santa Fe geospatial datasets.

Downloads raw data from various sources and saves to data/raw/.
"""

import requests
import geopandas as gpd
import pandas as pd
from pathlib import Path
from typing import Optional, Tuple
import zipfile
import io
from tqdm import tqdm

from ..config import DATA_RAW, DATA_PROCESSED, LOCAL_CRS, get_census_api_key


def download_file(url: str, output_path: Path, chunk_size: int = 8192) -> Path:
    """
    Download a file from URL with progress bar.
    
    Parameters
    ----------
    url : str
        URL to download from
    output_path : Path
        Output file path
    chunk_size : int
        Chunk size for streaming download
    
    Returns
    -------
    Path
        Path to downloaded file
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    response = requests.get(url, stream=True)
    response.raise_for_status()
    
    total_size = int(response.headers.get('content-length', 0))
    
    with open(output_path, 'wb') as f:
        if total_size == 0:
            f.write(response.content)
        else:
            with tqdm(total=total_size, unit='B', unit_scale=True, desc=f"Downloading {output_path.name}") as pbar:
                for chunk in response.iter_content(chunk_size=chunk_size):
                    if chunk:
                        f.write(chunk)
                        pbar.update(len(chunk))
    
    return output_path


def download_census_tracts(
    state_fips: str = "35",  # New Mexico
    county_fips: str = "049",  # Santa Fe County
    year: int = 2022,
    acs_year: str = "5yr",
    output_dir: Optional[Path] = None
) -> Tuple[Path, Path]:
    """
    Download census tracts with ACS demographics for Santa Fe County.
    
    Uses Census API and TIGER/Line shapefiles.
    
    Parameters
    ----------
    state_fips : str
        State FIPS code (35 = New Mexico)
    county_fips : str
        County FIPS code (049 = Santa Fe County)
    year : int
        Year for TIGER/Line boundaries
    acs_year : str
        ACS data year/period (e.g., "5yr" for 5-year estimates)
    output_dir : Path, optional
        Output directory. Defaults to DATA_RAW
    
    Returns
    -------
    tuple[Path, Path]
        Paths to (tracts shapefile, ACS data CSV)
    """
    if output_dir is None:
        output_dir = DATA_RAW
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Download TIGER/Line census tracts shapefile
    tiger_url = (
        f"https://www2.census.gov/geo/tiger/TIGER{year}/TRACT/"
        f"tl_{year}_{state_fips}_tract.zip"
    )
    
    tracts_zip = output_dir / f"census_tracts_{year}.zip"
    print(f"Downloading census tracts from {tiger_url}")
    download_file(tiger_url, tracts_zip)
    
    # Extract shapefile
    tracts_dir = output_dir / f"census_tracts_{year}"
    tracts_dir.mkdir(exist_ok=True)
    
    with zipfile.ZipFile(tracts_zip, 'r') as zip_ref:
        zip_ref.extractall(tracts_dir)
    
    # Find the shapefile
    shapefile = list(tracts_dir.glob("*.shp"))[0]
    
    # Download ACS data via census package (if available)
    acs_csv = output_dir / f"acs_{year}_{acs_year}_santa_fe.csv"
    
    api_key = get_census_api_key()
    
    if api_key:
        try:
            from census import Census
            c = Census(api_key)
            
            print("\nDownloading ACS demographic data...")
            
            # ACS 5-year estimates variables for Santa Fe County tracts
            # Common variables: income, race, housing tenure, etc.
            acs_vars = [
                'B19013_001E',  # Median household income
                'B25003_002E',  # Owner-occupied housing units
                'B25003_003E',  # Renter-occupied housing units
                'B25003_001E',  # Total occupied housing units
                'B01001_001E',  # Total population
                'B03002_003E',  # White alone
                'B03002_004E',  # Black or African American alone
                'B03002_005E',  # American Indian and Alaska Native alone
                'B03002_006E',  # Asian alone
                'B03002_012E',  # Hispanic or Latino
            ]
            
            # Fetch data for Santa Fe County tracts
            acs_data = c.acs5.get(
                acs_vars,
                {
                    'for': f'tract:*',
                    'in': f'state:{state_fips} county:{county_fips}'
                },
                year=int(year)
            )
            
            # Convert to DataFrame
            acs_df = pd.DataFrame(acs_data)
            
            # Calculate percentages
            if 'B25003_001E' in acs_df.columns and 'B25003_003E' in acs_df.columns:
                acs_df['pct_renters'] = (
                    (acs_df['B25003_003E'].astype(float) / 
                     acs_df['B25003_001E'].astype(float)) * 100
                ).round(2)
            
            # Rename columns for readability
            acs_df = acs_df.rename(columns={
                'B19013_001E': 'median_income',
                'B25003_001E': 'total_occupied_units',
                'B25003_002E': 'owner_occupied',
                'B25003_003E': 'renter_occupied',
                'B01001_001E': 'total_population',
                'B03002_003E': 'white_alone',
                'B03002_004E': 'black_alone',
                'B03002_005E': 'native_alone',
                'B03002_006E': 'asian_alone',
                'B03002_012E': 'hispanic_latino',
            })
            
            # Create GEOID for joining (state + county + tract)
            acs_df['GEOID'] = (
                acs_df['state'].astype(str).str.zfill(2) +
                acs_df['county'].astype(str).str.zfill(3) +
                acs_df['tract'].astype(str).str.zfill(6)
            )
            
            # Save to CSV
            acs_df.to_csv(acs_csv, index=False)
            print(f"✓ ACS data downloaded and saved to: {acs_csv}")
            print(f"  Downloaded {len(acs_df)} tracts")
            
        except ImportError:
            print("\n⚠ Census package not installed. Install with: pip install census")
            print("ACS data download skipped.")
        except Exception as e:
            print(f"\n⚠ Error downloading ACS data: {e}")
            print("Continuing with tracts shapefile only.")
    else:
        print("\n⚠ CENSUS_API_KEY not found in environment.")
        print("Set it in .env file or as environment variable to download ACS data.")
        print(f"\nTracts shapefile saved to: {shapefile}")
        print(f"ACS data CSV will be created at: {acs_csv} (when API key is set)")
    
    return shapefile, acs_csv


def download_osm_data(
    bbox: Optional[dict] = None,
    output_dir: Optional[Path] = None,
    use_overpass: bool = True
) -> Path:
    """
    Download OSM roads and POIs for Santa Fe area.
    
    Parameters
    ----------
    bbox : dict, optional
        Bounding box as {'minx', 'miny', 'maxx', 'maxy'}.
        Defaults to approximate Santa Fe bounds.
    output_dir : Path, optional
        Output directory. Defaults to DATA_RAW
    use_overpass : bool
        If True, use Overpass API. If False, use GeoFabrik extract.
    
    Returns
    -------
    Path
        Path to downloaded OSM data file
    """
    if output_dir is None:
        output_dir = DATA_RAW
    
    if bbox is None:
        # Approximate Santa Fe bounds
        bbox = {
            'minx': -106.0,
            'miny': 35.6,
            'maxx': -105.8,
            'maxy': 35.8
        }
    
    if use_overpass:
        # Use Overpass API for custom area
        overpass_query = f"""
        [out:json][timeout:25];
        (
          way["highway"~"^(primary|secondary|tertiary|residential|service)$"]({bbox['miny']},{bbox['minx']},{bbox['maxy']},{bbox['maxx']});
          node["amenity"]({bbox['miny']},{bbox['minx']},{bbox['maxy']},{bbox['maxx']});
          node["shop"]({bbox['miny']},{bbox['minx']},{bbox['maxy']},{bbox['maxx']});
        );
        out geom;
        """
        
        overpass_url = "https://overpass-api.de/api/interpreter"
        
        print("Downloading OSM data via Overpass API...")
        response = requests.post(overpass_url, data={"data": overpass_query})
        response.raise_for_status()
        
        osm_data = response.json()
        output_path = output_dir / "osm_santa_fe.json"
        
        import json
        with open(output_path, 'w') as f:
            json.dump(osm_data, f)
        
        print(f"OSM data saved to: {output_path}")
        return output_path
    
    else:
        # Alternative: Download from GeoFabrik (New Mexico extract)
        geofabrik_url = "https://download.geofabrik.de/north-america/us/new-mexico-latest-free.shp.zip"
        
        output_path = output_dir / "new-mexico-latest-free.shp.zip"
        print(f"Downloading New Mexico extract from GeoFabrik...")
        download_file(geofabrik_url, output_path)
        
        return output_path


def download_hydrology(
    output_dir: Optional[Path] = None,
    source: str = "osm"
) -> Optional[Path]:
    """
    Download hydrology data (rivers, streams, waterbodies) for Santa Fe area.
    
    Note: USGS NHD was retired in October 2023. This function provides alternatives.
    
    Parameters
    ----------
    output_dir : Path, optional
        Output directory. Defaults to DATA_RAW
    source : str
        Data source: "osm" (OpenStreetMap - default), "nm" (NM state GIS), or "usgs_3dhp" (3DHP)
    
    Returns
    -------
    Path or None
        Path to downloaded hydrology data, or None if manual download needed
    """
    if output_dir is None:
        output_dir = DATA_RAW
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    if source == "osm":
        # Use OpenStreetMap water features (readily available, good coverage)
        print("Downloading hydrology data from OpenStreetMap...")
        
        # Santa Fe bounds
        bbox = {
            'minx': -106.0,
            'miny': 35.6,
            'maxx': -105.8,
            'maxy': 35.8
        }
        
        # Overpass query for water features
        # Using out geom to get geometry directly
        overpass_query = f"""
        [out:json][timeout:30];
        (
          way["waterway"]({bbox['miny']},{bbox['minx']},{bbox['maxy']},{bbox['maxx']});
          way["natural"="water"]({bbox['miny']},{bbox['minx']},{bbox['maxy']},{bbox['maxx']});
        );
        out geom;
        """
        
        overpass_url = "https://overpass-api.de/api/interpreter"
        
        try:
            response = requests.post(overpass_url, data={"data": overpass_query}, timeout=90)
            response.raise_for_status()
            
            osm_data = response.json()
            
            # Check if we got any data
            elements = osm_data.get('elements', [])
            if not elements:
                print("⚠ No water features found in OSM for this area")
                print("This might be normal - Santa Fe is in a semi-arid region")
                print("Consider using alternative sources or expanding the bounding box")
                return None
            
            output_path = output_dir / "hydrology_osm.json"
            
            import json
            with open(output_path, 'w') as f:
                json.dump(osm_data, f)
            
            print(f"✓ OSM hydrology data saved to: {output_path}")
            print(f"  Found {len(elements)} water features")
            return output_path
            
        except requests.exceptions.Timeout:
            print("⚠ Request timed out. Overpass API may be slow. Try again later.")
            return None
        except requests.exceptions.RequestException as e:
            print(f"⚠ Network error downloading OSM hydrology: {e}")
            print(f"  Status code: {getattr(e.response, 'status_code', 'N/A')}")
            return None
        except Exception as e:
            print(f"⚠ Error downloading OSM hydrology: {e}")
            import traceback
            print(f"  Details: {traceback.format_exc()[:200]}")
            return None
    
    elif source == "usgs_3dhp":
        # USGS 3D Hydrography Program (replacement for NHD)
        print("\n" + "=" * 60)
        print("USGS 3D Hydrography Program (3DHP)")
        print("=" * 60)
        print("NHD was retired in October 2023. Use 3DHP instead:")
        print("1. Visit: https://www.usgs.gov/3d-hydrography-program/access-3dhp-data-products")
        print("2. Download by Hydrologic Unit (HU)")
        print("3. Santa Fe is in HUC 1302 (Upper Rio Grande)")
        print("4. Download and extract to:", output_dir)
        print("=" * 60)
        return None
    
    elif source == "nm":
        # New Mexico state GIS hydrology data
        print("\n" + "=" * 60)
        print("New Mexico State GIS Hydrology")
        print("=" * 60)
        print("1. Visit: https://www.nmgis.org/")
        print("2. Search for 'hydrology', 'water', or 'rivers'")
        print("3. Download shapefiles for:")
        print("   - Santa Fe County")
        print("   - Rio Grande watershed")
        print("   - Or specific river/stream layers")
        print("4. Save to:", output_dir)
        print("=" * 60)
        return None
    
    else:
        print(f"Unknown source: {source}")
        print("Available sources: 'osm', 'usgs_3dhp', 'nm'")
        return None


def download_city_parcels(
    output_dir: Optional[Path] = None,
    manual_url: Optional[str] = None
) -> Optional[Path]:
    """
    Download city parcels and zoning data.
    
    Note: City GIS portals often require manual download or have specific APIs.
    This function provides guidance and can download if URL is provided.
    
    Parameters
    ----------
    output_dir : Path, optional
        Output directory. Defaults to DATA_RAW
    manual_url : str, optional
        Direct download URL if available
    
    Returns
    -------
    Path or None
        Path to downloaded file, or None if manual download needed
    """
    if output_dir is None:
        output_dir = DATA_RAW
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    if manual_url:
        output_path = output_dir / "city_parcels_zoning.zip"
        print(f"Downloading city parcels from provided URL...")
        download_file(manual_url, output_path)
        return output_path
    
    # City of Santa Fe GIS portal
    print("City of Santa Fe Parcels & Zoning:")
    print("=" * 50)
    print("1. Visit: https://www.santafenm.gov/gis")
    print("2. Look for 'Parcels' or 'Zoning' data layer")
    print("3. Download as Shapefile or GeoJSON")
    print("4. Save to:", output_dir / "city_parcels_zoning.zip")
    print("\nAlternatively, check:")
    print("- ArcGIS Online: https://www.arcgis.com/apps/mapviewer/index.html")
    print("- Search for 'Santa Fe parcels'")
    
    return None


def download_city_limits(
    output_dir: Optional[Path] = None,
    manual_url: Optional[str] = None
) -> Optional[Path]:
    """
    Download Santa Fe city limits boundary.
    
    Parameters
    ----------
    output_dir : Path, optional
        Output directory. Defaults to DATA_RAW
    manual_url : str, optional
        Direct download URL if available
    
    Returns
    -------
    Path or None
        Path to downloaded file, or None if manual download needed
    """
    if output_dir is None:
        output_dir = DATA_RAW
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    if manual_url:
        output_path = output_dir / "city_limits.zip"
        print(f"Downloading city limits from provided URL...")
        download_file(manual_url, output_path)
        return output_path
    
    # Try TIGER/Line places (cities)
    # Santa Fe city FIPS: 3504900
    tiger_url = (
        "https://www2.census.gov/geo/tiger/TIGER2022/PLACE/"
        "tl_2022_35_place.zip"
    )
    
    output_path = output_dir / "nm_places_2022.zip"
    print("Downloading NM places (cities) from Census TIGER/Line...")
    print("Note: Will need to filter for Santa Fe city (PLACEFP=70490)")
    
    try:
        download_file(tiger_url, output_path)
        return output_path
    except Exception as e:
        print(f"Error: {e}")
        print("\nManual download options:")
        print("1. City GIS portal: https://www.santafenm.gov/gis")
        print("2. Census TIGER/Line: https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html")
        return None


def process_downloaded_data(
    dataset_name: str,
    raw_file: Path,
    output_crs: str = None,
    clip_to_city: bool = True
) -> Path:
    """
    Process downloaded raw data: reproject, clip, and save to processed/.
    
    Parameters
    ----------
    dataset_name : str
        Name of dataset (key in DATASET_FILES)
    raw_file : Path
        Path to raw downloaded file
    output_crs : str, optional
        Target CRS. Defaults to LOCAL_CRS
    clip_to_city : bool
        Whether to clip to city limits
    
    Returns
    -------
    Path
        Path to processed file
    """
    from ..config import get_data_path, get_city_limits_path
    
    if output_crs is None:
        output_crs = LOCAL_CRS
    
    # Load raw data
    if raw_file.suffix == '.zip':
        # Extract and find shapefile
        import zipfile
        import tempfile
        
        with tempfile.TemporaryDirectory() as tmpdir:
            with zipfile.ZipFile(raw_file, 'r') as zip_ref:
                zip_ref.extractall(tmpdir)
            
            # Find shapefile
            shp_files = list(Path(tmpdir).rglob("*.shp"))
            if not shp_files:
                raise ValueError(f"No shapefile found in {raw_file}")
            
            gdf = gpd.read_file(shp_files[0])
    else:
        gdf = gpd.read_file(raw_file)
    
    # Set CRS if missing
    if gdf.crs is None:
        print(f"Warning: {dataset_name} has no CRS. Assuming EPSG:4326 (WGS84)")
        gdf = gdf.set_crs("EPSG:4326", allow_override=True)
    
    # Clip to city limits if requested
    if clip_to_city:
        city_limits_path = get_city_limits_path()
        if city_limits_path and city_limits_path.exists():
            city_limits = gpd.read_file(city_limits_path)
            gdf = gpd.clip(gdf, city_limits)
        else:
            print(f"Warning: City limits not found. Skipping clip for {dataset_name}")
    
    # Reproject to target CRS
    if str(gdf.crs) != output_crs:
        gdf = gdf.to_crs(output_crs)
    
    # Save to processed directory
    output_path = get_data_path(dataset_name, processed=True)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    gdf.to_file(output_path, driver="GPKG")
    print(f"Processed {dataset_name} saved to: {output_path}")
    
    return output_path

