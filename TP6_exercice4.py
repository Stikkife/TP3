# PREMIERE PARTIE 
# import random
# ## Fonction generer(nbr, vmin, vmax) pour générer un tableau de 'nbr'
# def generer(nbr,vmin, vmax):
#   return [random.randint(vmin, vmax) 
#           for i in range(nbr)
#          ]

# ## Fonction combienInferieur(table, vseuil) pour compter le nombre de valeurs
# def combienInferieur(table, vseuil):
#   return len(
#     [nombre for nombre in table 
#         if nombre < vseuil
#     ])

# ## d'un tableau 'table' inférieures à la valeur 'vseuil'…

# nb = 100
# print(f"Générer {nb} nombres entiers entre 0 et 100")
# tab = generer(nb, 0, 100)
# tab.sort()
# print(tab)
# total = combienInferieur(tab, 25)
# print(f"Il y en a {total} inférieurs à 25")

# DEUXIEME PARTIE - VEUILLEZ ENLEVER LES COMMENTAIRES QUE VOUS SOUHAITEZ 

# import random
# ## Fonction generer(nbr, vmin, vmax) pour générer un tableau de 'nbr'
# def generer(nbr,vmin, vmax):
#   return [random.randint(vmin, vmax) 
#           for i in range(nbr)
#          ]

# ## Fonction combienInferieur(table, vseuil) pour compter le nombre de valeurs
# def combienInferieur(table, vseuil):
#   return len(
#     [nombre for nombre in table 
#         if nombre < vseuil
#     ])

# ## d'un tableau 'table' inférieures à la valeur 'vseuil'…

# nb = int(input("Veuillez préciser le nombre de valeurs à ajouter entre 0 et 100: "))
# print(f"Générer {nb} nombres entiers entre 0 et 100")
# vmin = int(input("Veuillez préciser la valeur du seuil minimale: "))
# vmax = int(input("Veuillez préciser la valeur du seuil maximale: "))
# tab = generer(nb, vmin, vmax)
# tab.sort()
# print(tab)
# vinf = int(input("Veuillez me préciser à partir de quelle valeur voulez-vous compter les inférieurs : "))
# total = combienInferieur(tab, vinf)
# print(f"Il y en a {total} inférieurs à {vinf}")