import streamlit as st
import pandas as pd

@st.cache
def load_data():
    data = pd.read_csv("http://logopt.com/data/Pokemon.csv")


st.header("Pokemon Attack Lookup")
pokemon_name = st.text_input("Enter a Pokemon name:")

if pokemon_name:
    data_subset = data[data["Name"].str.contains(pokemon_name, case=False)]
    if not data_subset.empty:
        st.write(f"Attack for {pokemon_name}: {data_subset['Attack'].values[0]}")
    else:
        st.write("Pokemon not found.")

if pokemon_name:
    data_subset = data[data["Name"].str.contains(pokemon_name, case=False)]
    if not data_subset.empty:
        st.write(f"Attack for {pokemon_name}: {data_subset['Attack'].values[0]}")
    else:
        st.write("Pokemon not found.")
