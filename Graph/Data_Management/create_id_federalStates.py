import geopandas as gpd
import csv
import pandas as pd
import centroid

gdf = gpd.read_file("Graph\Data_Management\Shapes\\federalStates.shp")
# Simplify the geometries
gdf['geometry'] = gdf['geometry'].simplify(tolerance=0.1, preserve_topology=True)
gdf_wgs84 = gdf.to_crs("EPSG:4326")
gdf = gdf_wgs84
d_names = gdf['Name']
d_geometry = gdf['geometry']

i = 1
ID = []
for c in d_names:
    ID.append("F"+str(i))
    i = i+1

# Area
gdf = gdf.to_crs(epsg=3035)
area = round(gdf['geometry'].area / 1000000 , 2)

districts = {"ID": ID, "Name": d_names, "Geometry": d_geometry, "Area": [area]}
df_districts = pd.DataFrame(districts)

# Konvertieren der Geometrie zu WKT (Well-Known Text) für den Export in CSV
df_districts['Geometry'] = df_districts['Geometry'].apply(lambda x: x.wkt)

# Speichern als CSV
df_districts.to_csv('Graph\id_federalStates.csv', index=False, sep=",")