
# Proyecto Integrador – Data Engineering M4

Este repositorio contiene el desarrollo del **Proyecto Integrador del Módulo 4 (Data Engineering)**.
El proyecto implementa un **pipeline de datos completo**, desde la ingesta hasta la orquestación y automatización del flujo de datos.

---

# Estructura del repositorio

El proyecto está organizado en diferentes **avances del módulo**, distribuidos en dos ramas del repositorio.

## Rama `master`

La rama **master** contiene los avances iniciales del proyecto:

### AVANCE 1

* Definición de la arquitectura del Data Pipeline.
* Diseño del Data Lake.
* Selección de tecnologías para ingesta, almacenamiento y procesamiento.

### AVANCE 2

* Implementación de la capa de **ingesta de datos**.
* Integración con APIs o fuentes externas.
* Almacenamiento inicial en la capa **Raw** del Data Lake.

### AVANCE 3

* Implementación de procesos de **transformación de datos**.
* Uso de herramientas de procesamiento como Spark o scripts de transformación.
* Generación de capas intermedias del Data Lake (Bronze / Silver).

---

## Rama `main`

La rama **main** contiene el **AVANCE 4**, donde se completa la automatización del pipeline.

### AVANCE 4 – Orquestación y CI/CD

En esta etapa se implementa:

* Orquestación del pipeline con **Apache Airflow**
* Despliegue del entorno en **AWS EC2**
* Automatización del flujo de datos mediante DAGs
* Manejo de dependencias y ejecución de tareas del pipeline
* Integración de **CI/CD con GitHub Actions**
* Validación automática del pipeline al realizar cambios en el repositorio

El pipeline ejecuta las siguientes etapas:

1. Ingesta de datos
2. Transformación de datos
3. Carga a la capa **Gold** del Data Lake en formato **Parquet**

---

# Tecnologías utilizadas

* Python
* Apache Airflow
* Apache Spark
* Docker
* AWS EC2
* Git y GitHub
* GitHub Actions
* Parquet

---

# Objetivo del proyecto

Construir un **pipeline de datos automatizado, escalable y mantenible**, capaz de:

* Ingerir datos desde distintas fuentes
* Transformarlos mediante procesos ETL
* Orquestar el flujo completo con Airflow
* Implementar integración continua (CI/CD)
* Mantener control de versiones mediante Git

---

# Autor

Luis Buruato
Proyecto Integrador – Data Engineering
=======
📘 README — AVANCE 1.

AVANCE 1 – Diseño de Arquitectura del Pipeline
Descripción

En este primer avance se plantea el diseño de la arquitectura del pipeline de datos que será desarrollado durante el proyecto integrador.

El objetivo principal es definir cómo fluirán los datos desde las fuentes originales hasta las capas finales de análisis dentro de un Data Lake.

Objetivos del avance

Definir la arquitectura general del pipeline de datos.

Diseñar la estructura del Data Lake.

Identificar las herramientas y tecnologías a utilizar.

Establecer el flujo de procesamiento de datos.

Arquitectura del pipeline

El flujo de datos propuesto sigue las siguientes etapas:

Fuente de datos
↓
Proceso de ingesta
↓
Data Lake (Raw Layer)
↓
Procesamiento y transformación
↓
Data Lake (Silver / Gold)
↓
Consumo analítico

Tecnologías consideradas

Durante el diseño se seleccionaron las siguientes herramientas:

Python

Apache Spark

Apache Airflow

Docker

AWS Cloud Services

Git y GitHub

Resultado del avance

Se definió la arquitectura base del sistema de datos, que servirá como guía para la implementación de los siguientes avances del proyecto.

📘 README — AVANCE 2

AVANCE 2 – Implementación de Ingesta de Datos
Descripción

En este avance se desarrolla el proceso de ingesta de datos, que permite obtener información desde fuentes externas y almacenarla en la capa inicial del Data Lake.

El objetivo es construir un mecanismo que permita capturar datos de forma estructurada para su posterior procesamiento.

Objetivos del avance

Implementar scripts de extracción de datos.

Conectar con fuentes de datos externas (APIs o datasets).

Almacenar los datos en la capa Raw del Data Lake.

Garantizar que los datos estén disponibles para procesos de transformación posteriores.

Flujo de ingesta

El proceso de ingesta sigue el siguiente flujo:

Fuente de datos
↓
Script de extracción
↓
Validación básica
↓
Carga al Data Lake (Raw)

Tecnologías utilizadas

Para implementar esta etapa se utilizaron:

Python

APIs públicas

Scripts de extracción de datos

Almacenamiento estructurado de archivos

Resultado del avance

Se implementó un sistema inicial de ingesta de datos, permitiendo capturar información desde las fuentes y almacenarla correctamente dentro del Data Lake.

📘 README — AVANCE 3

AVANCE 3 – Transformación y Procesamiento de Datos
Descripción

En este avance se implementa la etapa de transformación de datos, donde los datos almacenados en la capa Raw son procesados para generar información estructurada y lista para análisis.

El objetivo es limpiar, transformar y estructurar los datos para generar datasets de mayor calidad.

Objetivos del avance

Procesar los datos provenientes de la capa Raw.

Realizar procesos de limpieza y normalización de datos.

Generar datasets estructurados.

Preparar la información para su consumo analítico.

Flujo de transformación

El procesamiento de datos sigue el siguiente flujo:

Datos Raw
↓
Limpieza de datos
↓
Transformación de estructuras
↓
Optimización del formato
↓
Almacenamiento en capas superiores del Data Lake

Tecnologías utilizadas

Para esta etapa se emplearon las siguientes herramientas:

Python

Apache Spark

Procesamiento de datos distribuido

Formato de almacenamiento optimizado Parquet

Resultado del avance

Se generaron datasets transformados y estructurados, listos para ser utilizados en procesos analíticos o sistemas de visualización.
>>>>>>> c8b27c64ab8f00e125089f8d7d4b9b8b237d62b2
