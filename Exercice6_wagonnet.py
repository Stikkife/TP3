T = "Bonjour, je m'appelle Akif Aslankilic."

# Taille de la chaîne de caractères T
taille_chaine = len(T)

# Calcul du pourcentage de voyelles
nb_voyelles = sum(1 for char in T if char.lower() in 'aeiou')
pourcentage_voyelles = (nb_voyelles / (taille_chaine - 1)) * 100  
# On ne compte pas le caractère de fin de chaîne

# Vérifier si la sous-chaîne 'wagon' est présente dans T
if 'wagon' in T:
    # on regarde ou se trouve la première occurrence de 'wagon'
    debut_occurrence = T.index('wagon')
else:
    debut_occurrence = -1

# Calculer le nombre d'occurrences de la sous-chaîne 'wagon' dans T
nb_occurrences = T.count('wagon')

print("Taille de la chaîne de caractères T :", taille_chaine)
print("Pourcentage de voyelles :", pourcentage_voyelles)
print("Début de la première occurrence de 'wagon' :", debut_occurrence)
print("Nombre d'occurrences de 'wagon' dans T :", nb_occurrences)