#Esercitazione 2
#Esercizio 1

import numpy as np

array = np.array([2,3,5,7,11,13,17,19])

array_10 = array[array>10]
print(array_10)

array_pari = array[array%2==0]
print(array_pari)