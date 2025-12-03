#Esercitazione 3
#Esercizio 1

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("https://raw.githubusercontent.com/fivethirtyeight/data/master/alcohol-consumption/drinks.csv")

df.sort_values("total_litres_of_pure_alcohol", ascending=False, inplace=True)

print("I 10 paesi con il più alto consumo di alcol sono:")
print(df[['country', 'total_litres_of_pure_alcohol']].head(10))


media_birra = df['beer_servings'].mean()
media_vino = df['wine_servings'].mean()
media_distillati = df['spirit_servings'].mean()

print("Il consumo medio di birra è:" , media_birra)
print("Il consumo medio di vino è:" , media_vino)
print("Il consumo medio di distillati è:" , media_distillati)


df['alcohol_index'] = (df['beer_servings'] + df['wine_servings'] + df['spirit_servings']) / 3
paese_max = df.loc[df['alcohol_index'].idxmax()]
print("Il paese con il valore massimo nell'indice Alcohol Index è:" , paese_max['country'])

paesi_con_più_di_100_birre = df[df['beer_servings'] > 100] 
print("I paesi con un consumo di birra superiore a 100 sono:" , len(paesi_con_più_di_100_birre))

plt.figure(figsize=(10,5))
plt.bar(df['country'].head(10), df['total_litres_of_pure_alcohol'].head(10))
plt.title("Top 10 paesi per consumo di alcol")
plt.xlabel("Paesi")
plt.ylabel("Litri di alcol puro")
plt.xticks(rotation=45)
plt.show()

vini_ordinati = df.sort_values("wine_servings", ascending=False)
plt.figure(figsize=(50,25))
plt.plot(vini_ordinati['country'], vini_ordinati['wine_servings'], marker='o')
plt.title("Consumo di vino per paese")
plt.xlabel("Paesi")
plt.ylabel("Porzioni di vino")
plt.xticks(rotation=45)
plt.show()
