from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    "pipeline_weather",
    start_date=datetime(2026,3,1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    ingest = BashOperator(
        task_id="ingest_airbyte",
        bash_command="echo Airbyte ingest ok"
    )

    silver = BashOperator(
        task_id="silver_transform",
        bash_command="python /opt/airflow/scripts/silver_manual.py"
    )

    gold = BashOperator(
        task_id="gold_move",
        bash_command="echo move to gold ok"
    )

    ingest >> silver >> gold