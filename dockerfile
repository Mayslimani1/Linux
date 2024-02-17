# Utilisez une image officielle Python 3.10 comme parent
FROM python:3.10-slim

# Définissez le répertoire de travail dans le conteneur
# WORKDIR /app

# Copiez le fichier des dépendances et installez-les
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copiez le reste de votre code d'application dans le conteneur
COPY . .

# Exposez le port sur lequel votre application s'exécute
EXPOSE 8000

# Commande pour exécuter l'application
CMD ["bash", "-c", "bin/launch.sh", "--server.port=8000", "--server.address=0.0.0.0"]
