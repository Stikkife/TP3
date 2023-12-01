# Coded By Akif
# Partie 1
L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

# Completez le programme a partir d'ici.

def most_frequent(lst):
  # Trouver le nombre le plus demandé
  most_common = max(set(lst), key=lst.count)
  # Utilisation de la fonction count
  count_most_common = lst.count(most_common)
  return most_common, count_most_common


if __name__ == "__main__":
  # Exemple d'utilisation
  result = most_frequent(L1)

  print("Le nombre qui s'affiche le plus est", result[0], "et il est compter",
        result[1])

# Ne rien modifier apres cette ligne.
