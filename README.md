# Project Lamas
## Overview
This repository contains geojson files provided by our client, Lamas. Due to issues with the original files, we've transferred them to a new format and organized them accordingly.

## Folder Structure
### old_geojson_files
Contains the original geojson files received from the client. These files are outdated and may be broken.

### output_files
This folder houses the new and improved geojson files. We've converted and updated them from the old_geojson_files directory for better usability and reliability.

### topo_jsons
Here reside the topojson files. These are derived from the updated geojson files in the output_files folder. Topojsons offer a more compressed and simplified format, enhancing project efficiency and ease of use.

### merged
The merged folder is designated for uploading merged JSON files. These merged files consolidate multiple layers into a single JSON for streamlined data management.

## GeoJSON to TopoJSON Transformation subject


Based on your requirements, here's a draft for your README that explains the process and includes the provided Python script for transforming GeoJSON files, and subsequent steps for converting GeoJSON to TopoJSON, considering file size limitations. Adjustments can be made to better fit your specific project or documentation style.

## Introduction

This guide shows you how to convert GeoJSON files to TopoJSON for use in Looker. We'll start by explaining what GeoJSON is, then use a Python script to adjust its coordinate system. After that, we'll reduce the file size with `mapshaper.org`, upload it to `geojson.io`, and convert it to TopoJSON. This method helps meet Looker's size limits for such files.

### What is GeoJSON?

GeoJSON is a format for storing different types of geographical data. It can show points, lines, and shapes on a map, along with their details. This makes it easy to work with and share complex geographical information.

### Python Script for CRS Transformation

The Python script uses geopandas and pyproj to open a GeoJSON file, check its coordinate system, change it to a common web mapping format (EPSG:4326), and save the updated file. This makes sure the file works well with mapping tools like Looker Pro.

```python
import geopandas as gpd
from pyproj import Transformer

gdf = gpd.read_file('/path/to/your/original.geojson')
print("Original CRS:", gdf.crs)

gdf_transformed = gdf.to_crs(epsg=4326)
print("Transformed CRS:", gdf_transformed.crs)

gdf_transformed.to_file('/path/to/your/transformed.geojson', driver='GeoJSON')
```

you can find the transformed GeoJSON file in the *fix_geojson_files.py* script's directory.








### Reducing GeoJSON File Size with Mapshaper

To upload and process the new GeoJSON file, navigate to [mapshaper.org](https://mapshaper.org/). This web application allows for file size reduction through simplification and other techniques, which is critical for meeting Looker's file size limitations.

#### Steps for Conversion:
1. Upload your GeoJSON file to mapshaper.org.
2. Use the provided tools to simplify and minimize the file size as needed.
3. Download the optimized GeoJSON file.

### Uploading to geojson.io and Conversion to TopoJSON

After optimizing the file size, upload the GeoJSON to [geojson.io](https://geojson.io). This platform provides a convenient way to visualize and convert GeoJSON files into TopoJSON format, which is more efficient and typically smaller in file size than GeoJSON.

### What is TopoJSON?

TopoJSON is an extension of GeoJSON that encodes topology. It eliminates redundancy, significantly reducing file size while retaining the full precision and detail of the original GeoJSON. This format is particularly useful for web applications like Looker, which may have limitations on the size of GeoJSON/TopoJSON files that can be uploaded.

### Looker File Size Limitations

Looker imposes file size limitations for uploading Geo/TopoJSON files to ensure optimal performance and usability. It's important to keep the size of your TopoJSON files within these limits to ensure they can be uploaded and used within Looker without issues. The process outlined above, including the use of mapshaper.org for file size reduction, is crucial for meeting these restrictions.

## Conclusion

This guide outlines the process for transforming GeoJSON files to TopoJSON, making them suitable for use in Looker by ensuring they meet file size limitations. By following these steps, you can optimize your geographic data for better performance and usability in web applications.

--- 

Make sure to replace `/path/to/your/original.geojson` and `/path/to/your/transformed.geojson` in the Python script with the actual paths to your GeoJSON files. Adjust any part of this README to better fit your project requirements or personal preferences.
