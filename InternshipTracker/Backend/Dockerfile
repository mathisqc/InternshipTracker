# backend/Dockerfile
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les dépendances et les installer
COPY ../fastapi/requirements.txt .
RUN pip install -r requirements.txt
RUN pip install psycopg2-binary

# Copier tout le contenu du backend
COPY . .

# Exécuter `creerdb.py` avant de démarrer l'application principale
RUN python CreerDB.py

# Lancer l'application FastAPI
CMD ["python", "app.py"]
