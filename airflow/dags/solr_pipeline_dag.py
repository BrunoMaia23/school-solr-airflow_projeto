import sys
from datetime import datetime, timedelta

# Injeta a pasta de scripts no path do Python
sys.path.insert(0, '/opt/airflow/scripts')

from format_csv import format_csv
from load_to_solr import load_to_solr

from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 7, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='solr_pipeline',
    description='Formata CSV e carrega no Solr toda semana',
    schedule_interval='@weekly',
    default_args=default_args,
    catchup=False,
) as dag:

    format_task = PythonOperator(
        task_id='format_csv',
        python_callable=format_csv,
        op_kwargs={
            'input_path': '/opt/airflow/data/alunos.csv',
            'output_path': '/opt/airflow/data/alunos_clean.csv',
        },
    )

    load_task = PythonOperator(
        task_id='load_to_solr',
        python_callable=load_to_solr,
        op_kwargs={
            'solr_url': 'http://solr_instance:8983/solr/alunos_collection',
            'csv_path': '/opt/airflow/data/alunos_clean.csv',
        },
    )

    format_task >> load_task
