import geopandas as gpd
import csv
import pandas as pd
from shapely.geometry import LineString, MultiPoint, Polygon
import shapely.wkt


df = pd.read_csv("Graph\id_cities.csv")
c_geometry = df.Geometry
c_centroid = []

for city in c_geometry:
    p = shapely.wkt.loads(city)
    c_centroid.append(p.centroid())

print(c_centroid)