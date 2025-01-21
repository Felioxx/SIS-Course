import geopandas as gpd
import csv
import pandas as pd
from shapely.geometry import LineString, MultiPoint, Polygon

# Format the geometry to use it as a Polygon
def format_geometry(geometry):
    coord_pairs = []
    coord_pairs.append(geometry.replace("POLYGON ", "").replace("MULTI", "").replace("(","").replace(")","").split(", "))

    c_centroid = []
    for pair in coord_pairs[0]:
        c = pair.split(" ")
        if(c[0] != "" and c[1] != ""):
            c_centroid.append((float(c[0]), float(c[1])))

    return c_centroid

# Calculate the centroid of a geometry
def calculate_centroid(c_geometry):
    
    polygon = Polygon(format_geometry(c_geometry))
    return(polygon.centroid)

# Calculate the area of a geometry
def calculate_area(c_geometry):

    polygon = Polygon(format_geometry(c_geometry))
    gdf = gpd.GeoDataFrame({'geometry': [polygon]}, crs="EPSG:4326")
    gdf_utm = gdf.to_crs(epsg=25832)
    area_m2 = gdf_utm['geometry'].area[0]
    return(round(area_m2 / 1000000, 2))

# Calculate the realtive postion of two points
# Source: https://mapscaping.com/how-to-calculate-bearing-between-two-coordinates/
def calc_bearing(pointA, pointB):
    import math
    # Convert latitude and longitude to radians
    lat1 = math.radians(float(pointA[1]))
    long1 = math.radians(float(pointA[0]))
    lat2 = math.radians(float(pointB[1]))
    long2 = math.radians(float(pointB[0]))
    
    # Calculate the bearing
    bearing = math.atan2(
        math.sin(long2 - long1) * math.cos(lat2),
        math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(long2 - long1)
    )
    
    # Convert the bearing to degrees
    bearing = math.degrees(bearing)
    
    # Make sure the bearing is positive
    bearing = (bearing + 360) % 360
    
    #return bearing
    #print(bearing)
    if bearing < 22.5:
        return "northern"
    elif bearing < 67.5:
        return "northeastern"
    elif bearing < 112.5:
        return "eastern"
    elif bearing < 157.5:
        return "southeastern"
    elif bearing < 202.5:
        return "southern"
    elif bearing < 247.5:
        return "southwestern"
    elif bearing < 292.5:
        return "western"
    elif bearing < 337.5:
        return "northwestern"
    else:
        return "northern"
        

#pointB = "POINT (7.4159244216095725 51.77415323183996)".replace("POINT (", "").replace(")", "").split(" ")
#pointA = "POINT (7.485692037043793 51.68379605100887)".replace("POINT (", "").replace(")", "").split(" ")

#print(calc_bearing(pointA, pointB))