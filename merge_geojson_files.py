# Merge geojson files:
import geopandas as gpd
import pandas as pd

# Load the first GeoJSON file into a GeoDataFrame
gdf1 = gpd.read_file('/Users/amiross/Documents/lamas/merged/map.geojson')

# Load the second GeoJSON file into a GeoDataFrame
gdf2 = gpd.read_file('/Users/amiross/Documents/lamas/output_files/metropolin_rings.geojson')

# Load the third GeoJSON file into a GeoDataFrame
# gdf3 = gpd.read_file('/Users/amiross/Documents/lamas/output_files/Metropolin.geojson')

# gdf4 = gpd.read_file('/Users/amiross/Documents/lamas/output_files/Natural_Area.geojson')
#
# gdf5 = gpd.read_file('/Users/amiross/Documents/lamas/output_files/Natural_Area.geojson')
#
# gdf6 = gpd.read_file('/Users/amiross/Documents/lamas/output_files/Natural_Area.geojson')
#
# gdf7 = gpd.read_file('/Users/amiross/Documents/lamas/output_files/Natural_Area.geojson')
#
# gdf8 = gpd.read_file('/Users/amiross/Documents/lamas/output_files/Natural_Area.geojson')

# Concatenate the two GeoDataFrames
merged_gdf = gpd.GeoDataFrame(pd.concat([gdf1, gdf2], ignore_index=True))

# Save the merged GeoDataFrame to a new GeoJSON file
merged_gdf.to_file('/Users/amiross/Documents/lamas/merged/m_n_n_e_t_g_new.geojson', driver='GeoJSON')