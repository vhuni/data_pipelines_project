## Project Brief: Resumption of Study after a Year Out of Higher Education (HE) 2014/15 to 2018/19 in the UK

# Project Brief:
The project will focus on the available data, including the number of students who resume at the same HE institution, the percentage of students who resume at the same institution, the number of students who transfer to other UK HE institutions, the percentage of students who transfer to other institutions, the number of students no longer in HE, the percentage of students no longer in HE, the total number of entrants in the academic year, and the percentage of students not in HE for two years. 

The project aims to provide insights into the resumption patterns and outcomes for students who take a year out of HE.

Data Collection and Analysis:

Obtain data from HESA, the [Higher Education Statistics Agency](https://www.hesa.ac.uk/data-and-analysis/performance-indicators/non-continuation-summary).
Data Preparation: Clean and preprocess the collected data to ensure accuracy and consistency.
Data Analysis: Analyze the collected data to identify trends, patterns, and factors influencing the resumption of study after a year out of HE. 

Conclusion:
This project aims to provide a comprehensive analysis of the resumption of study after a year out of Higher Education in the UK. By examining the available data on resumption rates, transfers, and non-continuation, the project will shed light on the outcomes and pathways for students who take a break from their studies.

# Overview
The goal of this project is to develop a data pipeline using Apache Airflow to automate the process of obtaining, transforming, and visualizing data. The pipeline will consist of four main parts: data acquisition ([web scraping](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)), data transformation (using [pandas](https://pandas.pydata.org/docs/)), data storage (CSV), and data visualization ([Streamlit.io](https://streamlit.io/)). The pipeline will be scheduled to run daily.

* Part 1: Obtaining the Data (Web Scraping)
The consultants will be responsible for implementing web scraping to collect the required data from [Higher Education Statistics Agency](https://www.hesa.ac.uk/data-and-analysis/performance-indicators/non-continuation-summary) using libraries such as BeautifulSoup or Scrapy.

* Part 2: Transforming the Data (Pandas)
Once the data is obtained, the consultants will use pandas to transform and clean the collected data. 

* Part 3: Saving Data to CSV and Uploading to AWS S3
After the data has been transformed it will be saved from pandas DataFrames into CSV files. The consultants will use the AWS SDK (Boto3) to upload the CSV files to an S3 bucket on Amazon Web Services (AWS). 

* Part 4: Reading CSV Data from S3 for Visualization using Streamlit.io
In the final part of the pipeline, the consultants will develop a Streamlit.io web page to visualize the data stored in the CSV files. 

> Consultants should modify and expand the DAG by implementing the web scraping logic, data transformation, and any additional tasks required to complete the project. Each task should be implemented as a separate operator or Python function and connected using appropriate dependencies to form the complete data pipeline.

> The Project is divided into 4 parts so consultants can divide the work as a team and make use of [GitHub](https://github.com/) to commit changes and pull requests to merge the project in one branch.

# Airflow Data Pipeline
To automate and orchestrate the entire process, the data engineers will use [Apache Airflow](https://airflow.apache.org/), an open-source platform for creating, scheduling, and monitoring workflows. The provided code demonstrates a basic Airflow DAG (Directed Acyclic Graph) with tasks representing the different parts of the data pipeline.

- the DAG starts with the task "process_csv" that calls the process_csv function
- responsible for saving the data to a local CSV file and uploading it to the specified S3 bucket. 
- the task "visualize_data" calls the visualize_data function, responsible for reading the CSV data from the S3 bucket and creating visualizations using Streamlit.io.
- the DAG is scheduled to run daily (schedule_interval="@daily") and has the catchup=False parameter to avoid backfilling missed runs.

#### Please note that the provided code includes commented-out sections that can be used as a reference for implementing the missing functionality related to training models and choosing the best model based on accuracy. Feel free to uncomment and adapt these sections if they are relevant to your project.

###### For any questions or assistance during the development process, please refer to the Airflow documentation, pandas documentation, AWS SDK (Boto3) documentation, and Streamlit.io documentation, or consult with the stakeholders.

# Project Structure

### Description

### Description

- **dags**: This directory contains all the Apache Airflow DAG files. Airflow DAGs define the workflows and tasks for data processing, ETL (Extract, Transform, Load) operations, and other data-related processes.

- **dags/my_dag.py**: Example Apache Airflow DAG file. You can add more DAG files as needed for different workflows.

- **dags/another_dag.py**: Another example Apache Airflow DAG file.

- **streamlit_app**: This directory contains the Streamlit.io web application.

- **streamlit_app/data**: This sub-directory stores the data files required for the Streamlit.io application.

- **streamlit_app/src**: Contains the source code for the Streamlit.io web application.

- **streamlit_app/src/my_streamlit_app.py**: The main Streamlit.io application file where you define the interactive data visualization and analysis.

- **streamlit_app/src/utils.py**: Utility functions that might be used in the Streamlit.io app.

- **streamlit_app/Dockerfile**: Docker configuration file for building the Streamlit.io application image.

- **streamlit_app/requirements.txt**: Lists the dependencies required to run the Streamlit.io application.

- **airflow**: This directory contains the Apache Airflow configuration.

- **airflow/dags**: This sub-directory stores the Apache Airflow DAG files.

- **airflow/Dockerfile**: Docker configuration file for building the Apache Airflow image.

- **docker-compose.yml**: Docker Compose file for orchestrating the Airflow and Streamlit services.

- **README.md**: The main project readme file that contains the description and overview of the entire project.

## Getting Started

1. Clone the repository to your local machine:

```bash
git clone https://github.com/your_username/airflow-dags-and-streamlit.git
cd airflow-dags-and-streamlit
```

2. Set up Apache Airflow and create the DAGs by copying the DAG files from the dags directory to your Airflow DAGs directory.


3. Set up the Streamlit.io application:

a. Navigate to the streamlit_app directory:
```bash
cd airflow
docker build -t my_airflow_image .```
