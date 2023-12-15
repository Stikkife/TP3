# déclaration de la fonction ajouter_elt(lst=[0, 1, 2], elt=3)
def ajouter_elt(lst=[0,1,2], elt=3):
  lst.append(elt)
  return lst
print(ajouter_elt())
print(id(ajouter_elt()))
print(ajouter_elt()) 
print(id(ajouter_elt()))
# Ils gardent la même ID

def ajouter_elted(lst=["abc"], elt="d"):
  lst.append(elt)
  return lst
print(ajouter_elted())
print(id(ajouter_elted()))
print(ajouter_elted()) 
print(id(ajouter_elted()))
# Ses deux dernières valeurs gardent aussi la même ID