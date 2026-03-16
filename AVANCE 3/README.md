# Proyecto Integrador – Avance 3

## Procesamiento de Datos con Apache Spark (PySpark)

### 📌 Descripción del proyecto

En esta etapa del proyecto se implementa el procesamiento de datos dentro de un **Data Lake** utilizando **Apache Spark con PySpark**.

Los datos provienen de una API meteorológica pública y fueron previamente ingeridos mediante **Airbyte**, almacenándose en **Amazon S3** dentro de la capa **Bronze**.

Posteriormente, se desarrolló un job en PySpark para transformar estos datos y almacenarlos en la capa **Silver** del Data Lake en formato **Parquet**, optimizado para análisis.

---

## 🏗 Arquitectura del pipeline

El flujo de datos sigue una arquitectura **Medallion** dentro del Data Lake:

```
Weather API
     │
     ▼
Airbyte (Ingesta)
     │
     ▼
Amazon S3
     │
     ├── Bronze (datos crudos JSON)
     │
     ▼
Apache Spark (Transformación)
     │
     ▼
Silver (datos procesados en Parquet)
```

---

## ⚙ Tecnologías utilizadas

* Python
* Apache Spark (PySpark)
* Amazon S3
* Airbyte
* Apache Airflow
* AWS EC2

---

## 📂 Estructura del proyecto

```
DE_M4
│
├── spark_jobs
│     └── process_reviews.py
│
├── airflow
│     └── dags
│           └── pipeline_weather.py
│
└── documentation
      └── avance_3_procesamiento_spark.docx
```

---

## 🔄 Procesamiento de datos con PySpark

Se desarrolló un script en PySpark que realiza las siguientes tareas:

1. Conexión a Amazon S3.
2. Lectura de archivos JSON provenientes de la capa Bronze.
3. Conversión de los datos a DataFrames de Spark.
4. Transformación y limpieza de datos.
5. Escritura del dataset transformado en formato Parquet en la capa Silver.

Ejemplo de lectura de datos desde S3:

```python
df = spark.read.json("s3a://ingesta-airbyte-m4/bronze/patagonia/onecall/")
```

Escritura del resultado en formato Parquet:

```python
df.write.mode("overwrite").parquet("s3a://ingesta-airbyte-m4/silver/weather/")
```

---

## 🚀 Optimización del procesamiento

Para mejorar el rendimiento del procesamiento en Spark se aplicaron buenas prácticas:

* Uso del formato **Parquet** para almacenamiento columnar.
* Compresión **Snappy** para reducir tamaño de archivos.
* Procesamiento distribuido mediante Apache Spark.
* Generación de múltiples archivos `part-xxxxx.parquet` que permiten paralelismo.

---

## 📊 Resultados obtenidos

Los datos transformados fueron almacenados en **Amazon S3** dentro de la capa Silver.

Ubicación del dataset:

```
s3://ingesta-airbyte-m4/silver/weather/
```

Archivos generados:

```
_SUCCESS
part-00000.snappy.parquet
part-00001.snappy.parquet
```

El archivo `_SUCCESS` indica que el proceso de Spark finalizó correctamente.

---

## 📸 Evidencias

El proyecto incluye capturas de:

* Script PySpark utilizado para el procesamiento.
* Estructura del Data Lake en Amazon S3.
* Archivos generados en la capa Silver.
* Ejecución del job Spark desde la terminal.

---

## ✅ Conclusión

En este avance se implementó exitosamente el procesamiento de datos dentro del Data Lake utilizando Apache Spark.

Los datos crudos provenientes de la API meteorológica fueron transformados y almacenados en formato Parquet en la capa Silver, optimizando su uso para análisis posteriores.

Este procesamiento prepara los datos para las siguientes etapas del pipeline, incluyendo la orquestación mediante Apache Airflow y su consumo en herramientas de análisis.

---








