import geopandas as gpd
import csv
import pandas as pd

df_id_cities = pd.read_csv("Graph\Data_Management\id_administrativeDistricts.csv")
df_population = pd.read_csv("Graph\Data_Management\population.csv")
print(df_id_cities)
df_population = df_population.drop(["pop_male", "pop_female"], axis=1)

df_id_cities=pd.merge(df_id_cities, df_population, on='Name', how='left')

df_id_cities = df_id_cities.loc[(df_id_cities['aH'] != "Stadt") & (df_id_cities['aH'] != "Kreis") & (df_id_cities['aH'] != "krfr.Stadt")]
# df_id_cities = df_id_cities.drop("Geometry", axis=1)
df_id_cities = df_id_cities.drop(["aH", "Geometry"], axis=1)

# df_id_cities_none = df_id_cities.loc[(df_id_cities['aH'].isnull() == True)]

print(df_id_cities)

df_cities = pd.DataFrame(df_id_cities) 
df_cities.to_csv('Graph\id_administrativeDistricts_pop.csv', index=False, sep = ",") 


# folium plotlib leaflet bokert