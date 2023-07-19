FROM apache/airflow:2.6.2-python3.10

# execute as root
USER root

# Add in the python dependencies that are required from local to current build context 
RUN apt-get update && apt-get install -y --no-install-recommends \
    g++ \
    unixodbc-dev \
    unixodbc \
    libpq-dev \
    wget 

RUN apt-get update \
  && apt-get install
  
ADD requirements.txt /opt/airflow/

USER airflow

#RUN chmod -R 777 /opt/ 

RUN pip install --upgrade pip

RUN pip install -r requirements.txt