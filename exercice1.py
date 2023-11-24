# Exercice 1

# Proposer à l'utilisateur
N = int(input("Entrez un entier N : "))
somme = 0 # Initialise la variable somme à 0

for i in range(N + 1): # Parcourt les entiers de 0 à N inclus
    somme += i # Ajoute chaque entier à la somme

print(f"La somme des {N} premiers entiers naturels est : {somme}")

# B

valeur = 0 # Initialise la variable valeur à une valeur différente de 100 pour commencer la boucle

while valeur != 100: # Continue la boucle tant que l'utilisateur n'entre pas 100
    valeur = int(input("Entrez une valeur : ")) # Demande à l'utilisateur d'entrer une valeur

print("La boucle s'est terminée car vous avez entré la valeur 100.")

# C

# Initialise les compteurs pour chaque plage de valeurs
inferieur_10 = 0
entre_10_et_15 = 0
superieur_ou_egal_15 = 0

for i in range(10): # Boucle pour lire 10 valeurs
    valeur = float(input(f"Entrez la valeur réelle {i + 1}/10 : ")) # Demande à l'utilisateur d'entrer une valeur

while valeur < 0 or valeur > 20: # Vérifie si la valeur n'est pas comprise entre 0 et 20
    valeur = float(input("La valeur doit être comprise entre 0 et 20. Entrez une autre valeur : "))
# Redemande une valeur

if valeur < 10:
    inferieur_10 += 1
elif valeur < 15:
    entre_10_et_15 += 1
else:
    superieur_ou_egal_15 += 1

# Affichage des résultats
print(f"Nombre de valeurs inférieures strictement à 10 : {inferieur_10}")
print(f"Nombre de valeurs entre 10 inclus et 15 exclus : {entre_10_et_15}")
print(f"Nombre de valeurs supérieures ou égales à 15 : {superieur_ou_egal_15}")


# D

# Demander d'entrée S
S = int(input("Entrez un nombre supérieur à 1 (X) : "))
somme = 0
N = 0

while somme <= S:
    N += 1
    somme += N

plus_grand_N = N - 1

print(f"Le plus grand nombre N tel que la somme de 0 à N soit inférieure ou égale à {X} est : {plus_grand_N}")