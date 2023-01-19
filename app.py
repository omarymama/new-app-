import streamlit as st
import pandas as pd

@st.cache
def load_data():
    data = pd.read_csv("http://logopt.com/data/Pokemon.csv")
    return data


st.title("Pokemon Attack Lookup")

name = st.text_input("Enter Pokemon name:")

if name:
    attack = data[data["Name"] == name]["Attack"]
    st.write(f"Attack of {name} is {attack}")
