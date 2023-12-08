# Listes et coef qu'on inserera au fur et à mesure de la boucle for each
notes = []
coefficients = []
for i in range(5):
  note = float(input("Entrez la note {}: ".format(i + 1)))
  if note <= 20:
    notes.append(note)
    coefficient = int(
        input("Entrez le coefficient de la note {}: ".format(i + 1)))
    coefficients.append(coefficient)
  else:
    print("La note doit être comprise entre 0 et 20")

# Calculons la moyenne pondérée
moyenne = sum(note * coeff for note, coeff in zip(notes, coefficients))
somme_coef = sum(coefficients)
result = moyenne / somme_coef
print("La note finale est:", result)
