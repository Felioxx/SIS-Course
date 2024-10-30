import geopandas as gpd
import csv
import pandas as pd


df = pd.read_csv("Data_Management\cities.csv")
c_names = df.Name #you can also use df['column_name']
c_geometry = df.geometry

i = 1
C_ID = []
for c in c_names:
    C_ID.append("C"+str(i))
    i = i+1

cities = {"C_ID":C_ID, "Name": c_names, "Geometry": c_geometry}

df_cities = pd.DataFrame(cities) 
df_cities.to_csv('Data_Management\id_cities.csv', index=False, sep = ",") 
