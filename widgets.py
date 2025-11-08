import streamlit as st
import pandas as pd
import numpy as np

st.title("Streamlit Text Input Widget Example")

name = st.text_input("Enter your name:", "Type here...")

age = st.slider("Enter your age:", min_value=0, max_value=120, value=25)

st.write(f"Hello, {name}! You are {age} years old.")

options = ['Option 1', 'Option 2', 'Option 3']
choice = st.selectbox("Choose an option:", options)
st.write(f"You selected: {choice}")

if name:
    st.success(f"Welcome, {name}!")


data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Score': [85, 90, 95]}
df = pd.DataFrame(data)
st.write("Here is the DataFrame:")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    user_df = pd.read_csv(uploaded_file)
    st.write(user_df)