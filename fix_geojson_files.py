# GeoJSON:
import geopandas as gpd
from pyproj import Transformer

gdf = gpd.read_file('/Users/amiross/Documents/lamas/old_geojson_files/Nafa.geojson')
print("Original CRS:", gdf.crs)

gdf_transformed = gdf.to_crs(epsg=4326)
print("Transformed CRS:", gdf_transformed.crs)

gdf_transformed.to_file('/Users/amiross/Documents/lamas/output_files/Nafa.geojson', driver='GeoJSON')