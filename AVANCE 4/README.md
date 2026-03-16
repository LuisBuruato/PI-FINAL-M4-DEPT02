# Avance 4 – Orquestación y CI/CD del Data Pipeline

Este avance corresponde a la **fase final del Proyecto Integrador de Data Engineering (Módulo 4)**.
En esta etapa se implementa la **orquestación completa del pipeline de datos** y la **automatización del flujo de procesamiento**, permitiendo ejecutar de forma controlada las diferentes etapas del Data Lake.

El objetivo es construir un pipeline **automatizado, reproducible y escalable**, utilizando herramientas de orquestación y buenas prácticas de ingeniería de datos.

---

# Arquitectura del Pipeline

El pipeline implementa una arquitectura de **Data Lake basada en el modelo Medallion**, donde los datos pasan por distintas capas de procesamiento:

**Bronze → Silver → Gold**

* **Bronze:** almacenamiento inicial de datos sin procesar.
* **Silver:** datos limpios y transformados.
* **Gold:** datasets listos para análisis y consumo.

La ejecución de estas etapas es coordinada mediante **Apache Airflow**.

---

# Orquestación con Apache Airflow

En este avance se implementa un **DAG (Directed Acyclic Graph)** que permite automatizar la ejecución del pipeline.

El DAG coordina las siguientes tareas:

1. **Ingesta de datos** desde las fuentes definidas.
2. **Transformación de datos** mediante scripts de procesamiento.
3. **Carga de datos transformados** a la capa Gold del Data Lake.
4. **Automatización del flujo completo** mediante dependencias entre tareas.

Esto permite ejecutar el pipeline de manera programada o bajo demanda.

---

# Automatización y CI/CD

Para mejorar la calidad y mantenibilidad del proyecto, se implementó un flujo de **Integración Continua (CI/CD)** mediante **GitHub Actions**.

El pipeline de CI/CD permite:

* Validar automáticamente el código del proyecto.
* Verificar dependencias del entorno.
* Ejecutar controles automáticos al realizar cambios en el repositorio.
* Mantener un flujo de desarrollo más seguro y controlado.

---

# Estructura del Avance 4

La estructura principal del proyecto en este avance incluye:

* **dags/**
  Contiene los DAGs de Apache Airflow que definen la orquestación del pipeline.

* **scripts/**
  Scripts responsables de las transformaciones y movimientos de datos entre las capas del Data Lake.

* **.github/workflows/**
  Configuración del pipeline de CI/CD con GitHub Actions.

* **requirements.txt**
  Dependencias necesarias para ejecutar el pipeline.

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

# Objetivo del avance

El objetivo de este avance es demostrar la implementación de un **pipeline de datos completamente orquestado**, capaz de:

* Automatizar la ejecución de procesos de datos
* Coordinar múltiples etapas del pipeline
* Integrar buenas prácticas de CI/CD
* Facilitar la ejecución reproducible del flujo de datos

---

# Autor

Luis Buruato
Proyecto Integrador – Data Engineering

