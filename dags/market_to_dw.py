from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import logging

def extract():
    logging.info("Extract placeholder: fetch latest market snapshots")

def transform():
    logging.info("Transform placeholder: normalize records")

def load():
    logging.info("Load placeholder: insert into DW")

default_args = {
    'owner': 'exvo',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='exvo_market_to_dw',
    default_args=default_args,
    start_date=datetime(2025, 1, 1),
    schedule_interval='@hourly',
    catchup=False
) as dag:
    t1 = PythonOperator(task_id='extract', python_callable=extract)
    t2 = PythonOperator(task_id='transform', python_callable=transform)
    t3 = PythonOperator(task_id='load', python_callable=load)

    t1 >> t2 >> t3
