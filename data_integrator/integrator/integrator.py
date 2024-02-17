import pandas as pd
import numpy as np
import json
import warnings
warnings.filterwarnings("ignore")
import os

df = pd.read_csv('data/Grab_SG_Restaurants.csv')

### Traitement de la base de donénes : 
# Créer des variables pour les horaires d'ouvertures/fermetures :
df['opening_hours'] = df['opening_hours'].apply(json.loads)

# Ajouter des colonnes pour chaque jour de la semaine avec les horaires correspondants
df = pd.concat([df.drop(['opening_hours'], axis=1), df['opening_hours'].apply(pd.Series)], axis=1)
df['cuisine'] = df['cuisine'].apply(lambda x: json.loads(x) if pd.notnull(x) and x != '[]' else [])
df = pd.concat([df.drop(['cuisine'], axis=1), df['cuisine'].apply(pd.Series)], axis=1)
# Renommer les colonnes si nécessaire
df.rename(columns={0 : "type_food_0", 1: 'type_food_1', 2: 'type_food_2', 3: 'type_food_3', 4 : "type_food_4"}, inplace=True)
df[["type_food_1", "type_food_2", "type_food_3", "type_food_4"]].fillna(0, inplace=True)
#drop quand on a aps le nom du restaurant : 
df.dropna(axis=0,subset=['name'],inplace=True)
df.reset_index(drop=True,inplace=True)

#mettre others si pas de variable dans type food :
df[["type_food_0","type_food_1","type_food_2","type_food_3","type_food_4"]].fillna(0,inplace=True)

df.fillna('', inplace=True)
### Recommandation 
# Récupérer les delivery_options:
df['extracted_options'] = df['delivery_options'].str.extract(r'_(.*)')
df['extracted_options'] =df['extracted_options'].str.lower()
df['extracted_options'] = df['extracted_options'].replace({
    'delivery': 'Livraison uniquement',
    'takeaway': 'Livraison et à emporter',
    'dinein': 'Livraison et sur place',
    'takeaway_dinein': 'Livraison à emporter et sur place'
})
# Liste des modalités à supprimer
modalites_a_supprimer = [
    'Kids Friendly', 'Catering', 'MICHELIN Bib Gourmand', 'MICHELIN Plate', 'MICHELIN Stars', 
    'Social Enterprises', 'Specialties', 'Gifts', 'Hainanese Chicken Rice', "Valentine's Day Specials", 
    'Mom & Kids', 'Assorted Hotpot', 'Options de livraison', 'Islandwide Delivery', 'Takeaway', 
    'Delivery', 'Delivery & Takeaway', 'Dine-in', 'Options de repas', 'Breakfast & Brunch', 'Lunch', 
    'Dinner', 'Quick Bites', 'Produits', 'Same Prices In-Store', 'Convenience Store/Minimart', 
    'Fresh Produce', 'Frozen Food', 'Fresh & Frozen', 'Fresh Market', 'Fresh Products', 'Ready To Eat', 
    'Household Goods', 'Health', 'Medical Supplies & Equipments', 'Household Essentials', 'Party Supplies', "2 MICHELIN Stars",
    "'Gift Shops",'Convenience Store', '1 MICHELIN Star', 'Muslim', "Face & Body Care",'Beauty',"Eco-Friendly",
    'Maternity', 'Home & Hardware', 'Books & Office Supplies', "Toys & Gaming",  'Home and Hardware','Health & Wellness', 'Grocery', 'Izakaya',
    'Flowers','Convenience','Health & Beauty',
       'Pet Care','Home & Living',  'Fashion Accessories', 'Bookstore & Office Supplies', 'Coconut','Beauty & Personal Care', 'Pharmacy/Health',
'Gift & Party Shop', 'Baked Goods', 'Cosmetics', 'North Indian','Toys','','Mala Xiang Guo',
'Southern', 'Hampers', 'Pad Thai',  'Fresh Seafood',
       'Filipino', 'Pho', 'Herbal drink', 'Wings'
]

# Supprimer les modalités de la colonne type_food_2
df = df[~df['type_food_2'].isin(modalites_a_supprimer)]
df['delivery_cost'] = pd.to_numeric(df['delivery_cost'], errors='coerce')
df['delivery_cost'] = df['delivery_cost'] / 100

# ASIAT
df_asiat = df[df['type_food_2'].isin(['Chinese', 'Japanese', 'Thai', 'Korean', 'Vietnamese', 'Asian', 'Malaysian', 'Indonesian',
 'Peranakan', 'Singaporean', 'Taiwanese', "Korean Fried Chicken", 'Rice noodles','Dumplings','Kimbap','Sushi', 'Rice dishes'
 , 'Wok', 'Tofu', 'Curry', 'Satay'])]

# Halal
df_halal = df[df['type_food_2'].isin(['Halal', "Halal Food"])]

# Restaurant du monde
df_restaurant_monde = df[df['type_food_2'].isin(['Dessert', 'Ice Cream', 'Cake', 'Pastries', 'Chocolate', 'Cupcakes', 'Cream puff', 
             'Ice Cream & Iced Dessert', 'Dumplings', 'Coffee & Tea', 'Bubble Tea', 'Cold Brew', 
             'Coffee', 'Milk Tea', 'Bakery & Cake', 'Roasted Coffee Beans', 'Boba Tea'])]

# Fast Food
df_fast_food = df[df['type_food_2'].isin(["Fast Food", "Burger", "BBQ", "Fried Chicken", "Burgers", "Pizza", 
                       "Finger Food", "Kebabs", "Tacos"])]

# Café / Dessert
df_cafe_dessert = df[df['type_food_2'].isin(['Coffee & Tea', 'Dessert', 'Ice Cream', 'Cake', 'Bakery', 'Chocolate', 'Pastries', 'Bubble Tea', 'Cupcakes', 'Cream puff', 'Juice', 'Cold Brew', 'Milk Tea'])]

# Boisson
df_boisson = df[df['type_food_2'].isin(["Coffee & Tea", "Beverages", "Mart", "Snack", "Bubble Tea", "Tea", "Juice", 
                      "Drinks", "Cold Brew", "Coffee", "Milk Tea", "Juice & Smoothies", "Smoothies", 
                      "Beer", "Wine", "Juice/Smoothies"])]

# Végétarien
df_Healthy = df[df['type_food_2'].isin(['Vegetarian', 'Vegan', 'Salad', 'Healthy', 'Vegetarian Friendly'])]


# Exporter df_asiat en CSV
df_asiat.to_csv('data/df_asiat.csv', index=False)

# Exporter df_halal en CSV
df_halal.to_csv('data/df_halal.csv', index=False)

# Exporter df_restaurant_monde en CSV
df_restaurant_monde.to_csv('data/df_restaurant_monde.csv', index=False)

# Exporter df_fast_food en CSV
df_fast_food.to_csv('data/df_fast_food.csv', index=False)

# Exporter df_cafe_dessert en CSV
df_cafe_dessert.to_csv('data/df_cafe_dessert.csv', index=False)

# Exporter df_boisson en CSV
df_boisson.to_csv('data/df_boisson.csv', index=False)

# Exporter df_Healthy en CSV
df_Healthy.to_csv('data/df_Healthy.csv', index=False)

df.to_csv('data/new_Grab_SG_Restaurants.csv', index=False)
