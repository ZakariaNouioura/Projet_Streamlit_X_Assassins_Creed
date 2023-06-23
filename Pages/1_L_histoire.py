import streamlit as st
import pandas as pd


st.write("Hello!")
url="..\DataFrame\Les_jeux.xlsx"
df=pd.read_excel(url)
st.write(df)