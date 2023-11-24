# Exercice 5

# Création de fonctions
def calculate_cost(start_hour, end_hour):
    if not(0 <= start_hour <= 24) or not(0 <= end_hour <= 24):
        return "Les heures doivent être comprises entre 0 et 24 !"
    elif start_hour > end_hour:
        return "Attention ! le début de la location est après la fin ..."
    elif start_hour == end_hour:
        return "Attention ! l’heure de fin est identique à l’heure de début."
    else:
        early_hours = min(end_hour, 7) - start_hour
        late_hours = max(0, end_hour - 17)
        night_hours = max(0, 24 - end_hour) + max(0, start_hour - 7)
        return early_hours * 1 + late_hours * 2 + night_hours * 1,

def get_hours():
    while True:
        try:
            start_hour = int(input("Donnez l'heure de début de la location (un entier) : "))
            end_hour = int(input("Donnez l'heure de fin de la location (un entier) : "))
            return start_hour, end_hour
        except ValueError:
            print("Veuillez entrer des entiers.")

def main():
    start_hour, end_hour = get_hours()
    cost = calculate_cost(start_hour, end_hour)
    if isinstance(cost, tuple):
        early_hours, late_hours, night_hours = cost
        print(f"Vous avez loué votre vélo pendant {early_hours} heure(s) au tarif horaire de 1.0 euro(s) ")
        print(f"{late_hours} heure(s) au tarif horaire de 2.0 euro(s) ")
        print(f"{night_hours} heure(s) au tarif horaire de 1.0 euro(s) ")
        print(f"Le montant total à payer est de {early_hours + late_hours * 2 + night_hours} euro(s).")
    else:
        print(cost)
# Exécution du programme
if __name__ == "__main__":
    main()