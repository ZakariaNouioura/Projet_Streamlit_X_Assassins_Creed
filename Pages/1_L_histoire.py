import pandas as pd
import io
import requests
import streamlit as st

url = "https://github.com/ZakariaNouioura/Projet_Streamlit_X_Assassins_Creed/raw/main/DataFrame/Les_jeux.xlsx"
response = requests.get(url)
df = pd.read_excel(url)
st.write(df)