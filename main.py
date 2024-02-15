import streamlit as st
import pandas as pd

df = pd.read_csv('/Users/nana/Documents/GitHub/Linux/data/Grab_SG_Restaurants.csv', sep=',')

st.title("Restaurant - Singapour :flag-sg:")
type = st.multiselect(
    "Que voulez-vous manger ? :fork_and_knife:",
    df['cuisine'].unique())

names = df[df['cuisine'].isin(type)]['name'].unique()
st.write('Proposition :', names)

st.sidebar.radio("Options de livraison :car:", df['delivery_options'].unique())