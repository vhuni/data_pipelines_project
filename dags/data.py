import os
import pandas as pd
from airflow.hooks.S3_hook import S3Hook

def process_csv():
    s3_hook = S3Hook(aws_conn_id='aws_default')
    s3_bucket = 'your-bucket-name'
    s3_key = 'path/to/your/csv/file.csv'
    local_file_path = '/usr/local/airflow/dags/data/file.csv'
    
    s3_hook.download_file(s3_bucket, s3_key, local_file_path)
    
    # Process the CSV file
    df = pd.read_csv(local_file_path)
    # Your data processing logic here
    processed_data = df.head(10)  # Just an example

    # Save the processed data
    processed_data.to_csv('./processed_data.csv', index=False)
