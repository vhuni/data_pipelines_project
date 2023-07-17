def visualize_data():
    import streamlit as st
    import pandas as pd
    import boto3
    
    
    s3 = boto3.client('s3')
    s3_bucket = 'xander-test-c8'
    local_file_path = '/general_data.csv'
    s3.download_file(s3_bucket, 'general_data.csv', local_file_path)

    data = pd.read_csv('general_data.csv')

    st.title('Data Visualization')
    st.write(data)  # Display the data in Streamlit
