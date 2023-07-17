from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
# from data import process_csv
from streamlit_app import visualize_data

from random import randint
from datetime import datetime
import boto3


def process_csv():
    s3 = boto3.client('s3')
    s3_bucket = 'xander-test-c8'
    # s3_key = 'path/to/your/csv/file.csv'
    local_file_path = '/opt/airflow/include/general_data.csv'
    s3.upload_file(local_file_path, s3_bucket, 'general_data.csv')

# def _choose_best_model(ti):
#     accuracies = ti.xcom_pull(task_ids=[
#         'training_model_A',
#         'training_model_B',
#         'training_model_C'
#     ])
#     best_accuracy = max(accuracies)
#     if (best_accuracy > 5):
#         return 'accurate'
#     return 'inaccurate'


# def _training_model():
#     return randint(1, 10)

with DAG("my_dag", start_date=datetime(2021, 1, 1),
    schedule_interval="@daily", catchup=False) as dag:

        # training_model_A = PythonOperator(
        #     task_id="training_model_A",
        #     python_callable=_training_model
        # )

        # training_model_B = PythonOperator(
        #     task_id="training_model_B",
        #     python_callable=_training_model
        # )

        # training_model_C = PythonOperator(
        #     task_id="training_model_C",
        #     python_callable=_training_model
        # )

        # choose_best_model = BranchPythonOperator(
        #     task_id="choose_best_model",
        #     python_callable=_choose_best_model
        # )

        # accurate = BashOperator(
        #     task_id="accurate",
        #     bash_command="echo 'accurate'"
        # )

        # inaccurate = BashOperator(
        #     task_id="inaccurate",
        #     bash_command="echo 'inaccurate'"
        # )
        process_csv_task = PythonOperator(
            task_id='process_csv',
            python_callable=process_csv,
        )

        visualize_data_task = PythonOperator(
            task_id='visualize_data',
            python_callable=visualize_data,
        )

        process_csv_task >> visualize_data_task

        # [training_model_A, training_model_B, training_model_C] >> choose_best_model >> [accurate, inaccurate]