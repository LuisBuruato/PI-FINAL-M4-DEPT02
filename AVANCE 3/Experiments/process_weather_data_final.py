from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, TimestampType

# -----------------------------
# Esquema base para weather
# -----------------------------
weather_schema = StructType([
    StructField("city", StringType(), True),
    StructField("temp", DoubleType(), True),
    StructField("humidity", DoubleType(), True),
    StructField("pressure", DoubleType(), True),
    StructField("wind_speed", DoubleType(), True),
    StructField("timestamp", TimestampType(), True)
])

# -----------------------------
# Función para leer JSONL.GZ seguro
# -----------------------------
def read_json_safe(spark, path, schema=weather_schema):
    try:
        df = spark.read.option("multiLine", "false").json(path + "*.jsonl.gz", schema=schema)
        if "_airbyte_data" in df.columns:
            df = df.select("_airbyte_data.*")
        print(f"[INFO] Leídos {df.count()} registros de {path}")
        return df
    except Exception as e:
        print(f"[WARN] No se pudieron leer datos de {path}: {e}")
        # Devuelve un DataFrame vacío con esquema para no romper el flujo
        return spark.createDataFrame([], schema=schema)

# -----------------------------
# Función principal
# -----------------------------
def main():
    # Inicializar Spark
    spark = SparkSession.builder \
        .appName("Avance3_Bronze_to_Silver_and_Gold") \
        .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
        .config("spark.hadoop.fs.s3a.aws.credentials.provider", "com.amazonaws.auth.DefaultAWSCredentialsProviderChain") \
        .config("spark.sql.parquet.compression.codec", "snappy") \
        .config("spark.sql.shuffle.partitions", "10") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("WARN")

    # Rutas S3
    path_bronze_patagonia = "s3://ingesta-airbyte-m4/bronze/patagonia/onecall/"
    path_bronze_riohacha = "s3://ingesta-airbyte-m4/bronze/riohacha/onecall/"
    path_silver = "s3://ingesta-airbyte-m4/silver/"
    path_gold = "s3://ingesta-airbyte-m4/gold/"

    # -----------------------------
    # Leer datos
    # -----------------------------
    df_patagonia = read_json_safe(spark, path_bronze_patagonia)
    df_riohacha = read_json_safe(spark, path_bronze_riohacha)

    # -----------------------------
    # Combinar datasets (ignora vacíos)
    # -----------------------------
    dfs = [df for df in [df_patagonia, df_riohacha] if df.count() > 0]

    if dfs:
        df_silver = dfs[0]
        for df in dfs[1:]:
            df_silver = df_silver.unionByName(df, allowMissingColumns=True)
        df_silver.cache()

        # -----------------------------
        # Guardar Silver en S3 (particionado por ciudad)
        # -----------------------------
        df_silver.write.mode("overwrite").partitionBy("city").parquet(path_silver)
        print(f"[INFO] Silver guardado en {path_silver}")

        # -----------------------------
        # Gold: agregación por ciudad
        # -----------------------------
        if "temp" in df_silver.columns:
            df_gold = df_silver.groupBy("city").agg(avg("temp").alias("avg_temp"))
            df_gold.write.mode("overwrite").parquet(path_gold)
            print(f"[INFO] Gold guardado en {path_gold}")
    else:
        print("[WARN] No hay datos para procesar Silver/Gold")

    spark.stop()
    print("✅ Proceso completado")


if __name__ == "__main__":
    main()