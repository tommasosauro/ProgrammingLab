#Esercitazione 2
#Esercizio 5

import numpy as np

stipendi = np.array([50000, 105250, 55000, 89000])

costo_personale = np.sum(stipendi)
print("Il costo totale del personale è:", costo_personale)

variazione_stipendi = np.where(stipendi==105250, stipendi * 1.15, stipendi)
print("Gli stipendi dopo la variazione sono:", variazione_stipendi)

#Nel mio array è presente lo stipendio di 121.037,5 dollari.

variazione_stipendi2 = np.where(stipendi==50000, stipendi * 1.2, variazione_stipendi)
print("Gli stipendi dopo la seconda variazione sono:", variazione_stipendi2)

variazione_stipendi3 = np.where(stipendi==55000, stipendi * 1.1, variazione_stipendi2)
variazioone_stipendi3 = np.where(stipendi==89000, stipendi * 1.1, variazione_stipendi3)
print("Gli stipendi dopo la terza variazione sono:", variazione_stipendi3)

costo_personale_finale = np.sum(variazione_stipendi3)
print("Il costo totale del personale dopo le variazioni è:", costo_personale_finale)

print("Dopo l'aumento dello stipendio dei CEO, gli altri aumenti sono costati all'azienda un totale di:", costo_personale_finale - costo_personale, "dollari in più.")
