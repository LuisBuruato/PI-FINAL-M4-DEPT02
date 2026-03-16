import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.utils import AnalysisException

def main():

    spark = SparkSession.builder \
        .appName("Weather ETL") \
        .getOrCreate()
    spark.conf.set("spark.sql.shuffle.partitions", 10)  # Optimización

    # 🔹 Rutas S3
    path_patagonia = "s3://ingesta-airbyte-m4/raw/patagonia/"
    path_riohacha = "s3://ingesta-airbyte-m4/raw/riohacha/"
    silver_path = "s3://ingesta-airbyte-m4/silver/"
    gold_path = "s3://ingesta-airbyte-m4/gold/"

    def read_json_safe(path):
        """Lee todos los JSONL.GZ de una carpeta y maneja errores"""
        try:
            df = spark.read.option("multiLine", "false").json(path + "*.jsonl.gz")
            if "_airbyte_data" in df.columns:
                df = df.select("_airbyte_data.*")
            print(f"[INFO] Leídos {df.count()} registros de {path}")
            return df
        except AnalysisException as e:
            print(f"[ERROR] Problema leyendo {path}: {e}")
            return spark.createDataFrame([], schema=None)
        except Exception as e:
            print(f"[ERROR] Otro error leyendo {path}: {e}")
            return spark.createDataFrame([], schema=None)

    # 🔹 Leer datos
    df_patagonia = read_json_safe(path_patagonia)
    df_riohacha = read_json_safe(path_riohacha)

    # 🔹 Combinar datasets
    df_silver = df_patagonia.unionByName(df_riohacha)
    print(f"[INFO] Total registros combinados antes de filtrar: {df_silver.count()}")

    # 🔹 Filtrar registros válidos
    df_silver = df_silver.filter(col("temperature").isNotNull())
    print(f"[INFO] Total registros después de filtrar temperature nulo: {df_silver.count()}")

    # 🔹 Cache para optimización
    df_silver.cache()

    # 🔹 Guardar Silver en S3
    df_silver.write.mode("overwrite").partitionBy("city").parquet(silver_path)
    print(f"[INFO] Silver guardado en {silver_path}")

    # 🔹 Gold: agregación por ciudad
    df_gold = df_silver.groupBy("city").avg("temperature").withColumnRenamed("avg(temperature)", "avg_temperature")
    print(f"[INFO] Total ciudades en Gold: {df_gold.count()}")

    # 🔹 Guardar Gold en S3
    df_gold.write.mode("overwrite").parquet(gold_path)
    print(f"[INFO] Gold guardado en {gold_path}")

    print("✅ Proceso completado con éxito")
    spark.stop()

if __name__ == "__main__":
    main()