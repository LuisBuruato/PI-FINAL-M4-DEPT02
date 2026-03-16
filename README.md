# End-to-End Data Engineering Pipeline – Renewable Energy Data
CI Status: GitHub Actions enabled for pipeline validation

This repository contains the **Final Integrator Project for the Data Engineering Module (M4)**.
The project implements a complete **end-to-end data pipeline**, covering ingestion, processing, orchestration and automation using modern Data Engineering tools.

The pipeline processes renewable energy and weather data and follows the **Medallion Architecture** pattern.

---

# Project Architecture

The solution is built using a **Data Lake architecture** with three processing layers:

Bronze → Silver → Gold

### Bronze Layer

Raw data ingestion from external sources.
Data is stored without transformation to preserve the original dataset.

### Silver Layer

Data is cleaned, normalized and transformed using **Apache Spark**.

### Gold Layer

Aggregated datasets optimized for analytics and reporting.

---

# Data Pipeline Overview

The pipeline performs the following steps:

1. Data ingestion from external sources
2. Storage of raw data in the Bronze layer
3. Data transformation using Spark
4. Creation of curated datasets in Silver
5. Generation of analytical datasets in Gold
6. Pipeline orchestration using Apache Airflow
7. Automated validation with GitHub Actions

---

# Technologies Used

The project uses the following technologies:

* Python
* Apache Spark (PySpark)
* Apache Airflow
* Docker
* AWS EC2
* Git & GitHub
* GitHub Actions (CI/CD)
* Parquet

---

# CI/CD Automation

A **Continuous Integration pipeline** is implemented using GitHub Actions.

The CI workflow automatically:

* Installs dependencies
* Validates the pipeline environment
* Ensures the repository structure is correct
* Executes validation steps on every push

Workflow file location:

```
.github/workflows/ci.yml
```

---

# Repository Structure

```
AVANCE 1
Architecture design and Data Lake planning

AVANCE 2
Data ingestion pipeline implementation

AVANCE 3
Data processing and transformation with Spark

AVANCE 4
Pipeline orchestration and CI/CD automation
```

---

# Pipeline Orchestration

Pipeline tasks are orchestrated using **Apache Airflow DAGs**.

The DAG controls:

* Data ingestion
* Data transformation
* Movement between Data Lake layers
* Final dataset generation

---

# Project Objective

The goal of this project is to demonstrate the ability to design and implement a **production-style data pipeline**, including:

* Data ingestion
* Data transformation
* Data orchestration
* Automation
* CI/CD integration
* Version control using Git

---

# Author

Luis Buruato
Data Engineering Project – Module 4
