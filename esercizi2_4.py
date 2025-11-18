#Esercitazione 2
#Esercizio 4

import numpy as np

frequenza_cardiaca = np.array([68, 65, 77, 110, 160, 161, 162, 161 ,160, 161, 162, 163, 162, 100, 90, 97, 72, 60, 60])

frequenza_minima = np.min(frequenza_cardiaca)
print("Frequenza cardiaca minima:", frequenza_minima)

frequenza_massima = np.max(frequenza_cardiaca)
print("Frequenza cardiaca massima:", frequenza_massima)

frequenza_superiore_120 = frequenza_cardiaca[frequenza_cardiaca > 120]
print("Frequenze cardiache superiori a 120:", frequenza_superiore_120)

totale_120 = 0
for frequenza in frequenza_cardiaca:
    if frequenza > 120:
        totale_120 = totale_120 + 1 
percentuale_frequenza_superiore_120 = totale_120 / len(frequenza_cardiaca) * 100
print("Percentuale di frequenze cardiache superiori a 120:", percentuale_frequenza_superiore_120,"%")

