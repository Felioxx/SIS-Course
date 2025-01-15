import geopandas as gpd
import csv
import pandas as pd
import centroid

df_cities = pd.read_csv("Graph\id_cities.csv")
df_distances = pd.read_csv("Graph\distances.csv")

#Iterate through each row of df_distances to search for the Name in df_cities. Then add the Id to df_distances
for index, row in df_distances.iterrows():
    nameA = row["CityA"]
    nameB = row["CityB"]
    i = 0
    for el in df_cities.Name:
        do_break = False
        if el == nameA:
            df_distances.at[index, "ID_A"] = df_cities.loc[i]["ID"]
            do_break = True
        if el == nameB:
            df_distances.at[index, "ID_B"] = df_cities.loc[i]["ID"]
            do_break = True
        i = i+1

# Write to csv
df_distances.to_csv("Graph\distances.csv", index=False)