import os
import pandas as pd
import boto3

def process_csv():
    s3 = boto3.client('s3')
    s3_bucket = 'xander-test-c8'
    # s3_key = 'path/to/your/csv/file.csv'
    local_file_path = '/opt/airflow/include/general_data.csv'
    s3.upload_file(local_file_path, s3_bucket, 'general_data.csv')
    
    # Process the CSV file
    # df = pd.read_csv(local_file_path)
    # # Your data processing logic here
    # processed_data = df.head(10)  # Just an example

    # # Save the processed data
    # processed_data.to_csv('./processed_data.csv', index=False)

process_csv()