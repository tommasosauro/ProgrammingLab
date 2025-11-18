#Esercitazione 2
#Esercizio 2

import numpy as np

array_2d = np.random.randint(1, 50, size=(5 , 5))
print("Array 2D originale:")
print(array_2d)

b = array_2d[:, [1, 3]]

print("Elementi delle colonne 2 e 4:")
print(b)

c = array_2d[:, 2]

print("Elementi della colonna 3:")
print(c)
