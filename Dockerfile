FROM apache/airflow:2.6.2-python3.10

# execute as root
USER root

# Add in the python dependencies that are required from local to current build context 

ADD requirements.txt /opt/airflow/

USER airflow

#RUN chmod -R 777 /opt/ 

RUN pip install --upgrade pip

RUN pip install -r requirements.txt