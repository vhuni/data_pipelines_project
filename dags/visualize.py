def visualize_data():
    import streamlit as st
    import pandas as pd
    data_path = './general_data.csv'
    data = pd.read_csv(data_path)

    st.title('Data Visualization')
    st.write(data)  # Display the data in Streamlit
