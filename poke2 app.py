import streamlit as st
import pandas as pd

@st.cache
def load_data():
    url = "http://logopt.com/data/Pokemon.csv"
    data = pd.read_csv(url)
    return data

data = load_data()

st.write("Enter the name of a Pokemon:")
name = st.text_input()

if name: