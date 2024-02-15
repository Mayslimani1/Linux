import streamlit as st
import pandas as pd

df_fast_food = pd.read_csv('/Users/nana/Documents/GitHub/Linux/data/df_fast_food.csv', sep=',')

st.title("Porn Food :hamburger:")
type = st.multiselect(
    "Qu'est-ce qu'il vous ferait plaisir ? :yum:",
    df_fast_food['type_food_2'].unique())
livraison = st.sidebar.radio("Options de livraison :car:", df_fast_food['extracted_options'].unique())

with_promo = st.sidebar.checkbox("Avec offres promotionnelles")

st.sidebar.write(" ")
st.sidebar.write("**Meilleures catégories :**")

#pages
acc = st.sidebar.page_link("main.py", label="Tous les restaurants", icon="🏠")
Asia = st.sidebar.page_link("pages/Asia.py", label=":bento: Asiatique")
Boisson = st.sidebar.page_link("pages/Boisson.py", label=":cocktail: Boissons")
Cafe = st.sidebar.page_link("pages/Cafe.py", label=":cake: Café & Dessert")
Fast = st.sidebar.page_link("pages/Fast.py", label=":hamburger: Fast Food")
Halal = st.sidebar.page_link("pages/Halal.py", label=":mosque: Halal")
Healthy = st.sidebar.page_link("pages/Healthy.py", label=":green_salad: Healthy")
World = st.sidebar.page_link("pages/World.py", label=":earth_africa: Monde")

if not type:
    type = df_fast_food['type_food_2'].unique()
    
filtered_df = df_fast_food[
    (df_fast_food['type_food_2'].isin(type)) &
    (df_fast_food['extracted_options'] == livraison)
]

# Si l'option 'Avec offres promotionnelles' est cochée, filtrer les restaurants ayant des offres promotionnelles
if with_promo:
    filtered_df = filtered_df.dropna(subset=['promo'])

st.write('Propositions :')
for index, row in filtered_df.iterrows():
    restaurant_info = "- **{}** |  Options de livraison : {} | Adresse : {} | Coût de livraison : {} | Note : {}".format(
        row['name'],
        row['extracted_options'],
        row['address'],
        row['delivery_cost'],
        row['rating']
    )
    st.write(restaurant_info)