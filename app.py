import streamlit as st
import pandas as pd
import base64

def add_logo():
    logo_image_path = "webapp/ressources/logo.jpeg"

    # Charger le logo en tant que base64
    logo_base64 = base64.b64encode(open(logo_image_path, "rb").read()).decode()

    # Utiliser st.markdown pour afficher le logo centré verticalement
    st.sidebar.markdown(
        f"""
        <div style='display: flex; flex-direction: column; align-items: center; justify-content: center; height: 200px;'>
            <img src='data:image/jpeg;base64,{logo_base64}' alt='Logo' style='width: auto; height: 150px;'/>
        </div>
        """,
        unsafe_allow_html=True,
    )


# Appeler la fonction pour ajouter le logo
add_logo()

# DF
df = pd.read_csv('data/new_Grab_SG_Restaurants.csv', sep=',')

st.title("Restaurant - Singapour :flag-sg:")

df.fillna(' ')
restaurant_title = st.text_input('Nom du restaurant')
st.markdown(" ")

type = st.multiselect(
    "Que voulez-vous manger ? :fork_and_knife:",
    df['type_food_2'].unique())

livraison = st.sidebar.radio("Options de livraison :car:", df['extracted_options'].unique())

st.sidebar.write(" ")

# Définir with_promo au début du script
with_promo = st.sidebar.checkbox("Avec offres promotionnelles", key="promo_checkbox")

st.sidebar.write(" ")

min_rating, max_rating = st.sidebar.slider('**Notes :**', min_value=0.0, max_value=5.0, value=(0.0, 5.0), step=0.1)

st.sidebar.write(" ")
st.sidebar.write("**Meilleures catégories :**")

# pages
acc = st.sidebar.page_link("app.py", label="Tous les restaurants", icon="🏠")
Asia = st.sidebar.page_link("pages/Asia.py", label=":bento: Asiatique")
Boisson = st.sidebar.page_link("pages/Boisson.py", label=":cocktail: Boissons")
Cafe = st.sidebar.page_link("pages/Cafe.py", label=":cake: Café & Dessert")
Fast = st.sidebar.page_link("pages/Fast.py", label=":hamburger: Fast Food")
Halal = st.sidebar.page_link("pages/Halal.py", label=":mosque: Halal")
Healthy = st.sidebar.page_link("pages/Healthy.py", label=":green_salad: Healthy")
World = st.sidebar.page_link("pages/World.py", label=":earth_africa: Monde")

if not type:
    type = df['type_food_2'].unique()

if restaurant_title:
    df = df[df['name'] == restaurant_title]

filtered_df = df[
    (df['type_food_2'].isin(type)) &
    (df['extracted_options'] == livraison) &
    (df['rating'] >= min_rating) &
    (df['rating'] <= max_rating)
]

# Si l'option 'Avec offres promotionnelles' est cochée, filtrer les restaurants ayant des offres promotionnelles
if with_promo:
    filtered_df = filtered_df.dropna(subset=['promo'])

st.write('Propositions :')
for index, row in filtered_df.iterrows():
    restaurant_info = "- **{}** | Options de livraison : {} | Adresse : {} | Coût de livraison : {} | Horaire : {} | Note : {}".format(
        row['name'],
        row['extracted_options'],
        row['address'],
        row['delivery_cost'],
        row['displayedHours'],
        row['rating']
    )
    st.write(restaurant_info)
