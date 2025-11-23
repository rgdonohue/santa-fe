"""
Smoke tests for mapping utilities.
"""

import pytest
import geopandas as gpd
import matplotlib.pyplot as plt
from pathlib import Path
import tempfile
import shutil

from src.viz.maps import setup_basemap, save_map
from src.config import MAPS_DIR


@pytest.fixture
def sample_gdf():
    """Create a sample GeoDataFrame for testing."""
    from shapely.geometry import Point
    gdf = gpd.GeoDataFrame(
        {"name": ["A", "B"]},
        geometry=[Point(-105.95, 35.65), Point(-105.94, 35.66)],
        crs="EPSG:4326"
    )
    return gdf


def test_setup_basemap_with_crs(sample_gdf):
    """Test setup_basemap with valid CRS."""
    fig, ax = setup_basemap(sample_gdf, crs="EPSG:3857", add_basemap=False)
    assert fig is not None
    assert ax is not None
    plt.close(fig)


def test_setup_basemap_no_crs_error():
    """Test setup_basemap raises error when CRS is missing."""
    from shapely.geometry import Point
    gdf_no_crs = gpd.GeoDataFrame(
        {"name": ["A"]},
        geometry=[Point(-105.95, 35.65)]
    )
    
    with pytest.raises(ValueError, match="no CRS"):
        setup_basemap(gdf_no_crs, crs=None, add_basemap=False)


def test_setup_basemap_sets_crs_when_missing():
    """Test setup_basemap sets CRS when provided."""
    from shapely.geometry import Point
    gdf_no_crs = gpd.GeoDataFrame(
        {"name": ["A"]},
        geometry=[Point(-105.95, 35.65)]
    )
    
    fig, ax = setup_basemap(gdf_no_crs, crs="EPSG:4326", add_basemap=False)
    assert fig is not None
    plt.close(fig)


def test_save_map(temp_data_dir):
    """Test saving a map figure."""
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [1, 2, 3])
    
    save_map(fig, "test_map", output_dir=temp_data_dir)
    
    expected_path = temp_data_dir / "test_map.png"
    assert expected_path.exists()
    
    plt.close(fig)


def test_save_map_auto_png_extension(temp_data_dir):
    """Test that save_map adds .png extension if missing."""
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [1, 2, 3])
    
    save_map(fig, "test_map_no_ext", output_dir=temp_data_dir)
    
    expected_path = temp_data_dir / "test_map_no_ext.png"
    assert expected_path.exists()
    
    plt.close(fig)

