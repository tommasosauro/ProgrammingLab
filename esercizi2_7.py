#Esercitazione 2
#Esercizio 7

import numpy as np

survey_matrix = np.array([ [25, 40000, 10], [32, 52000, 12], [40, 63000, 14], [29, 47000, 11], [35, 58000, 13] ])

survey_matrix_12_anni= survey_matrix[survey_matrix[:,2] >= 12]
print("I dipendenti con almeno 12 anni di esperienza sono:\n", survey_matrix_12_anni)

survey_matrix_redditi = survey_matrix_12_anni[:,1]
print("I redditi dei dipendenti con almeno 12 anni di esperienza sono:\n", survey_matrix_redditi)

media_redditi = np.mean(survey_matrix_redditi)
print("La media dei redditi dei dipendenti con almeno 12 anni di esperienza è:", media_redditi,"dollari.")
