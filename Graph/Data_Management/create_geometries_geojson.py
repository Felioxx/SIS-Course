import pandas as pd
from shapely.wkt import loads as wkt_loads
from shapely.geometry import mapping
import geojson

df_id_cities = pd.read_csv("Graph\id_cities.csv")
df_id_districts = pd.read_csv("Graph\id_districts.csv")
df_id_administrativeDistricts = pd.read_csv("Graph\id_administrativeDistricts.csv")
df_id_federalStates = pd.read_csv("Graph\id_federalStates.csv")


geojson = {
  "type": "FeatureCollection",
  "features": []
}

feature = {
    "type": "Feature",
    "id": "",
    "geometry": { "type": "Point", "coordinates": [] }
}

for index, row in df_id_cities.iterrows():
    feature["id"] = row["C_ID"]

    polygon = wkt_loads(row["Geometry"])
    geojson_geometry = mapping(polygon)
    #print(geojson_geometry)
    feature["geometry"] = geojson_geometry
    geojson["features"].append(feature)

for index, row in df_id_districts.iterrows():
    feature["id"] = row["D_ID"]

    polygon = wkt_loads(row["Geometry"])
    geojson_geometry = mapping(polygon)
    feature["geometry"] = geojson_geometry
    geojson["features"].append(feature)

for index, row in df_id_administrativeDistricts.iterrows():
    feature["id"] = row["A_ID"]

    polygon = wkt_loads(row["Geometry"])
    geojson_geometry = mapping(polygon)
    feature["geometry"] = geojson_geometry
    geojson["features"].append(feature)

for index, row in df_id_federalStates.iterrows():
    feature["id"] = row["F_ID"]

    polygon = wkt_loads(row["Geometry"])
    geojson_geometry = mapping(polygon)
    feature["geometry"] = geojson_geometry
    geojson["features"].append(feature)

write_file = open("App\public\geometries.geojson", "w")
write_file.write(str(geojson))
write_file.close()