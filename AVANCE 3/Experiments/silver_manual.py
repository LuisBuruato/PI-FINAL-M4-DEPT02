import pandas as pd
import boto3
from io import StringIO

df1 = pd.read_json("data/raw/Patagonia_-41.json")
df2 = pd.read_json("data/raw/Riohacha_11.json")

df = pd.concat([df1, df2])

csv_buffer = StringIO()
df.to_csv(csv_buffer, index=False)

s3 = boto3.client(
    "s3",
    aws_access_key_id="TU_ACCESS_KEY",
    aws_secret_access_key="TU_SECRET_KEY"
)

s3.put_object(
    Bucket="ingesta-airbyte-m4",
    Key="silver/weather_clean/weather_clean.csv",
    Body=csv_buffer.getvalue()
)