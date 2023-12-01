def tri_selection(tableau):
  n = len(tableau)
  for i in range(n):
      min_index = i
      for j in range(i + 1, n):
          if tableau[j] < tableau[min_index]:
              min_index = j
      tableau[i], tableau[min_index] = tableau[min_index], tableau[i]
      print(tableau)


# Déclarer une liste avec les éléments de l'exemple
tab = [5, 2, 4, 8, 1, 3]

# Affichage de l'évolution du tri
print(tab)
tri_selection(tab)

# Affichage de la liste après le tri avec la fonction sorted()
print("Après utilisation de sorted():", sorted(tab))

# Affichage de la liste après le tri avec la méthode sort()
tab.sort()
print("Après utilisation de tab.sort():", tab)