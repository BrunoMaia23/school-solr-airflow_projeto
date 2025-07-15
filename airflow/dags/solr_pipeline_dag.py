from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 7, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'solr_pipeline',
    description='Formata CSV e carrega no Solr toda semana',
    schedule_interval='@weekly',
    default_args=default_args,
    catchup=False
) as dag:

    format_task = BashOperator(
        task_id='format_csv',
        bash_command=(
            'python /opt/airflow/scripts/format_csv.py '
            '/opt/airflow/data/alunos.csv '
            '/opt/airflow/data/alunos_clean.csv '
        )
    )

    load_task = BashOperator(
        task_id='load_to_solr',
        bash_command=(
            'python /opt/airflow/scripts/load_to_solr.py '
            'http://solr_instance:8983/solr/alunos_collection '
            '/opt/airflow/data/alunos_clean.csv'
        )
    )

    format_task >> load_task