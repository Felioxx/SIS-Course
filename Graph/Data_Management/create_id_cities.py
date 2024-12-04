import geopandas as gpd
import csv
import pandas as pd
import centroid


df = pd.read_csv("Graph\Data_Management\cities.csv")
c_names = df.Name #you can also use df['column_name']
c_geometry = df.geometry

# Ids
i = 1
ID = []
for c in c_names:
    ID.append("C"+str(i))
    i = i+1

# Centroid
centroids = []
for g in c_geometry:
    centroids.append(centroid.calculate_centroid(g))

# Area
areas = []
for g in c_geometry:
    areas.append(centroid.calculate_area(g))

cities = {"ID":ID, "Name": c_names, "Geometry": c_geometry, "Centroid": centroids, "Area": areas}

df_cities = pd.DataFrame(cities) 
df_cities.to_csv('Graph\id_cities.csv', index=False, sep = ",") 
