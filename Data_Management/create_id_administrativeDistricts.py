import geopandas as gpd
import csv
import pandas as pd


df = pd.read_csv("Data_Management\\administraticeDistricts.csv")
d_names = df.Name #you can also use df['column_name']
d_geometry = df.geometry

i = 1
D_ID = []
for d in d_names:
    D_ID.append("A"+str(i))
    i = i+1

districts = {"A_ID":D_ID, "Name": d_names, "Geometry": d_geometry}

df_districts = pd.DataFrame(districts) 
df_districts.to_csv('Data_Management\id_administraticeDistrics.csv', index=False, sep = ",")

# print(c_names)