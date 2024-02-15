import streamlit as st
import pandas as pd

file = st.file_uploader("Upload file")
if file is not None:
    df = pd.read_csv(file, encoding='utf-8')
    st.dataframe(df.describe())
    
    
# 1:20:00 - Continue    