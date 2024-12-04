import geopandas as gpd
import csv
import pandas as pd
import centroid

df = pd.read_csv("Graph\Data_Management\\administrativeDistricts.csv")
d_names = df.Name #you can also use df['column_name']
d_geometry = df.geometry

i = 1
ID = []
for d in d_names:
    ID.append("A"+str(i))
    i = i+1

# Centroid
centroids = []
for g in d_geometry:
    centroids.append(centroid.calculate_centroid(g))

# Area
areas = []
for g in d_geometry:
    areas.append(centroid.calculate_area(g))

districts = {"ID":ID, "Name": d_names, "Geometry": d_geometry, "Centroid": centroids, "Area": areas}

df_districts = pd.DataFrame(districts) 
df_districts.to_csv('Graph\id_administrativeDistricts.csv', index=False, sep = ",")

# print(c_names)