# Utilisez une image de base légère avec Python
FROM python:3.8-slim

# Définissez le répertoire de travail
WORKDIR /app

# Copiez le contenu actuel dans le répertoire de travail
COPY . /app

# Installez les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposez le port que Flask utilisera
EXPOSE 5000

# Commande pour démarrer l'application Flask
CMD ["python", "app.py"]
