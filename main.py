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


restaurant_title = st.text_input('Nom du restaurant', 'Nom du restaurant par défaut')
st.write('Le nom du restaurant actuel est', restaurant_title)


df.fillna(' ')
st.title("Restaurant - Singapour :flag-sg:")
type = st.multiselect(
    "Que voulez-vous manger ? :fork_and_knife:",
    df['type_food_2'].unique())
livraison = st.sidebar.radio("Options de livraison :car:", df['extracted_options'].unique())

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
Vegan = st.sidebar.page_link("pages/Vegan.py", label=":stuffed_flatbread: Végétarien")
World = st.sidebar.page_link("pages/World.py", label=":earth_africa: Monde")

names = df[df['type_food_2'].isin(type)]['name'].unique()
names = df[df['extracted_options'].isin([livraison])]['name'].unique()

if with_promo:
    names = df.dropna(subset=['promo'])

st.write('Propositions :')
for name in names:
    if name in df['name'].unique(): 
        restaurant_data = df[df['name'] == name].iloc[0] 
        restaurant_info = "- **{}** |  Options de livraison : {} | Adresse : {} | Coût de livraison : {} | Note : {}".format(
            name,
            restaurant_data['extracted_options'],
            restaurant_data['address'],
            restaurant_data['delivery_cost'],
            restaurant_data['rating'])
        st.write(restaurant_info)