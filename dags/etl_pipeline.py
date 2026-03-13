from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="etl_pipeline",
    start_date=datetime(2024,1,1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    extract = BashOperator(
        task_id="extract_api",
        bash_command="python /opt/airflow/scripts/api_extract.py"
    )

    transform = BashOperator(
        task_id="transform_data",
        bash_command="python /opt/airflow/scripts/spark_etl.py"
    )

    extract >> transform