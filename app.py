import streamlit as st
import pandas as pd
import numpy as np

## Title of the app
st.title("Hello Streamlit!")
st.write("This is my first Streamlit app.")

## create a simple DataFrame
data = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

## display the DataFrame
st.write("Here is a  DataFrame:")
st.write(data)

## Simple line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3), columns=['a', 'b', 'c']
)

st.line_chart(chart_data)