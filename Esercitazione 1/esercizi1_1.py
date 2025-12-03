#Esercitazione 1
#Esercizio 1: Fai tre esempi di cicli che producono una lista e poi riscrivi lo stesso codice usando la list comprehension.

#Esempio 1
numeri = [1,2,3,4,5]
quadrati = []

for n in numeri:
    quadrati.append(n**2)


numeri1 = numeri.copy()
quadrati1= [n**2 for n in numeri1]

print(quadrati)
print(quadrati1)

#Esempio 2
numeri2= [1,2,3,4,5,6]
numeri_pari = []

for n in numeri:
    if n % 2 == 0:
        numeri_pari.append(n)

numeri3 = numeri2.copy()
numeri_pari1 = [n for n in numeri3 if n % 2 == 0]

print(numeri_pari)
print(numeri_pari1)

#Esempio 3
numeri4 = [1,2,3,4,5,6]
divisi_per_2 = []

for n in numeri4:
    divisi_per_2.append(n / 2)

numeri5 = numeri4.copy()
divisi_per_21 = [n / 2 for n in numeri5]

print(divisi_per_2)
print(divisi_per_21)