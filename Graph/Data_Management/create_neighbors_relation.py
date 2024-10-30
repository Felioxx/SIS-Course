import geopandas as gpd
import csv
import pandas as pd

gdf_cities = gpd.read_file("Graph\Shapes\\cities.shp")
df_cities = pd.read_csv("Data_Management\id_cities.csv")
gdf_districts = gpd.read_file("Graph\Shapes\\districts.shp")
df_districts = pd.read_csv("Data_Management\id_districts.csv")
gdf_administrativeDistricts = gpd.read_file("Graph\Shapes\\administrativeDistricts.shp")
df_administrativeDistricts = pd.read_csv("Data_Management\id_administrativeDistricts.csv")

def buildArray(gdf,df,id_column):
    result_array = []
    i = 0
    for n in gdf.Neighbors:
        name = gdf.Name[i]
        startID = None
        # Search startID for name
        j = 0
        for el in df.Name:
            if el == name:
                startID = df.loc[j][id_column]
                break
            j = j+1
        for c in n.split(","):
            endID = None
            # Search endID for name
            k = 0
            for el in df.Name:
                if el == c:
                    endID = df.loc[k][id_column]
                    break
                k = k+1
            # Append the result to the result_array
            result_array.append([startID, endID])
            #print([name, c])
        i = i+1

    return result_array

cities = buildArray(gdf_cities,df_cities,"C_ID")
districts = buildArray(gdf_districts,df_districts,"D_ID")
administrativeDistricts = buildArray(gdf_administrativeDistricts,df_administrativeDistricts,"A_ID")

# Save the result_array as csv
with open('Data_Management/next_to.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["StartID", "EndID"])
    writer.writerows(cities)
    writer.writerows(districts)
    writer.writerows(administrativeDistricts)