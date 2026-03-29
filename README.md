# 🚀 End-to-End Data Engineering Pipeline – Renewable Energy Data

![Status](https://img.shields.io/badge/status-production--ready-brightgreen)
![CI](https://img.shields.io/badge/CI-GitHub%20Actions-blue)
![Tech](https://img.shields.io/badge/stack-Airflow%20%7C%20Spark%20%7C%20AWS-orange)

---

## 📌 Overview

This project implements a **production-style end-to-end data pipeline** using modern Data Engineering tools.

The pipeline processes **weather and renewable energy data** following a **Medallion Architecture (Bronze → Silver → Gold)** and is fully orchestrated using **Apache Airflow deployed on AWS EC2 with Docker**.

---

## 🧠 Architecture

### 🏗️ Data Lake Layers

```
Bronze → Silver → Gold
```

* **Bronze Layer**

  * Raw data ingestion from external sources
  * No transformations applied

* **Silver Layer**

  * Data cleaning and normalization
  * Processing using Python / PySpark logic

* **Gold Layer**

  * Aggregated datasets optimized for analytics
  * Ready for reporting and downstream consumption

---

## 🔄 Pipeline Flow

The pipeline executes the following steps:

1. Data ingestion from external sources
2. Storage in Bronze layer
3. Data transformation (Silver)
4. Data aggregation (Gold)
5. Orchestration using Apache Airflow
6. Automated validation via CI/CD

---

## ⚙️ Tech Stack

* **Python**
* **Apache Airflow**
* **Apache Spark (PySpark)**
* **Docker**
* **AWS EC2**
* **Parquet**
* **Git & GitHub**
* **GitHub Actions (CI/CD)**

---

## 🧩 Project Structure

```
project/
│
├── dags/
│   ├── pipeline_weather.py
│   ├── process_reviews.py
│   └── create_gold_dataset.py
│
├── .github/workflows/
│   └── ci.yml
│
└── README.md
```

---

## ⚙️ Deployment & Execution Guide

### 1. Connect to EC2

```bash
ssh -i airflow-key.pem ubuntu@<PUBLIC_IP>
```

---

### 2. Run Airflow using Docker

```bash
sudo docker run -d \
  --name airflow \
  -p 8080:8080 \
  apache/airflow:2.8.1 standalone
```

---

### 3. Access Airflow UI

Open in browser:

```
http://<PUBLIC_IP>:8080
```

Retrieve credentials:

```bash
sudo docker logs airflow | grep password
```

---

### 4. Deploy DAG and Scripts

```bash
sudo docker cp pipeline_weather.py airflow:/opt/airflow/dags/
sudo docker cp process_reviews.py airflow:/opt/airflow/dags/
sudo docker cp create_gold_dataset.py airflow:/opt/airflow/dags/
```

---

### 5. Verify DAG Deployment

```bash
sudo docker exec -it airflow ls /opt/airflow/dags
```

---

### 6. Run the Pipeline

1. Open Airflow UI
2. Enable DAG: `pipeline_weather`
3. Click **Trigger DAG**
4. Monitor execution in Graph View

---

### 7. DAG Execution Flow

```
ingest_airbyte → silver_transform → gold_layer
```

---

## 🐞 Troubleshooting

### ❌ File not found inside container

Error:

```
No such file or directory
```

Solution:

```bash
sudo docker cp <file> airflow:/opt/airflow/dags/
```

---

### ❌ Port 8080 not accessible

Solution:

* Open port **8080** in AWS Security Group

---

### ❌ Login issues

Solution:

```bash
sudo docker logs airflow | grep password
```

---

## 📊 Results

* ✅ Pipeline executed successfully end-to-end
* ✅ Data processed across Bronze → Silver → Gold layers
* ✅ Airflow DAG orchestrating multiple tasks
* ✅ Fully deployed in cloud environment (AWS EC2)

---

## 🔄 CI/CD Automation

Continuous Integration is implemented using **GitHub Actions**.

### Workflow includes:

* Dependency installation
* Environment validation
* Pipeline structure checks
* Execution on every push

📍 Location:

```
.github/workflows/ci.yml
```

---

## 🎯 Key Learnings

* Building scalable data pipelines using Airflow
* Deploying services using Docker on AWS EC2
* Debugging real-world pipeline failures
* Managing dependencies inside containerized environments
* Implementing CI/CD for data workflows

---

## 🚀 Future Improvements

* Integrate AWS S3 as Data Lake storage
* Add real Airbyte ingestion pipelines
* Implement Spark cluster processing
* Schedule automated DAG runs (@daily)
* Add monitoring & alerting

---

## 💼 About This Project

This project demonstrates **hands-on experience in Data Engineering**, including:

* Pipeline orchestration
* Cloud deployment
* Containerized environments
* Data transformation workflows

---

## 🏁 Final Result

A fully functional **production-style data pipeline** deployed in AWS and orchestrated with Apache Airflow.

---

## ⭐ If you find this useful

Give it a ⭐ on GitHub and feel free to fork!

---

Proyecto Integrador – Data Engineering Módulo 4
