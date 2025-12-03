import numpy as np

array = [1, 2, 3, 5, 7]
np_array = np.array(array)

print(len(np_array))
print(np_array.size)

#Mi aspetto che np_array abbia un tipo int.

print(np_array.dtype)

array_controllo_primi= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def controllo_primi(n):
    
    if n <= 2:
        return True
    for i in range(2,10):
        if n % i == 0:
            return False
    return True

numeri_primi = [n for n in array_controllo_primi if controllo_primi(n)]

print(numeri_primi)
