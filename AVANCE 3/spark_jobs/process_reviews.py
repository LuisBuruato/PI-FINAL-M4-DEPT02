from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Bronze_to_Silver") \
    .config(
        "spark.hadoop.fs.s3a.aws.credentials.provider",
        "com.amazonaws.auth.DefaultAWSCredentialsProviderChain"
    ) \
    .getOrCreate()

# Leer datos desde S3 Bronze
df_patagonia = spark.read.json(
    "s3a://ingesta-airbyte-m4/bronze/patagonia/onecall/*.jsonl.gz"
)

df_riohacha = spark.read.json(
    "s3a://ingesta-airbyte-m4/bronze/riohacha/onecall/*.jsonl.gz"
)

# Combinar datasets
df_silver = df_patagonia.unionByName(
    df_riohacha,
    allowMissingColumns=True
)

# Optimización Spark
df_silver = df_silver.cache()
df_silver = df_silver.repartition(2)

# Ver datos
df_silver.show()

# Guardar en Silver
df_silver.write \
    .mode("overwrite") \
    .parquet("s3a://ingesta-airbyte-m4/silver/weather/")

spark.stop()