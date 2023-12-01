def table_multiplication(nombre, n):
  resultat = [nombre * i for i in range(n+1)]
  return resultat


# Demander à l'utilisateur le nombre pour la table de multiplication
nombre = float(input("Vous cherchez la table de multiplication de quel nombre ? "))

# Demander à l'utilisateur la taille de la table de multiplication
n = int(input("Jusqu'à quelle valeur souhaitez-vous générer la table de multiplication ? "))

# Générer la table de multiplication
table = table_multiplication(nombre, n)

# Afficher la table de multiplication
print(f"\nTable de multiplication de {nombre}:")
for i, resultat in enumerate(table):
    print(f"{nombre} * {i} = {round(resultat, 1)}")
