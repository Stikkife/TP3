nom = input("Entrez votre nom : ")
prenom = input("Entrez votre prénom : ")

nom = nom.upper()
prenom = prenom.capitalize()

total = nom + ' ' + prenom
sorted_name = ' '.join(sorted(total.split(), key=str.lower))
print(sorted_name)
