#Altri esercizi sulla liberia Numpy

import numpy as np

#Esercizio 1

array_zeri = np.zeros(10)
print(array_zeri)

array_uni = np.ones((3,3))
print(array_uni)

array_1 = np.linspace(1,9,9)
print(array_1)

array_identita = np.eye(4,4)
print(array_identita)

print("\n")
print("\n")
print("\n")

#Esercizio 2

array = np.array([1,2,3,4,5])

somma_array = np.sum(array)
print(somma_array)

media_array = np.mean(array)
print(media_array)

std_array = np.std(array)
print(std_array)

elevazione_quadrato = array_1 ** 2
print(elevazione_quadrato)

array_piu_10 = array_1 + 10
print(array_piu_10)

print("\n")
print("\n")
print("\n")

#Esercizio 3

mat = np.arange(1, 26).reshape(5, 5)
print(mat)

print(mat[2, :])
print("\n")
print(mat[: ,1])
print("\n")
print(mat[:2, 3:])
print("\n")
print(mat[mat>15])

print("\n")
print("\n")
print("\n")

#Esercizio 4

a = np.arange(12)

a_reshape = a.reshape(3,4)
print(a_reshape)
a_flatten = a.flatten()
print(a_flatten)
a_2d = a.reshape(2,6)
a_2d = a_2d.transpose()
print(a_2d)

a_nuova = a
a_nuova = a_nuova * 2
print(a_nuova)

print("\n")
print("\n")
print("\n")

#Esercizio 5

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

prodotto_scalare = np.dot(a,b)
print(prodotto_scalare)

elemento_per_elemento = a * b
print(elemento_per_elemento)

prodotto_vettoriale = np.cross(a,b)
print(prodotto_vettoriale)

sin_di_a = np.sin(a)
print(sin_di_a)

print("\n")
print("\n")
print("\n")

#Esercizio 6

array_1_1 = np.random.random(10)
print(array_1_1)

array_2_1 = np.random.randint(1,100,size=(3,3))
print(array_2_1)

array_3_1 = np.linspace(0,9,10)

estrazione_random = np.random.randint(0,1,10)
print(estrazione_random)
print("\n")

numeri_scelti = np.empty(5)
j=0

for i in range(10):
    if estrazione_random[i] == 1:
        numeri_scelti[j] = array_3_1[i]
        j=j+1
    else:
        continue

print(numeri_scelti)

print("\n")
print("\n")
print("\n")

#Esercizio 7