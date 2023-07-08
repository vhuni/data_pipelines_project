FROM apache/airflow:2.5.0-python3.10

# execute as root
USER root

# install the required drivers for msodbcsql17
# RUN apt-get update \
#   &&  apt-get install -y apt-transport-https ca-certificates \
#   && curl --proxy-insecure https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
#   && curl --proxy-insecure https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list \
#   && apt-get update \
#   && ACCEPT_EULA=Y apt-get install -y msodbcsql17 \
#   && ACCEPT_EULA=Y apt-get install -y mssql-tools 


# # install additional required libs for sql drivers
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     g++ \
#     unixodbc-dev \
#     unixodbc \
#     libpq-dev \
#     wget 

# RUN apt-get update \
#   && apt-get install -y --no-install-recommends \
#          openjdk-11-jre-headless \
#   && apt-get autoremove -yqq --purge \
#   && apt-get clean \
#   && rm -rf /var/lib/apt/lists/*

# ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

# # Install Spark
# ENV SPARK_VERSION=3.2.0 \
#     HADOOP_VERSION=3.2 \
#     SPARK_HOME=/opt/spark \
#     PYTHONHASHSEED=1

# # Download and uncompress spark from the apache archive
# RUN wget --no-verbose -O apache-spark.tgz "https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" --no-check-certificate\
#     && mkdir -p /opt/spark \
#     && tar -xf apache-spark.tgz -C /opt/spark --strip-components=1 \
#     && rm apache-spark.tgz

# Add in the python dependencies that are required from local to current build context 

# ADD requirements.txt /opt/airflow/
# ADD openssl.cnf /etc/ssl/

USER airflow

#RUN chmod -R 777 /opt/ 

# RUN pip install --no-cache-dir apache-airflow-providers-apache-spark==2.1.3

RUN pip install --upgrade pip

# RUN pip install -r requirements.txt