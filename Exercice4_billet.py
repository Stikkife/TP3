# Foncton pour compter le nombre de dinerooo
def entrelasommela(somme):
    billets100 = somme // 100
    reste = somme % 100
    billets50 = reste // 50
    reste %= 50
    billets10 = reste // 10
    reste %= 10
    pieces2 = reste // 2
    pieces1 = reste % 2

    print("Billets de 100:", billets100)
    print("Billets de 50:", billets50)
    print("Billets de 10:", billets10)
    print("Pièces de 2:", pieces2)
    print("Pièces de 1:", pieces1)


# Afficher le résultat
somme = int(input("Entrez la somme d'argent : "))
entrelasommela(somme)
