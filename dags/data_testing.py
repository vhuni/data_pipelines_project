import os
import pandas as pd
import boto3

def process_csv():
    s3 = boto3.client('s3',aws_access_key_id='AKIAVBDSPFQCFFHLKWE5',
    aws_secret_access_key='UT7p/FuouBAhUyja/vZ0mJWQhoLRiz/OBr02ExYE')
    s3_bucket = 'xander-test-c8'
    # s3_key = 'path/to/your/csv/file.csv'
    local_file_path = '/opt/airflow/include/general_data.csv'
    s3.upload_file(local_file_path, s3_bucket, 'general_data.csv')

    local_file_name = '/opt/airflow/include/new_data.csv'
    s3.download_file(s3_bucket, 'general_data.csv', local_file_name)

    print("File successfully tested, uploaded and downloaded")
    # Process the CSV file
    # df = pd.read_csv(local_file_path)
    # # Your data processing logic here
    # processed_data = df.head(10)  # Just an example

    # # Save the processed data
    # processed_data.to_csv('./processed_data.csv', index=False)

process_csv()