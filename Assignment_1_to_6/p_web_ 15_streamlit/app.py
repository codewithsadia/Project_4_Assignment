import streamlit as st # type: ignore
import pandas as pd # type: ignore
import numpy as np # type: ignore

# Set page config
st.set_page_config(page_title="Simple Data Dashboard", layout="wide")

# Title
st.title("Simple Data Dashboard")

# File uploader
st.subheader("Choose a CSV file")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read CSV file
    df = pd.read_csv(uploaded_file)
    
    # Data Preview
    st.subheader("Data Preview")
    st.write(df.head())
    
    # Data Summary
    st.subheader("Data Summary")
    st.write(df.describe())
    
    # Filter Data
    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select value", unique_values)
    
    # Show filtered dataframe
    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)