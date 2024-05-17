import pendulum
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_select_fruit",
    schedule="10 0 * * 6#1",
    start_date=pendulum.datetime(2024, 5, 17, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    t1_orange = BashOperator(
        task_id="t1_orange",
        bash_command="/opt/airflow/plugins/shells/select_fruit.sh ORANGE",
    )

    t1_avocado = BashOperator(
        task_id="t1_avocado",
        bash_command="/opt/airflow/plugins/shells/select_fruit.sh AVOCADO",
    )

    t1_orange >> t1_avocado
