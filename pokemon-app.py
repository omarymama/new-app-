import streamlit as st
import pandas as pd

# データセットの読み込み
data = pd.read_csv("pokemon.csv")

# アプリケーションのタイトル
st.title("Pokemon Info App")

# ユーザーが入力するためのテキストボックス
pokemon_name = st.text_input("Enter Pokemon name:")

# Pokemonの名前が入力された場合、そのPokemonの詳細情報を表示
if pokemon_name:
    st.write("You selected:", pokemon_name)
    selected_pokemon = data[data['name'] == pokemon_name]
    st.write(selected_pokemon)