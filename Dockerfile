FROM python:3

WORKDIR /usr/src/app

COPY Projet.py .
COPY templates templates
COPY requirements.txt .

run pip install --no-cache-dir -r requirements.txt

ENTRYPOINT python Projet.py
