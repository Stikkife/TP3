# Coded by Akif
def bissextile(annee):
  return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)

def date_valide(date):
  if len(date) != 8:
      return False

  jour = int(date[:2])
  mois = int(date[2:4])
  annee = int(date[4:])

  if mois < 1 or mois > 12:
      return False

  jours_par_mois = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

  if bissextile(annee):
      jours_par_mois[2] = 29

  return 1 <= jour <= jours_par_mois[mois]


# Verification avec les dates suivantes
dates = ["3102199", "31041000", "32052020", "30032021", "29022022"]

for date in dates:
    if date_valide(date):
        print(f"{date} est une date valide.")

    else:
        print(f"{date} n'est pas une date valide.")
