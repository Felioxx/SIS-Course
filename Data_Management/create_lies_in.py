import geopandas as gpd
import csv
import pandas as pd

df_cities = pd.read_csv("Data_Management\cities.csv")
df_id_cities = pd.read_csv("Data_Management\id_cities.csv")


c_id = df_id_cities.C_ID
c_names = df_cities.Name #you can also use df['column_name']
c_d_names = df_cities.NameD

df_districts = pd.read_csv("Data_Management\districts.csv", dtype=object, low_memory=False)
d_ad = df_districts.NameAD

df_districts = pd.read_csv("Data_Management\id_districts.csv", dtype=object, low_memory=False)
d_id = df_districts.D_ID
d_name = df_districts.Name

df_ad_districts = pd.read_csv("Data_Management\id_administraticeDistrics.csv", dtype=object, low_memory=False)
ad_id = df_ad_districts.A_ID
ad_name = df_ad_districts.Name

df_f_districts = pd.read_csv("Data_Management\id_federalStates.csv", dtype=object, low_memory=False)
f_id = df_f_districts.D_ID
f_name = df_f_districts.Name

df_ad_districts = pd.read_csv("Data_Management\\administraticeDistricts.csv", dtype=object, low_memory=False)
a_f_name = df_ad_districts.nameFS

c_lies_in = []
d_lies_in = []
lies_in = {"Start_Point": c_lies_in, "End_Point": d_lies_in}

j=0
for city_id in c_id:   
    i=0
    for district in d_name:    
        if c_d_names[j] == district:
            # print(city_id)
            # print(c_d_names[j])
            # print(d_name[i])
            lies_in["Start_Point"].append(city_id)
            lies_in["End_Point"].append(d_id[i])
        i = i +1   
    j= j+1

j=0
for district_id in d_id:   
    i=0
    for ad_Dis in ad_name:    
        if d_ad[j] == ad_Dis:
            # print(city_id)
            # print(c_d_names[j])
            # print(d_name[i])
            lies_in["Start_Point"].append(district_id)
            lies_in["End_Point"].append(ad_id[i])
        i = i +1   
    j= j+1 


j=0
for adistrict in ad_id:   
    i=0
    for federalState in f_name:    
        if a_f_name[j] == federalState:
            # print(city_id)
            # print(c_d_names[j])
            # print(d_name[i])
            lies_in["Start_Point"].append(adistrict)
            lies_in["End_Point"].append(f_id[i])
        i = i +1   
    j= j+1 

df_lies_in = pd.DataFrame(lies_in) 
df_lies_in.to_csv('Data_Management\lies_in.csv', index=False, sep = ",")