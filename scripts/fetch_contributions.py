import requests
from bs4 import BeautifulSoup
import json
import os

url = "https://github.com/users/LankyGG/contributions"
print(f"Récupération de {url}...")

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

days = []
# GitHub utilise cette classe pour les cases de la grille de contribution
for td in soup.find_all('td', class_='ContributionCalendar-day'):
    date = td.get('data-date')
    level = td.get('data-level')
    if date and level:
        days.append({"date": date, "level": int(level)})

# S'assure que le dossier data existe
os.makedirs("data", exist_ok=True)

with open('data/contributions.json', 'w') as f:
    json.dump(days, f)
    
print("Succès : Les données ont été sauvegardées dans data/contributions.json")