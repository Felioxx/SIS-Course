import pandas as pd
import glob

csv_files = ['Graph\Data_Management\distances_cities.csv', 'Graph\Data_Management\distances_districts.csv', 'Graph\Data_Management\distances_administrativeDistricts.csv']

df_list = []

for file in csv_files:
    df = pd.read_csv(file)
    df_list.append(df)

combined_df = pd.concat(df_list, ignore_index=True)

# Speichern der kombinierten CSV-Datei
combined_df.to_csv('Graph\\relates.csv', index=False)

print("Dateien wurden erfolgreich kombiniert!")
