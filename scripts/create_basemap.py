#!/usr/bin/env python3
"""
Create a baseline basemap for Santa Fe.

This script generates a simple, reusable basemap that can serve as a template
for future maps in the project.
"""

import sys
from pathlib import Path

# Add src to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root / "src"))

import geopandas as gpd
import matplotlib.pyplot as plt
from src.data.loaders import load_city_limits
from src.viz.maps import setup_basemap, save_map
from src.config import LOCAL_CRS


def create_baseline_basemap():
    """
    Create a baseline basemap of Santa Fe city limits.
    
    This is a simple, clean map suitable for use as a base layer in other visualizations.
    """
    # Load city limits
    city_limits = load_city_limits()
    
    if city_limits is None:
        print("Error: City limits not found.")
        print("Run notebooks/00_exploratory/000_data_prep.ipynb first to download data.")
        return None
    
    # Create basemap
    # Use Web Mercator for web-friendly basemap tiles
    fig, ax = setup_basemap(
        city_limits,
        crs="EPSG:3857",
        figsize=(12, 12),
        add_basemap=True
    )
    
    # Plot city limits with clean styling
    city_limits_mercator = city_limits.to_crs("EPSG:3857")
    city_limits_mercator.plot(
        ax=ax,
        color='none',
        edgecolor='#2C3E50',
        linewidth=2.5,
        label='Santa Fe City Limits'
    )
    
    # Add title
    ax.set_title(
        'Santa Fe, New Mexico\nBaseline Basemap',
        fontsize=16,
        fontweight='bold',
        pad=20
    )
    
    # Add attribution
    ax.text(
        0.02, 0.02,
        'Data: Census TIGER/Line, CartoDB Positron',
        transform=ax.transAxes,
        fontsize=8,
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8)
    )
    
    # Save
    output_name = 'baseline_basemap_santa_fe'
    save_map(fig, output_name, dpi=300)
    
    print(f"✓ Baseline basemap saved to maps/static/{output_name}.png")
    
    plt.close(fig)
    return fig, ax


if __name__ == "__main__":
    create_baseline_basemap()

