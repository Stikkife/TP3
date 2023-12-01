# Création du dictionnaire avec vos informations
mon_dictionnaire = {
    'name': 'ASLANKILIC',
    'firstname': 'Akif',
    'promo': 2023,
    'group': 'R111'
}

# Affichage des informations personnelles
print(f"Votre nom est '{mon_dictionnaire['name']}', prénom est '{mon_dictionnaire['firstname']}',"
      f" vous faites partie de la promo '{mon_dictionnaire['promo']}' et votre groupe est '{mon_dictionnaire['group']}'")

# Affichage du contenu du dictionnaire avec les méthodes keys(), values() et items()
print("\nLes clés du dictionnaire sont :")
for key in mon_dictionnaire.keys():
    print(f"-{key}")

print("\nLes valeurs du dictionnaire sont :")
for value in mon_dictionnaire.values():
    print(f"-{value}")

print("\nLes tuplets du dictionnaire sont :")
for item in mon_dictionnaire.items():
    print(f"-{item}")

# Ajout d'un autre dictionnaire pour former un binôme
binome = {
    'name': 'Patyan',
    'firstname': 'Micha',
    'promo': 2021,
    'group': 'RT???'
}

# Création du dictionnaire binôme
dictionnaire_binome = {
    '001': mon_dictionnaire,
    '002': binome
}

# Affichage des membres du binôme
print("\nLes étudiants formant le binôme sont :")
for id, etudiant in dictionnaire_binome.items():
    print(f"- L'étudiant {etudiant['firstname']} {etudiant['name']} du groupe {etudiant['group']}")
