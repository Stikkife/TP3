# Fonction qui va directement nous permettre de savoir si c'en est un ou pas.
def palindrome(s):
  s = s.lower()
  return s == s[::-1]


mot = input("Entrez une chaine de caractères : ")

if palindrome(mot):
  print("C'est un palindrome")
else:
  print("Ce n'est pas un palindrome")