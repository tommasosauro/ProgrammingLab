#Esercitazione 4
#Esercizio 1

import numpy as np
import matplotlib.pyplot as plt

vettore_possibilita = ['T','C']
vettore_probabilita = [0.5,0.5]

def lancio_moneta(n):

    vettore_risultati = []

    risultato_lancio = np.random.choice(vettore_possibilita, n, vettore_probabilita)

    counter = np.sum(risultato_lancio == 'T')
        
    return float(counter/n)

vettore_probabilita_teste = []
dimensione_campione = []


for i in range (100):

    n_lanci = np.random.randint(10,20000)

    probabilita=lancio_moneta(n_lanci)

    vettore_probabilita_teste.append(probabilita)
    dimensione_campione.append(n_lanci)

print(vettore_probabilita_teste)    

plt.figure(figsize=(12,6))
plt.plot(dimensione_campione,vettore_probabilita_teste,alpha=0.8)
plt.xlabel("Dimensione del campione")
plt.ylabel("Frequenza di uscita Testa")
plt.title("Legge dei Grandi Numeri relativa al lancio di una moneta")
plt.show()