import geopandas as gpd
import csv
import pandas as pd


gdf = gpd.read_file("Graph\Shapes\\federalStates.shp")
# Simplify the geometries
gdf['geometry'] = gdf['geometry'].simplify(tolerance=0.01, preserve_topology=True)
d_names = gdf['Name']
d_geometry = gdf['geometry']

i = 1
D_ID = []
for c in d_names:
    D_ID.append("D"+str(i))
    i = i+1

districts = {"D_ID": D_ID, "Name": d_names, "Geometry": d_geometry}
df_districts = pd.DataFrame(districts)

# Konvertieren der Geometrie zu WKT (Well-Known Text) für den Export in CSV
df_districts['Geometry'] = df_districts['Geometry'].apply(lambda x: x.wkt)

# Speichern als CSV
df_districts.to_csv('Data_Management/id_federalStates.csv', index=False, sep=",")