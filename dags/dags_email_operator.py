import pendulum
from airflow import DAG
from airflow.operators.email import EmailOperator

with DAG(
    dag_id="dags_email_operator",
    schedule="0 8 1 * *",
    start_date=pendulum.datetime(2024, 5, 17, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    send_email_task = EmailOperator(
        task_id="send_email_task",
        to="jinsolkim719@gmail.com",
        subject="Airflow Test Mail",
        html_content="Mail Test by aijinsol",
    )
