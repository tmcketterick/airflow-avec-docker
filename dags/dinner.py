import datetime as dt

from airflow import DAG
from airflow.operators.python import PythonOperator

from have_dinner import starter, main, dessert

base_dir = '/'
default_args = {
    'owner': 'tmcketterick',
    'depends_on_past': False,
    'start_date': dt.datetime.strptime('2017-04-17T00:00:00', '%Y-%m-%dT%H:%M:%S'),
    'provide_context': True
}
dag = DAG(
    dag_id='TOMS-DINNER',
    default_args=default_args,
    schedule_interval='0 0 * * 2',
    max_active_runs=1,
)

starter_task = PythonOperator(
    task_id='STARTER',
    python_callable=starter,
    op_kwargs={'base_dir': base_dir},
    dag=dag,
)
main_task = PythonOperator(
    task_id='MAIN',
    python_callable=main,
    op_kwargs={'base_dir': base_dir},
    dag=dag,
)
dessert_task = PythonOperator(
    task_id='DESSERT',
    python_callable=dessert,
    op_kwargs={'base_dir': base_dir},
    dag=dag,
)


starter_task >> main_task
main_task >> dessert_task
