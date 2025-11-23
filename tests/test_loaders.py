"""
Smoke tests for data loaders.

Tests basic functionality with small fixture data.
"""

import pytest
import geopandas as gpd
from pathlib import Path
import tempfile
import shutil

from src.data.loaders import (
    load_parcels,
    load_census_tracts,
    load_hydrology,
    load_osm_infrastructure,
    load_city_limits,
    get_santa_fe_bounds
)
from src.config import get_data_path


@pytest.fixture
def temp_data_dir():
    """Create temporary data directory for tests."""
    temp_dir = Path(tempfile.mkdtemp())
    processed_dir = temp_dir / "processed"
    processed_dir.mkdir(parents=True)
    yield processed_dir
    shutil.rmtree(temp_dir)


def test_load_parcels_with_fixture(temp_data_dir):
    """Test loading parcels with fixture data."""
    # Copy fixture to temp directory
    fixture_path = Path(__file__).parent / "fixtures" / "sample_parcel.geojson"
    target_path = temp_data_dir / "parcels_zoning.gpkg"
    
    gdf = gpd.read_file(fixture_path)
    gdf = gdf.set_crs("EPSG:4326")
    gdf.to_file(target_path, driver="GPKG")
    
    # Test loading
    result = load_parcels(data_dir=temp_data_dir)
    assert isinstance(result, gpd.GeoDataFrame)
    assert len(result) > 0
    assert "geometry" in result.columns


def test_load_parcels_crs_validation(temp_data_dir):
    """Test CRS validation in load_parcels."""
    fixture_path = Path(__file__).parent / "fixtures" / "sample_parcel.geojson"
    target_path = temp_data_dir / "parcels_zoning.gpkg"
    
    gdf = gpd.read_file(fixture_path)
    gdf = gdf.set_crs("EPSG:4326")
    gdf.to_file(target_path, driver="GPKG")
    
    # Should work with correct CRS
    result = load_parcels(data_dir=temp_data_dir, expected_crs="EPSG:4326")
    assert result is not None
    
    # Should raise with wrong CRS
    with pytest.raises(ValueError, match="CRS mismatch"):
        load_parcels(data_dir=temp_data_dir, expected_crs="EPSG:3857")


def test_load_parcels_column_validation(temp_data_dir):
    """Test column validation in load_parcels."""
    fixture_path = Path(__file__).parent / "fixtures" / "sample_parcel.geojson"
    target_path = temp_data_dir / "parcels_zoning.gpkg"
    
    gdf = gpd.read_file(fixture_path)
    gdf = gdf.set_crs("EPSG:4326")
    gdf.to_file(target_path, driver="GPKG")
    
    # Should work with existing columns
    result = load_parcels(
        data_dir=temp_data_dir,
        required_columns=["parcel_id", "zoning"]
    )
    assert result is not None
    
    # Should raise with missing columns
    with pytest.raises(ValueError, match="missing required columns"):
        load_parcels(
            data_dir=temp_data_dir,
            required_columns=["nonexistent_column"]
        )


def test_load_parcels_missing_file():
    """Test error handling for missing file."""
    with pytest.raises(FileNotFoundError):
        load_parcels(data_dir=Path("/nonexistent/path"))


def test_load_census_tracts_with_fixture(temp_data_dir):
    """Test loading census tracts with fixture data."""
    fixture_path = Path(__file__).parent / "fixtures" / "sample_tract.geojson"
    target_path = temp_data_dir / "census_tracts_acs.gpkg"
    
    gdf = gpd.read_file(fixture_path)
    gdf = gdf.set_crs("EPSG:4326")
    gdf.to_file(target_path, driver="GPKG")
    
    result = load_census_tracts(data_dir=temp_data_dir)
    assert isinstance(result, gpd.GeoDataFrame)
    assert len(result) > 0


def test_get_santa_fe_bounds():
    """Test getting Santa Fe bounds."""
    bounds = get_santa_fe_bounds()
    assert "minx" in bounds
    assert "miny" in bounds
    assert "maxx" in bounds
    assert "maxy" in bounds
    assert bounds["minx"] < bounds["maxx"]
    assert bounds["miny"] < bounds["maxy"]

