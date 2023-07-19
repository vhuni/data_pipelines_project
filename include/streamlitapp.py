# from airflow.models.baseoperator import BaseOperator
import streamlit as st
import pandas as pd
import plotly.express as px
import boto3
import sys
from streamlit.web import cli as stcli


def visualize_data():    
    s3 = boto3.client('s3', aws_access_key_id='sss',
    aws_secret_access_key='sssss')
    s3_bucket = 'xander-test-c8'
    local_file_name = 'new_data.csv'
    with open(local_file_name, 'wb') as f:
        s3.download_fileobj(s3_bucket, 'general_data.csv', f)

    data = pd.read_csv('new_data.csv')

    st.dataframe(data)
    st.title("Testing Streamlit")

    options = ["MonthlyIncome","TotalWorkingYears","JobRole"]
    selected = st.selectbox("Select an Employee data value", options)
    inform = f"Employees {selected} Chart:"
    fig = px.line(data, x="Age", y=selected, title=inform)
    st.plotly_chart(fig, use_container_width=True)

    print("Streamlit successful!!!")

    sys.argv = ["streamlit", "run", "streamlitapp.py","--server.port=8501", "--server.address=0.0.0.0", "--server.enableWebsocketCompression=false" ,"--server.enableCORS=false", "--server.enableXsrfProtection=false"]
    sys.exit(stcli.main())

visualize_data()




