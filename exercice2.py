# Coded By Akif
# Demande le nombre d'étudiants à l'utilisateur
nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
# déclaration d’une liste vide qui va contenir autant de notes que d'étudiants
notes = []
for i in range(nombreEtudiants):
  note = float(input("Donnez la note de l'étudiant : "))
  moyenne = moyenne + note
moyenne = moyenne / nombreEtudiants
print("La moyenne des notes est : ", moyenne)