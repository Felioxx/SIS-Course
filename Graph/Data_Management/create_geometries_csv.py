import pandas as pd
from shapely.wkt import loads as wkt_loads
from shapely.geometry import mapping
import json

df_id_cities = pd.read_csv("Graph/id_cities.csv")
df_id_districts = pd.read_csv("Graph/id_districts.csv")
df_id_administrativeDistricts = pd.read_csv("Graph/id_administrativeDistricts.csv")
df_id_federalStates = pd.read_csv("Graph/id_federalStates.csv")

def create_geojson_geometry(wkt_geom):
    polygon = wkt_loads(wkt_geom)
    geojson_geometry = mapping(polygon)
    return json.dumps(geojson_geometry)

rows = []

for index, row in df_id_cities.iterrows():
    rows.append({"ID": row["C_ID"], "Geometry": create_geojson_geometry(row["Geometry"])})

for index, row in df_id_districts.iterrows():
    rows.append({"ID": row["D_ID"], "Geometry": create_geojson_geometry(row["Geometry"])})

for index, row in df_id_administrativeDistricts.iterrows():
    rows.append({"ID": row["A_ID"], "Geometry": create_geojson_geometry(row["Geometry"])})

for index, row in df_id_federalStates.iterrows():
    rows.append({"ID": row["F_ID"], "Geometry": create_geojson_geometry(row["Geometry"])})

df_geojson = pd.DataFrame(rows)

output_file = "App\public\geometries.csv"
df_geojson.to_csv(output_file, index=False)