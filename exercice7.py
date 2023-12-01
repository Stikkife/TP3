# Partie 1
binome = ('AKIIIFF',1, 'MOHA',2)
print(f"L'étudiant {binome[0]} est en binôme avec l'étudiant {binome[1]}")

# Partie 2
nouveau_login = input("Entrez le nouveau login pour changer de binôme : ")
binome = (binome[0], nouveau_login)
print(f"Nouveau binôme : L'étudiant {binome[0]} est en binôme avec l'étudiant {binome[1]}")

# Partie 3
# --> del binome[1]  # Cette ligne générera une erreur, car les tuples ne supportent pas l'opération de suppression

# Partie 4
troisieme_element = input("Entrez le troisième élément pour former un trinôme : ")
binome = binome + (troisieme_element,)
print(f"Trinôme : {binome}")