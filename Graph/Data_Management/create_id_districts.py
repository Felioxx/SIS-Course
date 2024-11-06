import geopandas as gpd
import csv
import pandas as pd
import centroid

df = pd.read_csv("Graph\Data_Management\districts.csv")
d_names = df.Name #you can also use df['column_name']
d_geometry = df.geometry

i = 1
D_ID = []
for d in d_names:
    D_ID.append("D"+str(i))
    i = i+1

# Centroid
centroids = []
for g in d_geometry:
    centroids.append(centroid.calculate_centroid(g))

districts = {"D_ID":D_ID, "Name": d_names, "Geometry": d_geometry, "Centroid": centroids}

df_districts = pd.DataFrame(districts) 
df_districts.to_csv('Graph\id_districts.csv', index=False, sep = ",")

# print(c_names)