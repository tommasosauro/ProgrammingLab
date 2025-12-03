#Esercitazione 2
#Esercizio 3

import numpy as np

array = np.random.random((10 , 3))
print("Array:")
print(array)
print()

differenze = np.abs(array - 0.5)
indici = np.argmin(differenze, axis=1)
valori_piu_vicini = array[np.arange(10), indici]

for i in range(10):
    print(f"Riga {i}: {array[i]}")
    print(f"L'elemento più vicino a 0.5 della riga è: {valori_piu_vicini[i]}")
    print()