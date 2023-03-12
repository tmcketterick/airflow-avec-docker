import datetime as dt

from airflow import DAG
from airflow.operators.python import PythonOperator

from have_breakfast import cereal, juice

base_dir = '/'
default_args = {
    'owner': 'tmcketterick',
    'depends_on_past': False,
    'start_date': dt.datetime.strptime('2017-04-17T00:00:00', '%Y-%m-%dT%H:%M:%S'),
    'provide_context': True
}
dag = DAG(
    dag_id='TOMS-BREAKFAST',
    default_args=default_args,
    schedule_interval='0 0 * * 2',
    max_active_runs=1,
)

cereal_task = PythonOperator(
    task_id='CEREAL',
    python_callable=cereal,
    op_kwargs={'base_dir': base_dir},
    dag=dag,
)
juice_task = PythonOperator(
    task_id='JUICE',
    python_callable=juice,
    op_kwargs={'base_dir': base_dir},
    dag=dag,
)


cereal_task >> juice_task