import geopandas as gpd
import csv
import pandas as pd
import centroid

gdf_cities = gpd.read_file("Graph\Data_Management\Shapes\cities.shp")
df_cities = pd.read_csv("Graph\id_cities.csv")
gdf_districts = gpd.read_file("Graph\Data_Management\Shapes\districts.shp")
df_districts = pd.read_csv("Graph\id_districts.csv")
gdf_administrativeDistricts = gpd.read_file("Graph\Data_Management\Shapes\\administrativeDistricts.shp")
df_administrativeDistricts = pd.read_csv("Graph\id_administrativeDistricts.csv")

def buildArray(gdf,df,id_column):
    result_array = []
    i = 0
    for n in gdf.Neighbors:
        name = gdf.Name[i]
        startID = None
        centroidA = None
        # Search startID for name
        j = 0
        for el in df.Name:
            if el == name:
                startID = df.loc[j][id_column]
                centroidA = df.loc[j]["Centroid"]
                break
            j = j+1
        for c in n.split(","):
            endID = None
            centroidB = None
            # Search endID for name
            k = 0
            for el in df.Name:
                if el == c:
                    endID = df.loc[k][id_column]
                    centroidB = df.loc[k]["Centroid"]
                    break
                k = k+1

            # Calculate the relation between the two centroids of the polygons
            rel = centroid.calc_bearing(
                centroidA.replace("POINT (", "").replace(")", "").split(" "), 
                centroidB.replace("POINT (", "").replace(")", "").split(" ")
            )
            # Append the result to the result_array
            result_array.append([startID, endID, rel])
            #print([name, c])
        i = i+1

    return result_array

cities = buildArray(gdf_cities,df_cities,"ID")
districts = buildArray(gdf_districts,df_districts,"ID")
administrativeDistricts = buildArray(gdf_administrativeDistricts,df_administrativeDistricts,"ID")

#Save the result_array as csv
with open('Graph/touches.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["StartID", "EndID", "Rel_Position"])
    writer.writerows(cities)
    writer.writerows(districts)
    writer.writerows(administrativeDistricts)