from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator

from bs4 import BeautifulSoup
import requests
import csv
import sys

sys.path.append("./include")
from streamlitapp import visualize_data

from datetime import datetime
import boto3

'''
    # The function process_csv uploads the 'products.csv' from web_scraping_b4 function to Amazon S3 bucket.
    # Simply add this to the DAG as a PythonOperator and schedule it after web scraping data.

def process_csv():
    s3 = boto3.client('s3',aws_access_key_id='ssss',
    aws_secret_access_key='ssss')
    s3_bucket = 'xander-test-c8'
    # s3_key = 'path/to/your/csv/file.csv'
    local_file_path = '/opt/airflow/include/products.csv'
    s3.upload_file(local_file_path, s3_bucket, 'products.csv')


    # The function web_scraping_b4 below is an example of a bs4 web scraping script. You can use this as a reference in making you webscraping
    # function. Simply add this to the DAG as a PythonOperator and schedule it before the processing of the csv if needed.  

def web_scraping_b4():
    URL = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
    r = requests.get(URL)

    html_content = r.text

    soup = BeautifulSoup(html_content, 'html.parser')

    product_list = [] # a list to store products
   
    table = soup.find('div', attrs = {'class':'col-md-9'}) 
    table_new = table.find('div', attrs = {'class':"row"})
    rows = table_new.find_all('div', attrs = {'class':"caption"})

    # print(rows)

    # print("-------------------------------------")
    filename = 'products.csv'
    with open(filename, 'w', newline='') as f:
        w = csv.DictWriter(f,['item','price'])
        w.writeheader()
        for row in rows:
            products={}  
            products['item'] = row.a['title']
            # print(item)
            products['price'] = row.find('h4', class_ = 'pull-right price').text 
            # print(price)
            product_list.append(products)
            w.writerow(products)
'''

with DAG("my_dag", start_date=datetime(2021, 1, 1),
    schedule_interval="@daily", catchup=False) as dag:
    
        webscrape_data_task = PythonOperator(
            task_id='web_scrape_data',
            python_callable=web_scraping_b4
        )

        process_csv_task = PythonOperator(
            task_id='process_csv',
            python_callable=process_csv
        )

        visualize_data_task = PythonOperator(
            task_id='visualize_data',
            python_callable=visualize_data
        )

        webscrape_data_task >> process_csv_task >> visualize_data_task

