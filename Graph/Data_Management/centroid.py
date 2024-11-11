import geopandas as gpd
import csv
import pandas as pd
from shapely.geometry import LineString, MultiPoint, Polygon

# Calculate the centroid of a geometry
def calculate_centroid(c_geometry):

    coord_pairs = []
    coord_pairs.append(c_geometry.replace("POLYGON ", "").replace("MULTI", "").replace("(","").replace(")","").split(", "))

    c_centroid = []
    for pair in coord_pairs[0]:
        c = pair.split(" ")
        if(c[0] != "" and c[1] != ""):
            c_centroid.append((float(c[0]), float(c[1])))

    polygon = Polygon(c_centroid)
    return(polygon.centroid)

# Calculate the realtive postion of two points
# Source: https://math.stackexchange.com/questions/3812110/calculation-of-direction-between-two-geographical-points
def calc_bearing(pointA, pointB):
    import math
    deg2rad = math.pi / 180
    latA = float(pointA[0]) * deg2rad 
    latB = float(pointB[0]) * deg2rad 
    lonA = float(pointA[1]) * deg2rad 
    lonB = float(pointB[1]) * deg2rad 

    delta_ratio = math.log(math.tan(latB/ 2 + math.pi / 4) / math.tan(latA/ 2 + math.pi / 4))
    delta_lon = abs(lonA - lonB)

    negative = False
    if(lonA - lonB < 0):
        negative = True

    delta_lon %= math.pi
    bearing = math.atan2(delta_lon, delta_ratio)/deg2rad

    if negative:
        bearing *= -1
    #return bearing
    if bearing < -157.5:
        return "eastern"
    elif bearing < -112.5:
        return "southeastern"
    elif bearing < -67.5:
        return "southern"
    elif bearing < -22.5:
        return "southwestern"
    elif bearing < 22.5:
        return "western"
    elif bearing < 67.5:
        return "northwestern"
    elif bearing < 112.5:
        return "northern"
    elif bearing < 157.5:
        return "northeastern"
    else:
        return "eastern"
        
