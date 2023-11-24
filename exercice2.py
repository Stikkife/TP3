# Exercice 2
# Importation de la librarie Time
import time

n = int(input("Entrez un nombre entier n positif: "))

for i in range(n, 0, -1):
    print(i)
    time.sleep(1)

import time

n = int(input("Entrez un nombre entier n positif: "))

while n >= 0:
    print(n)
    n -= 1
    time.sleep(1)
