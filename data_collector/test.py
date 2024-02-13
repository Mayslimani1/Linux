from datetime import datetime

# Date de naissance avec heure
date_naissance = datetime(1998, 2, 13, 21, 3)

# Date future à laquelle vous souhaitez connaître votre âge
date_future = datetime(2024, 2, 13, 1, 30)

# Calcul de l'âge en prenant en compte l'heure de naissance
if date_future < datetime(date_future.year, date_naissance.month, date_naissance.day, date_naissance.hour, date_naissance.minute):
    age = date_future.year - date_naissance.year - 1
else:
    age = date_future.year - date_naissance.year

# Affichage de l'âge
print("Vous aurez {} ans le {} à {}.".format(age, date_future.strftime("%d/%m/%Y"), date_future.strftime("%H:%M")))
