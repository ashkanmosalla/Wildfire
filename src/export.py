import geopandas as gpd

# Define the input shapefile
input_shapefile = r"path.shp"

# Define the output CSV file
output_csv = input_shapefile.replace('.shp', '_with_lat_long.csv')

# Read the shapefile using geopandas
gdf = gpd.read_file(input_shapefile)

# Check the CRS (Coordinate Reference System) of the shapefile
print(f"Original CRS: {gdf.crs}")

# If the CRS is not in EPSG:4326 (WGS 84), reproject it
if gdf.crs != 'EPSG:4326':
    gdf = gdf.to_crs('EPSG:4326')

# Add latitude and longitude columns
gdf['Latitude'] = gdf.geometry.y
gdf['Longitude'] = gdf.geometry.x

# Drop the geometry column if you only want tabular data in the CSV
gdf = gdf.drop(columns='geometry')

# Export to CSV
gdf.to_csv(output_csv, index=False)

print(f"CSV export completed successfully! Output file: {output_csv}")
