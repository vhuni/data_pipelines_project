# from airflow.models.baseoperator import BaseOperator
import streamlit as st
import pandas as pd
import plotly.express as px
import boto3



def visualize_data():    
    s3 = boto3.client('s3', aws_access_key_id='AKIAVBDSPFQCFFHLKWE5',
    aws_secret_access_key='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')
    s3_bucket = 'xander-test-c8'
    local_file_name = 'new_data.csv'
    with open(local_file_name, 'wb') as f:
        s3.download_fileobj(s3_bucket, 'products.csv', f)

    data = pd.read_csv('new_data.csv')

    st.dataframe(data)
    st.title("Testing Streamlit")

    options = ["item","price"]
    selected = st.selectbox("Select an Item", options)
    inform = f"Item {selected} Chart:"
    fig = px.bar(data, x="item", y="price", title=inform)
    st.plotly_chart(fig, use_container_width=True)

    print("Streamlit successful!!!")

visualize_data()




