import json

try:
    with open('data/contributions.json', 'r') as f:
        days = json.load(f)
except FileNotFoundError:
    print("Erreur : data/contributions.json introuvable. Lance fetch_contributions.py d'abord.")
    exit()

# Les couleurs officielles de GitHub pour le mode sombre
PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]
box_size = 10
gap = 4

svg_content = [
    '<svg xmlns="http://www.w3.org/2000/svg" width="860" height="150">',
    '<style>',
    '  .day { animation: slideIn 0.8s ease-out forwards; opacity: 0; transform: translateY(-10px); }',
    '  @keyframes slideIn { to { opacity: 1; transform: translateY(0); } }',
    '</style>',
    '<g transform="translate(20, 20)">'
]

# Dessine la grille de 53 semaines
for i, day in enumerate(days):
    week = i // 7
    day_of_week = i % 7
    x = week * (box_size + gap)
    y = day_of_week * (box_size + gap)
    
    # Niveau de contribution (0 à 4)
    level = min(day['level'], 4)
    color = PALETTE[level]
    
    # Décalage de l'animation pour l'effet d'apparition en diagonale
    delay = (week * 10) + (day_of_week * 20)
    
    rect = f'<rect class="day" x="{x}" y="{y}" width="{box_size}" height="{box_size}" rx="2" fill="{color}" style="animation-delay: {delay}ms" />'
    svg_content.append(rect)

svg_content.append('</g></svg>')

with open('contrib-heatmap.svg', 'w') as f:
    f.write("\n".join(svg_content))
    
print("Succès : Image contrib-heatmap.svg générée à la racine.")