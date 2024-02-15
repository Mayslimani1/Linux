import streamlit as st
import pandas as pd
import base64

# background_image = "/Users/maysaslimani/Documents/GitHub/Linux/image_fond.png"

# st.markdown(
#     f"""
#     <style>
#     .reportview-container {{
#         background: url(data:image/jpeg;base64,{base64.b64encode(open(background_image, "rb").read()).decode()})
#     }}
#     </style>
#     """,
#     unsafe_allow_html=True
# )
# st.markdown(background_image, unsafe_allow_html=True)

#DF
df = pd.read_csv('/Users/nana/Documents/GitHub/Linux/data/nouvelle_base_linux.csv', sep=',')


restaurant_title = st.text_input('Nom du restaurant')

df.fillna(' ')
st.title("Restaurant - Singapour :flag-sg:")
type = st.multiselect(
    "Que voulez-vous manger ? :fork_and_knife:",
    df['type_food_2'].unique())

livraison = st.sidebar.radio("Options de livraison :car:", df['extracted_options'].unique())

st.sidebar.write(" ")

with_promo = st.sidebar.checkbox("Avec offres promotionnelles")

st.sidebar.write(" ")

min_rating, max_rating = st.sidebar.slider('**Notes :**', min_value=0.0, max_value=5.0, value=(0.0, 5.0), step=0.1)

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
    restaurant_info = "- **{}** |  Options de livraison : {} | Adresse : {} | Coût de livraison : {} | Note : {}".format(
        row['name'],
        row['extracted_options'],
        row['address'],
        row['delivery_cost'],
        row['rating']
    )
    st.write(restaurant_info)