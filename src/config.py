"""
Configuration for Santa Fe geospatial project.

Centralizes data paths, CRS defaults, and other project settings.
Can be overridden via environment variables.
"""

import os
from pathlib import Path
from typing import Optional

# Load .env file if it exists
try:
    from dotenv import load_dotenv
    env_path = Path(__file__).parent.parent / ".env"
    if env_path.exists():
        load_dotenv(env_path)
except ImportError:
    # python-dotenv not installed, skip
    pass


# Project root (parent of src/)
PROJECT_ROOT = Path(__file__).parent.parent

# Data directories
DATA_ROOT = Path(os.getenv("SANTA_FE_DATA_ROOT", PROJECT_ROOT / "data"))
DATA_RAW = DATA_ROOT / "raw"
DATA_PROCESSED = DATA_ROOT / "processed"

# Default CRS settings
# Using Web Mercator (EPSG:3857) for web maps, but can switch to local projection
# NM State Plane Central (EPSG:32113) or UTM Zone 13N (EPSG:32613) for local analysis
DEFAULT_CRS = os.getenv("SANTA_FE_DEFAULT_CRS", "EPSG:3857")
LOCAL_CRS = os.getenv("SANTA_FE_LOCAL_CRS", "EPSG:32113")  # NM State Plane Central

# Map output settings
MAPS_DIR = PROJECT_ROOT / "maps" / "static"
MAP_DPI = 300

# Expected dataset filenames
DATASET_FILES = {
    "parcels": "parcels_zoning.gpkg",
    "census_tracts": "census_tracts_acs.gpkg",
    "hydrology": "hydrology.gpkg",
    "osm": "osm_roads_pois.gpkg",
    "city_limits": "city_limits.gpkg",
}


def get_data_path(dataset_name: str, processed: bool = True) -> Path:
    """
    Get path to a dataset file.
    
    Parameters
    ----------
    dataset_name : str
        Name of dataset (key in DATASET_FILES)
    processed : bool
        If True, look in processed/; otherwise raw/
    
    Returns
    -------
    Path
        Full path to dataset file
    """
    if dataset_name not in DATASET_FILES:
        raise ValueError(
            f"Unknown dataset: {dataset_name}. "
            f"Available: {list(DATASET_FILES.keys())}"
        )
    
    base_dir = DATA_PROCESSED if processed else DATA_RAW
    return base_dir / DATASET_FILES[dataset_name]


def get_city_limits_path() -> Optional[Path]:
    """
    Get path to city limits boundary file.
    
    Returns
    -------
    Path or None
        Path to city limits file if it exists
    """
    path = get_data_path("city_limits", processed=True)
    return path if path.exists() else None


def get_census_api_key() -> Optional[str]:
    """
    Get Census API key from environment variable.
    
    Returns
    -------
    str or None
        Census API key if set, None otherwise
    """
    return os.getenv("CENSUS_API_KEY")

