import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator
from common.common_func import register

with DAG(
    dag_id="dags_python_with_op_args",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2024, 5, 20, tz="Asia/Seoul"),
    catchup=False,
) as dag:

    register_t1 = PythonOperator(
        task_id="register_t1",
        python_callable=register,
        op_args=["aijinsol", "female", "kr", "seoul"],
    )

    register_t1
