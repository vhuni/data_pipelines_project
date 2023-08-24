from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator

from bs4 import BeautifulSoup
import requests
import csv

# from data import process_csv
import sys

sys.path.append("./include")
from streamlitapp import visualize_data

# from random import randint
from datetime import datetime
import boto3


def process_csv():
    s3 = boto3.client('s3',aws_access_key_id='ssss',
    aws_secret_access_key='ssss')
    s3_bucket = 'xander-test-c8'
    # s3_key = 'path/to/your/csv/file.csv'
    local_file_path = '/opt/airflow/include/general_data.csv'
    s3.upload_file(local_file_path, s3_bucket, 'general_data.csv')

def web_scraping_b4():
    URL = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')

    products=[]  # a list to store quotes
   
    table = soup.find('div', attrs = {'class':'row'}) 
   
    for row in table.findAll('div', 
                             attrs = {"class":"col-sm-4 col-lg-4 col-md-4"}):
        cols = row.find_all('thumbnail')
        item = cols.text
        price = row.a['href']
        description = row.img['src']
        rating = row.img['alt'].split(" #")[0]
        products.append([item,price,description,rating])
   
filename = 'inspirational_quotes.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['theme','url','img','lines','author'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)

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

