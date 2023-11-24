# Exercice 4
# Création d'une fonction
def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n-1)

def calculate_factorial_iteratively(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    n = int(input("Entrez un entier: "))
    print("1. Boucle récursive")
    print("2. Boucle itérative")
    choice = int(input("Choisissez le type de boucle à utiliser: "))

    if choice == 1:
        result = calculate_factorial(n)
        print("La factorielle de {} est {}.".format(n, result))
    elif choice == 2:
        result = calculate_factorial_iteratively(n)
        print("La factorielle de {} est {}.".format(n, result))
    else:
        print("Choix non valide.")
