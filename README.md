# Pipeline End-to-End de Data Engineering – Datos de Energía Renovable

Estado CI: GitHub Actions habilitado para validación del pipeline

Este repositorio contiene el **Proyecto Integrador Final del Módulo 4 (Data Engineering)**.
El proyecto implementa un **pipeline de datos end-to-end**, que cubre ingesta, procesamiento, orquestación y automatización utilizando herramientas modernas de ingeniería de datos.

El pipeline procesa datos meteorológicos y relacionados con energía renovable siguiendo el patrón de arquitectura **Medallion Architecture**.

---

# Arquitectura del Proyecto

La solución está construida utilizando una arquitectura de **Data Lake** con tres capas de procesamiento:

Bronze → Silver → Gold

### Capa Bronze

Ingesta de datos crudos provenientes de fuentes externas.
Los datos se almacenan sin transformación para preservar el dataset original.

### Capa Silver

Los datos son limpiados, normalizados y transformados utilizando **Apache Spark**.

### Capa Gold

Datasets agregados optimizados para análisis y generación de reportes.

---

# Flujo del Pipeline de Datos

El pipeline realiza los siguientes pasos:

1. Ingesta de datos desde fuentes externas
2. Almacenamiento de datos crudos en la capa Bronze
3. Transformación de datos utilizando Apache Spark
4. Creación de datasets curados en la capa Silver
5. Generación de datasets analíticos en la capa Gold
6. Orquestación del pipeline utilizando Apache Airflow
7. Validación automática del proyecto mediante GitHub Actions

---

# Tecnologías Utilizadas

El proyecto utiliza las siguientes tecnologías:

* Python
* Apache Spark (PySpark)
* Apache Airflow
* Docker
* AWS EC2
* Git y GitHub
* GitHub Actions (CI/CD)
* Parquet

---

# Automatización CI/CD

Se implementa un pipeline de **Integración Continua (CI)** utilizando GitHub Actions.

El workflow de CI realiza automáticamente:

* Instalación de dependencias
* Validación del entorno del pipeline
* Verificación de la estructura del repositorio
* Ejecución de validaciones cada vez que se realiza un *push* al repositorio

Ubicación del workflow:

```
.github/workflows/ci.yml
```

---

# Estructura del Repositorio

```
AVANCE 1
Diseño de arquitectura del pipeline y planificación del Data Lake

AVANCE 2
Implementación del proceso de ingesta de datos

AVANCE 3
Procesamiento y transformación de datos con Apache Spark

AVANCE 4
Orquestación del pipeline y automatización con CI/CD
```

---

# Orquestación del Pipeline

Las tareas del pipeline se orquestan utilizando **DAGs de Apache Airflow**.

El DAG controla:

* Ingesta de datos
* Transformación de datos
* Movimiento de datos entre capas del Data Lake
* Generación del dataset final en la capa Gold

---

# Objetivo del Proyecto

El objetivo del proyecto es demostrar la capacidad de diseñar e implementar un **pipeline de datos de nivel productivo**, incluyendo:

* Ingesta de datos
* Transformación y procesamiento
* Orquestación del pipeline
* Automatización de procesos
* Integración continua (CI/CD)
* Control de versiones mediante Git

---

# Autor

Luis Ramon Buruato
Proyecto Integrador – Data Engineering Módulo 4
