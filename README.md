# 🚀 End-to-End Data Engineering Pipeline – Renewable Energy Data

![Status](https://img.shields.io/badge/status-production--ready-brightgreen)
![CI](https://img.shields.io/badge/CI-GitHub%20Actions-blue)
![Stack](https://img.shields.io/badge/stack-Airflow%20%7C%20Spark%20%7C%20AWS-orange)

---

## 📌 Overview

This project implements a **production-style end-to-end data pipeline** using modern Data Engineering tools.

It processes **weather and renewable energy data** using a **Medallion Architecture (Bronze → Silver → Gold)** and is fully orchestrated using **Apache Airflow deployed on AWS EC2 with Docker**.

Additionally, it includes a **Streamlit dashboard** for data visualization.

---

## 🧠 Architecture

```text
Bronze → Silver → Gold
```

* **Bronze Layer**

  * Raw data ingestion from external sources
* **Silver Layer**

  * Data cleaning and transformation
* **Gold Layer**

  * Aggregated datasets for analytics

---

## 🔄 Pipeline Flow

1. Data ingestion
2. Bronze storage
3. Data transformation (Silver)
4. Aggregation (Gold)
5. Orchestration with Airflow
6. Visualization with Streamlit

---

## ⚙️ Tech Stack

* Python
* Apache Airflow
* Apache Spark (PySpark)
* Docker
* AWS EC2
* Parquet
* Git & GitHub
* GitHub Actions (CI/CD)
* Streamlit

---

## 🧩 Project Structure

```text
project/
│
├── dags/
│   ├── pipeline_weather.py
│   ├── process_reviews.py
│   └── create_gold_dataset.py
│
├── app.py
├── .github/workflows/ci.yml
└── README.md
```

---

## ⚙️ Deployment & Execution Guide

### 1. Connect to EC2

```bash
ssh -i airflow-key.pem ubuntu@<PUBLIC_IP>
```

---

### 2. Run Airflow (Docker)

```bash
sudo docker run -d \
  --name airflow \
  -p 8080:8080 \
  apache/airflow:2.8.1 standalone
```

---

### 3. Access Airflow

```
http://<PUBLIC_IP>:8080
```

```bash
sudo docker logs airflow | grep password
```

---

### 4. Deploy DAGs

```bash
sudo docker cp pipeline_weather.py airflow:/opt/airflow/dags/
sudo docker cp process_reviews.py airflow:/opt/airflow/dags/
sudo docker cp create_gold_dataset.py airflow:/opt/airflow/dags/
```

---

### 5. Run Pipeline

* Enable DAG: `pipeline_weather`
* Click **Trigger DAG**
* Monitor execution

---

### 6. DAG Flow

```text
ingest_airbyte → silver_transform → gold_layer
```

---

## 📊 Data Visualization (Streamlit)

### Run dashboard

```bash
streamlit run app.py --server.port 8503 --server.address 0.0.0.0
```

---

### Access dashboard

```
http://<PUBLIC_IP>:8503
```

---

### Features

* Interactive dashboard
* Displays Silver & Gold datasets
* Real-time updates

---

## 🐞 Troubleshooting

### Missing files in Docker

```bash
sudo docker cp <file> airflow:/opt/airflow/dags/
```

---

### Airflow not accessible

* Open port 8080 in AWS Security Group

---

### Streamlit errors (S3)

```bash
aws configure
```

Ensure:

* Correct Access Key
* Correct Secret Key
* Correct Region

---

## 📊 Results

* ✅ Pipeline executed end-to-end
* ✅ Data processed across layers
* ✅ Dashboard visualization working
* ✅ Deployed in AWS cloud

---

## 🔄 CI/CD

GitHub Actions pipeline:

* Dependency validation
* Project structure checks
* Triggered on push

```
.github/workflows/ci.yml
```

---

## 🎯 Key Learnings

* Airflow orchestration
* Docker containerization
* AWS deployment
* Debugging real pipelines
* Data pipeline architecture

---

## 🚀 Future Improvements

* Integrate AWS S3 Data Lake
* Add real Airbyte ingestion
* Use Spark cluster
* Schedule DAG runs
* Add monitoring

---

## 💼 Project Impact

This project demonstrates **real-world Data Engineering skills**, including:

* Cloud deployment
* Pipeline orchestration
* Data processing workflows
* Full-stack data applications

---

## ⭐ Final Result

A fully functional **production-style data pipeline with visualization layer** deployed in AWS.

---
