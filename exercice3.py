# Exercice 3
import random

# Création d'une fonction
def generate_random_number():
    return random.randint(0, 100)

    secret_number = generate_random_number()
    count = 0
    guess = -1

    while guess != secret_number:
        try:
            guess = int(input("Entrez un nombre entre 0 et 100: "))
        except ValueError:
            print("Veuillez entrer un nombre entier.")
            continue

        count += 1

        if guess == secret_number:
            print("Félicitations! Vous avez deviné le nombre correct en {} tours.".format(count))
        elif guess > secret_number:
            print("Le nombre à deviner est plus petit.")
        else:
            print("Le nombre à deviner est plus grand.")

    play_again = input("Voulez-vous jouer à nouveau? (O/N) ")
    if play_again.lower() == "o":
        play_game()

if __name__ == "__main__":
    play_game()
