#Esercitazione 2
#Esercizio 9

import numpy as np

lista_parole = [
    'INSEDIAMENTO', 'SEPARAZIONE', 'DIFFERENZA', 'APPLICAZIONE', 'ATTEGGIAMENTO', 'VERDURA', 'IMPERO', 'RICEVIMENTO',
    'IGNORANZA', 'BIOGRAFIA', 'VISIONE', 'AGENTE DI POLIZIA', 'PROVA', 'PRESTAZIONE', 'PRESENTAZIONE', 'PARENTE',
    'GIUSTIFICAZIONE', 'FILOSOFIA', 'DIREZIONE', 'BENEFICIARIO', 'BATTERIA', 'CERIMONIA', 'AGONIA', 'RECUPERO',
    'ALFABETIZZAZIONE', 'CONSEGNA', 'SERBATOIO', 'VOLONTARIO', 'DEPOSITO', 'BIRILLO DA BOWLING', 'NEMICO', 'ANNUNCIO',
    'CARAMELLA ZUCCHERATA', 'FULMINE', 'PALLONCINO', 'COPERTA', 'SCOPERTA', 'PENALITÀ', 'GENERALE', 'ALPACA',
    'VANTAGGIO', 'HOT DOG', 'ABITO', 'MATEMATICA', 'VARIANTE']

for parola in lista_parole:
    parole_scelte = np.random.choice(lista_parole  , size=5, replace=True)
      
print("In epoche passate, viveva una donna saggia che era molto orgogliosa dell'antico", parole_scelte[0], "che proteggeva. Quando un anziano del villaggio venne a chiederle consiglio su come garantire al meglio un raccolto abbondante e le offrì il", parole_scelte[1], "come dono, i suoi occhi si spalancarono e lei esclamò una sola parola", parole_scelte[2],".",
"Radunò il villaggio e, per i successivi 100 giorni, su sua richiesta, gli abitanti cercarono nella foresta un", parole_scelte[3],".",
"Nel centounesimo giorno, il bambino più giovane del villaggio trovò ciò che stavano cercando e tutti corsero dalla donna saggia per donarglielo.",
"Con un sorriso da un orecchio all altro, e cantando canti di festa, la donna saggia guardò i suoi compaesani e disse: Ora è giunto il tempo del banchetto nessuno rimarrà mai più senza", parole_scelte[4], "Ci fu grande gioia e celebrazione.")
