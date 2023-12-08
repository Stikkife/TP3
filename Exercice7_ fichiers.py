import os
import datetime

# Demander à l'utilisateur le nom du ficher afin de le repérer
file1 = input("Entrez le nom du premier fichier: ")
file2 = input("Entrez le nom du deuxième fichier: ")

# Vérifier si le fichier existe
if os.path.isfile(file1) and os.path.isfile(file2):
  # Vérifier la taille des fichiers
  size1 = os.path.getsize(file1)
  size2 = os.path.getsize(file2)

  mtime1 = os.path.getmtime(file1)
  mtime2 = os.path.getmtime(file2)

  # Vérifier qui est le plus récent

  if mtime1 > mtime2:
    recent_file = file1
    mtime = mtime1
  else:
    recent_file = file2
    mtime = mtime2

  # Vérifier si le fichier est trop ancien
  mtime_readable = datetime.datetime.fromtimestamp(mtime)
  # Afficher le nom du fichier le plus récent et son nom complet
  print("Taille de", file1, ":", size1, "octets")
  print("Taille de", file2, ":", size2, "octets")
  print("Le fichier le plus récent est:", recent_file)
  print("Date de modification:", mtime_readable)
else:
  print("Au moins l'un des fichiers n'existe pas.")
