from airflow import DAG
from airflow.providers.ssh.operators.ssh import SSHOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'data_engineer',
    'depends_on_past': False,
    'retries': 0
}

with DAG('orquestador_remoto_spark',
         default_args=default_args,
         schedule_interval=timedelta(days=1),
         start_date=datetime(2024, 1, 1),
         catchup=False) as dag:

    ejecutar_etl = SSHOperator(
        task_id='trigger_spark_submit',
        ssh_conn_id='spark_ec2_ssh',  # Conexión SSH configurada en Airflow
        command="""
        docker exec spark-master /opt/spark/bin/spark-submit \
        --master spark://spark-master:7077 \
        --deploy-mode client \
        /opt/spark/process_weather_silver_gold.py
        """
    )