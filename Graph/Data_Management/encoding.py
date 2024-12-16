import pandas as pd

df = pd.read_csv("Graph\id_cities_pop.csv")

df = pd.DataFrame(df) 
df.to_csv('Graph\id_cities_pop.csv', index=False, sep = ",", encoding='utf-8-sig') 
