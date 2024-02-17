# Utilisez une image officielle Python 3.10 comme parent
FROM ubuntu:20.04

# Copiez le fichier des dépendances et installez-les
RUN apt update && \
    apt-get install -y curl python3 python3-pip unzip && \
    python3 -m pip install virtualenv

RUN mkdir -p /Linux
WORKDIR /Linux

# Copiez le reste de votre code d'application dans le conteneur
COPY . .

RUN bash install.sh

# Commande pour exécuter l'application
CMD ["bash", "launch.sh"]
