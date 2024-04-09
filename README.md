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
![image](https://github.com/amir-jutomate/lamas/assets/142908270/c82d081f-5058-4a7b-9ef3-9a1a853f79f0)

![image](https://github.com/amir-jutomate/lamas/assets/142908270/c856a77d-4432-45cd-b2f3-6fd814241556)

![image](https://github.com/amir-jutomate/lamas/assets/142908270/e3740eb2-67b4-433b-85c5-2200d8d3e469)

![image](https://github.com/amir-jutomate/lamas/assets/142908270/6645cc21-33b3-479b-b124-36f18db35349)

![image](https://github.com/amir-jutomate/lamas/assets/142908270/c8cf520c-aad2-479e-b19a-d3eb235d4015)

![image](https://github.com/amir-jutomate/lamas/assets/142908270/09440b7c-c99a-421b-9561-8e5e2eca431e)


#### Steps for Conversion:
1. Upload your GeoJSON file to mapshaper.org.
2. Use the provided tools to simplify and minimize the file size as needed.
3. Download the optimized TopoJSON file the web is downloaded in JSON.

### Uploading to geojson.io and Conversion to TopoJSON

After optimizing the file size, upload the JSON to [geojson.io](https://geojson.io). 
This platform provides a convenient way to visualize and convert JSON files into TopoJSON format.

![image](https://github.com/amir-jutomate/lamas/assets/142908270/c552a3a9-c9f5-4ffc-a553-6da43353587c)
![image](https://github.com/amir-jutomate/lamas/assets/142908270/39415828-fd80-49f2-aecc-2483b66cef31)

### Steps for Conversion to TopoJSON:

1. Upload GeoJSON: Go to geojson.io and upload your optimized JSON file.
2. Visualize and Convert: Once uploaded, you can view your JSON on the map. Look for the option to convert the file to TopoJSON format on the platform.
3. Download TopoJSON: After conversion, download the TopoJSON file, which is more efficient than the original GeoJSON in Looker Pro.

### What is TopoJSON?

TopoJSON is a type of GeoJSON that reduces file size by removing unnecessary data but keeps all the important details.
It's great for web apps like Looker that have strict file size limits.

### Looker File Size Limitations

Looker has file size limits for Geo/TopoJSON files to keep things running smoothly. 
It's important to make sure your TopoJSON files aren't too big so you can use them in Looker  Pro without any problems.
