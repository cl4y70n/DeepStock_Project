
import streamlit as st
import pandas as pd
from src.utils.helpers import plot_series

st.title('DeepStock Dashboard')

uploaded_file = st.file_uploader('Upload CSV', type='csv')
if uploaded_file:
    df = pd.read_csv(uploaded_file, parse_dates=['Date'], index_col='Date')
    st.line_chart(df['Close'])
    plot_series(df)
