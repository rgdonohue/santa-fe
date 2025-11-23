"""
Data loading utilities for Santa Fe geospatial datasets.
"""

import geopandas as gpd
import pandas as pd
from pathlib import Path
from typing import Optional, List

from ..config import get_data_path, DATA_PROCESSED, get_city_limits_path


def load_parcels(
    data_dir: Optional[Path] = None,
    expected_crs: Optional[str] = None,
    required_columns: Optional[List[str]] = None
) -> gpd.GeoDataFrame:
    """
    Load city parcels + zoning data.
    
    Parameters
    ----------
    data_dir : Path, optional
        Base data directory. Defaults to config DATA_PROCESSED
    expected_crs : str, optional
        Expected CRS (e.g., 'EPSG:3857'). If provided, validates CRS matches.
    required_columns : list of str, optional
        Required column names. If provided, validates columns exist.
    
    Returns
    -------
    gpd.GeoDataFrame
        Parcels with zoning information
    
    Raises
    ------
    FileNotFoundError
        If dataset file doesn't exist
    ValueError
        If CRS or columns don't match expectations
    """
    if data_dir is None:
        parcels_path = get_data_path("parcels", processed=True)
    else:
        parcels_path = data_dir / "parcels_zoning.gpkg"
    
    if not parcels_path.exists():
        raise FileNotFoundError(
            f"Parcels data not found at {parcels_path}. "
            "Download from City of Santa Fe GIS and process first. "
            f"Expected location: {get_data_path('parcels', processed=True)}"
        )
    
    gdf = gpd.read_file(parcels_path)
    
    # Validate CRS
    if expected_crs is not None:
        if gdf.crs is None:
            raise ValueError(
                f"Parcels data has no CRS. Expected {expected_crs}. "
                "Set CRS during data processing."
            )
        if str(gdf.crs) != expected_crs:
            raise ValueError(
                f"Parcels CRS mismatch: got {gdf.crs}, expected {expected_crs}. "
                "Reproject during data processing."
            )
    
    # Validate columns
    if required_columns is not None:
        missing = set(required_columns) - set(gdf.columns)
        if missing:
            raise ValueError(
                f"Parcels data missing required columns: {missing}. "
                f"Available columns: {list(gdf.columns)}"
            )
    
    return gdf


def load_census_tracts(
    data_dir: Optional[Path] = None,
    expected_crs: Optional[str] = None,
    required_columns: Optional[List[str]] = None
) -> gpd.GeoDataFrame:
    """
    Load census tracts with ACS demographics.
    
    Parameters
    ----------
    data_dir : Path, optional
        Base data directory. Defaults to config DATA_PROCESSED
    expected_crs : str, optional
        Expected CRS. If provided, validates CRS matches.
    required_columns : list of str, optional
        Required column names. If provided, validates columns exist.
    
    Returns
    -------
    gpd.GeoDataFrame
        Census tracts with demographic attributes
    
    Raises
    ------
    FileNotFoundError
        If dataset file doesn't exist
    ValueError
        If CRS or columns don't match expectations
    """
    if data_dir is None:
        tracts_path = get_data_path("census_tracts", processed=True)
    else:
        tracts_path = data_dir / "census_tracts_acs.gpkg"
    
    if not tracts_path.exists():
        raise FileNotFoundError(
            f"Census tracts data not found at {tracts_path}. "
            "Download from Census Bureau and process first. "
            f"Expected location: {get_data_path('census_tracts', processed=True)}"
        )
    
    gdf = gpd.read_file(tracts_path)
    
    if expected_crs is not None:
        if gdf.crs is None:
            raise ValueError(
                f"Census tracts data has no CRS. Expected {expected_crs}. "
                "Set CRS during data processing."
            )
        if str(gdf.crs) != expected_crs:
            raise ValueError(
                f"Census tracts CRS mismatch: got {gdf.crs}, expected {expected_crs}. "
                "Reproject during data processing."
            )
    
    if required_columns is not None:
        missing = set(required_columns) - set(gdf.columns)
        if missing:
            raise ValueError(
                f"Census tracts missing required columns: {missing}. "
                f"Available columns: {list(gdf.columns)}"
            )
    
    return gdf


def load_hydrology(
    data_dir: Optional[Path] = None,
    expected_crs: Optional[str] = None
) -> gpd.GeoDataFrame:
    """
    Load Santa Fe River + arroyos / hydrology layer.
    
    Parameters
    ----------
    data_dir : Path, optional
        Base data directory. Defaults to config DATA_PROCESSED
    expected_crs : str, optional
        Expected CRS. If provided, validates CRS matches.
    
    Returns
    -------
    gpd.GeoDataFrame
        River, arroyos, and flow paths
    
    Raises
    ------
    FileNotFoundError
        If dataset file doesn't exist
    ValueError
        If CRS doesn't match expectations
    """
    if data_dir is None:
        hydro_path = get_data_path("hydrology", processed=True)
    else:
        hydro_path = data_dir / "hydrology.gpkg"
    
    if not hydro_path.exists():
        raise FileNotFoundError(
            f"Hydrology data not found at {hydro_path}. "
            "Download from source and process first. "
            f"Expected location: {get_data_path('hydrology', processed=True)}"
        )
    
    gdf = gpd.read_file(hydro_path)
    
    if expected_crs is not None:
        if gdf.crs is None:
            raise ValueError(
                f"Hydrology data has no CRS. Expected {expected_crs}. "
                "Set CRS during data processing."
            )
        if str(gdf.crs) != expected_crs:
            raise ValueError(
                f"Hydrology CRS mismatch: got {gdf.crs}, expected {expected_crs}. "
                "Reproject during data processing."
            )
    
    return gdf


def load_osm_infrastructure(
    data_dir: Optional[Path] = None,
    expected_crs: Optional[str] = None
) -> gpd.GeoDataFrame:
    """
    Load OSM roads + POIs.
    
    Parameters
    ----------
    data_dir : Path, optional
        Base data directory. Defaults to config DATA_PROCESSED
    expected_crs : str, optional
        Expected CRS. If provided, validates CRS matches.
    
    Returns
    -------
    gpd.GeoDataFrame
        Roads and points of interest from OpenStreetMap
    
    Raises
    ------
    FileNotFoundError
        If dataset file doesn't exist
    ValueError
        If CRS doesn't match expectations
    """
    if data_dir is None:
        osm_path = get_data_path("osm", processed=True)
    else:
        osm_path = data_dir / "osm_roads_pois.gpkg"
    
    if not osm_path.exists():
        raise FileNotFoundError(
            f"OSM data not found at {osm_path}. "
            "Download from GeoFabrik/Overpass API and process first. "
            f"Expected location: {get_data_path('osm', processed=True)}"
        )
    
    gdf = gpd.read_file(osm_path)
    
    if expected_crs is not None:
        if gdf.crs is None:
            raise ValueError(
                f"OSM data has no CRS. Expected {expected_crs}. "
                "Set CRS during data processing."
            )
        if str(gdf.crs) != expected_crs:
            raise ValueError(
                f"OSM CRS mismatch: got {gdf.crs}, expected {expected_crs}. "
                "Reproject during data processing."
            )
    
    return gdf


def load_city_limits(data_dir: Optional[Path] = None) -> Optional[gpd.GeoDataFrame]:
    """
    Load Santa Fe city limits boundary.
    
    Parameters
    ----------
    data_dir : Path, optional
        Base data directory. Defaults to config DATA_PROCESSED
    
    Returns
    -------
    gpd.GeoDataFrame or None
        City limits boundary if file exists, None otherwise
    """
    city_limits_path = get_city_limits_path()
    if city_limits_path is None:
        if data_dir is not None:
            city_limits_path = data_dir / "city_limits.gpkg"
            if not city_limits_path.exists():
                return None
        else:
            return None
    
    return gpd.read_file(city_limits_path)


def get_santa_fe_bounds() -> dict:
    """
    Get bounding box for Santa Fe city limits.
    
    Tries to load actual city limits file first, falls back to approximate bounds.
    
    Returns
    -------
    dict
        Bounding box as {'minx', 'miny', 'maxx', 'maxy'}
    """
    city_limits = load_city_limits()
    if city_limits is not None:
        bounds = city_limits.total_bounds
        return {
            'minx': bounds[0],
            'miny': bounds[1],
            'maxx': bounds[2],
            'maxy': bounds[3]
        }
    
    # Fallback to approximate bounds for Santa Fe, NM
    return {
        'minx': -106.0,
        'miny': 35.6,
        'maxx': -105.8,
        'maxy': 35.8
    }

