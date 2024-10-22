import geopandas as gpd

# Import .shp file into a GeoPandas DataFrame
geopandas_df = gpd.read_file('Graph\Shapes\\federalStates.shp')

# Convert geospatial data to latitude/longitude coordinate system
converted_df = geopandas_df.to_crs('EPSG:4326')

# Write data to CSV
converted_df.to_csv('Data_Management\\federalStates.csv', index=False)