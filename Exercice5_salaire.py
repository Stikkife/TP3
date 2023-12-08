# Fonction pour calculer le salaire
def calculer_salaire(nombreheures, salairehoraire):
  if nombreheures <= 160:
    salaire = nombreheures * salairehoraire
  elif 160 < nombreheures <= 200:
    salaire = 160 * salairehoraire + (nombreheures -
                                      160) * salairehoraire * 1.25
  else:
    salaire = 160 * salairehoraire + 40 * salairehoraire * 1.25
    +(nombreheures - 200) * salairehoraire * 1.5
  return salaire


# Entrées - Sorties
heurestravaillees = int(input("Nombre d'heures travaillées : "))
salairehoraire = float(input("Salaire horaire : "))
salairetotal = calculer_salaire(heurestravaillees, salairehoraire)
print("Le salaire total est de : ", salairetotal)
