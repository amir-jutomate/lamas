# # GeoJSON:
# import geopandas as gpd
# from pyproj import Transformer
#
# gdf = gpd.read_file('/Users/amiross/Documents/lamas/old_geojson_files/Nafa.geojson')
# print("Original CRS:", gdf.crs)
#
# gdf_transformed = gdf.to_crs(epsg=4326)
# print("Transformed CRS:", gdf_transformed.crs)
#
# gdf_transformed.to_file('/Users/amiross/Documents/lamas/output_files/Nafa.geojson', driver='GeoJSON')


# # TopoJSON - change format and convert to topoJSON:
# import geopandas as gpd
# import topojson as tp

# # Load the GeoJSON file into a GeoDataFrame
# gdf = gpd.read_file('/Users/idanavrahami/Downloads/Nafa.geojson')

# # Reproject to EPSG:4326
# gdf = gdf.to_crs(epsg=4326)

# # Convert GeoDataFrame to TopoJSON
# topology = tp.Topology(gdf, prequantize=False, topology=True)

# # Save the TopoJSON to a file
# topology.to_json('/Users/idanavrahami/Downloads/nafa_transformed.topojson')



# # Geo JSON to TopoJSON convertion - doesn't work:
# import geopandas as gpd
# import topojson as tp

# # Load the GeoJSON file into a GeoDataFrame
# gdf = gpd.read_file('/Users/idanavrahami/Downloads/merged_mahoz_nafa.geojson')

# # Convert GeoDataFrame to TopoJSON
# topology = tp.Topology(gdf, prequantize=False, topology=True)

# # Save the TopoJSON to a file
# topology.to_json('/Users/idanavrahami/Downloads/merged_mahoz_nafa.topojson')



#
# # Merge geojson files:
# import geopandas as gpd
# import pandas as pd
#
# # Load the first GeoJSON file into a GeoDataFrame
# gdf1 = gpd.read_file('/Users/idanavrahami/Downloads/mahoz_transformed.geojson')
#
# # Load the second GeoJSON file into a GeoDataFrame
# gdf2 = gpd.read_file('/Users/idanavrahami/Downloads/nafa_transformed.geojson')
#
# # Concatenate the two GeoDataFrames
# merged_gdf = gpd.GeoDataFrame(pd.concat([gdf1, gdf2], ignore_index=True))
#
# # Save the merged GeoDataFrame to a new GeoJSON file
# merged_gdf.to_file('/Users/idanavrahami/Downloads/merged_mahoz_nafa.geojson', driver='GeoJSON')


#test
