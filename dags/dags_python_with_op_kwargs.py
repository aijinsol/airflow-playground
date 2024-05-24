import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator
from common.common_func import register2

with DAG(
    dag_id="dags_python_with_op_kwargs",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2024, 5, 20, tz="Asia/Seoul"),
    catchup=False,
) as dag:

    register2_t1 = PythonOperator(
        task_id="register2_t1",
        python_callable=register2,
        op_args=["aijinsol", "female", "kr", "seoul"],
        op_kwargs={"email": "jinsolkim719@gmail.com", "phone": "010", "etc": "others"}
    )

    register2_t1
