import pandas as pd

# leer datos desde S3 (Silver)
df = pd.read_parquet("s3://ingesta-airbyte-m4/silver/weather/")

# convertir fecha
df["datetime"] = pd.to_datetime(df["datetime"])
df["date"] = df["datetime"].dt.date

# calcular potencial solar
df["solar_potential"] = df["uvi"] * (1 - df["clouds"]/100)

# calcular potencial eolico
df["wind_power"] = df["wind_speed"] ** 3

# crear tabla Gold
gold = df.groupby(["date","location"]).agg({
"solar_potential":"mean",
"wind_power":"mean"
}).reset_index()

# guardar en S3
gold.to_parquet("s3://ingesta-airbyte-m4/gold/energy_summary/")

print("Gold dataset created successfully")