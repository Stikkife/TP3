# Coded By Akif
nMax = 3
v1 = []
v2 = []

n = int(input(f"Entrez la taille des vecteurs (entre 1 et {nMax}): "))
while not 1 <= n <= nMax:
    n = int(input("La taille doit être entre 1 et {nMax}. Entrez à nouveau : "))

v1 = [int(input(f"Entrez la composante v1[{i}]: ")) for i in range(n)]
v2 = [int(input(f"Entrez la composante v2[{i}]: ")) for i in range(n)]

produit_scalaire = sum(x * y for x, y in zip(v1, v2))
print("Le produit scalaire de v1 et v2 est :", produit_scalaire)