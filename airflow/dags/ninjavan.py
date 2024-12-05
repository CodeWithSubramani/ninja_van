from datetime import datetime
from datetime import timedelta

from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

from airflow import DAG
from helper_functions import test_process_events

now = datetime.now()
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(now.year, now.month, now.day),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1)
}
dag = DAG(
    dag_id="ninja_van_micro_batch",
    description="Example of micro batching",
    default_args=default_args,
    schedule_interval="* * * * *",
    catchup=False
)

get_data = PythonOperator(
    task_id='get_data',
    python_callable=test_process_events,
    dag=dag)

start = DummyOperator(task_id="start", dag=dag)

start >> get_data
