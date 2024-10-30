import geopandas as gpd
import csv
import pandas as pd
from shapely.geometry import LineString, MultiPoint, Polygon


df = pd.read_csv("Graph\id_cities.csv")
c_geometry = df.Geometry
c_centroid = []
print(c_geometry[0].replace("POLYGON", "").replace("(","").replace(")","").split(",")[0].split(" "))

coord_pairs = []
for city in c_geometry:
    coord_pairs.append(city.replace("POLYGON ", "").replace("MULTI", "").replace("(","").replace(")","").split(","))

for pair in coord_pairs:
    c = pair[0].split(" ")
    c_centroid.append((float(c[0]), float(c[1])))

polygon = Polygon(c_centroid)
print(polygon.centroid)

#print(c_centroid)