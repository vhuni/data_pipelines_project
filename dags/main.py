from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
# from data import process_csv
import sys

sys.path.append("./include")
from streamlitapp import visualize_data

# from random import randint
from datetime import datetime
import boto3


def process_csv():
    s3 = boto3.client('s3',aws_access_key_id='AKIAVBDSPFQCFFHLKWE5',
    aws_secret_access_key='UT7p/FuouBAhUyja/vZ0mJWQhoLRiz/OBr02ExYE')
    s3_bucket = 'xander-test-c8'
    # s3_key = 'path/to/your/csv/file.csv'
    local_file_path = '/opt/airflow/include/general_data.csv'
    s3.upload_file(local_file_path, s3_bucket, 'general_data.csv')


with DAG("my_dag", start_date=datetime(2021, 1, 1),
    schedule_interval="@daily", catchup=False) as dag:

        process_csv_task = PythonOperator(
            task_id='process_csv',
            python_callable=process_csv
        )

        visualize_data_task = PythonOperator(
            task_id='visualize_data',
            python_callable=visualize_data
        )
        # run_this = BashOperator(
        #     task_id="run_streamlit",
        #     bash_command="streamlit run --server.enableWebsocketCompression=false --server.enableCORS=false --server.enableXsrfProtection=false /opt/airflow/include/streamlitapp.py",
        # )

        process_csv_task >> visualize_data_task

