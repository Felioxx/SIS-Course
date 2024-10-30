import geopandas as gpd
import csv
import pandas as pd
from shapely.geometry import LineString, MultiPoint, Polygon


df = pd.read_csv("Graph\id_cities.csv")
c_geometry = df.Geometry
c_centroid = []


for city in c_geometry:
    print(city)
    c_centroid.append(Polygon.centroid(city))

print(c_centroid)