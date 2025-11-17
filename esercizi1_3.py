import numpy as np 
    
#Utilizando NumPy
a = np.arange(1,5)
b = a[1:3]
c = a[::-1]

a_diviso_c= a / c

#Utilizzando liste di Python

a_lista = list(range(1,5))
b_lista = a_lista[1:3]
c_lista = a_lista[::-1]

a_diviso_c_lista = [a_lista[i] / c_lista[i] for i in range(len(a_lista))]

print("Array NumPy divisione:", a_diviso_c)
print("Lista Python divisione:", a_diviso_c_lista)

print("Tipo risultato NumPy:", type(a_diviso_c))
print("Tipo risultato Lista Python:", type(a_diviso_c_lista))