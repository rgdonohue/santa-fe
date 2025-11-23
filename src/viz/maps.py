"""
Mapping utilities for Santa Fe field notes.
"""

import matplotlib.pyplot as plt
import geopandas as gpd
import contextily as ctx
from typing import Optional, Tuple

from ..config import DEFAULT_CRS


def setup_basemap(
    gdf: gpd.GeoDataFrame,
    crs: Optional[str] = None,
    figsize: Tuple[int, int] = (12, 12),
    alpha: float = 0.7,
    add_basemap: bool = True,
    basemap_source = None
) -> Tuple[plt.Figure, plt.Axes]:
    """
    Set up a basemap with contextily tiles.
    
    Parameters
    ----------
    gdf : gpd.GeoDataFrame
        Data to plot (will be reprojected if needed)
    crs : str, optional
        Target CRS for basemap (default: DEFAULT_CRS from config, usually Web Mercator).
        If None and gdf has no CRS, raises ValueError.
    figsize : tuple
        Figure size (width, height)
    alpha : float
        Transparency for data layers
    add_basemap : bool
        Whether to add contextily basemap tiles (requires internet)
    basemap_source
        Contextily tile source (default: CartoDB Positron)
    
    Returns
    -------
    fig, ax : matplotlib figure and axes
    
    Raises
    ------
    ValueError
        If gdf has no CRS and crs is not provided
    """
    if crs is None:
        crs = DEFAULT_CRS
    
    # Handle missing CRS
    if gdf.crs is None:
        if crs is None:
            raise ValueError(
                "GeoDataFrame has no CRS and no target CRS provided. "
                "Either set CRS on the GeoDataFrame or provide crs parameter."
            )
        # Set CRS assuming it's in the provided CRS
        gdf = gdf.set_crs(crs, allow_override=True)
    
    # Reproject if needed
    if str(gdf.crs) != crs:
        gdf_plot = gdf.to_crs(crs)
    else:
        gdf_plot = gdf.copy()
    
    fig, ax = plt.subplots(figsize=figsize)
    
    # Plot data
    gdf_plot.plot(ax=ax, alpha=alpha)
    
    # Add basemap if requested
    if add_basemap:
        try:
            if basemap_source is None:
                basemap_source = ctx.providers.CartoDB.Positron
            
            ctx.add_basemap(
                ax,
                crs=gdf_plot.crs,
                source=basemap_source,
                attribution_size=6
            )
        except Exception as e:
            print(f"Warning: Could not add basemap: {e}")
            print("Continuing without basemap (offline mode or network issue)")
    
    ax.set_axis_off()
    ax.set_aspect('equal')
    
    # Set tight limits based on data bounds
    bounds = gdf_plot.total_bounds
    ax.set_xlim(bounds[0], bounds[2])
    ax.set_ylim(bounds[1], bounds[3])
    
    return fig, ax


def save_map(
    fig: plt.Figure,
    filename: str,
    output_dir: Optional[str] = None,
    dpi: int = 300
):
    """
    Save map figure to maps/static directory.
    
    Parameters
    ----------
    fig : plt.Figure
        Figure to save
    filename : str
        Output filename (will add .png if no extension)
    output_dir : str, optional
        Output directory. Defaults to MAPS_DIR from config
    dpi : int
        Resolution for saved figure (default: 300)
    """
    from pathlib import Path
    from ..config import MAPS_DIR
    
    if output_dir is None:
        output_dir = MAPS_DIR
    else:
        output_dir = Path(output_dir)
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    if not filename.endswith(('.png', '.jpg', '.pdf')):
        filename += '.png'
    
    output_path = output_dir / filename
    fig.savefig(output_path, dpi=dpi, bbox_inches='tight', facecolor='white')
    print(f"Map saved to {output_path}")

