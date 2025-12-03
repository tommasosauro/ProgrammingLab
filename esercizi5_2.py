import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Caricamento del dataset
url = 'https://zenodo.org/record/5898311/files/vgsales.csv'
df = pd.read_csv(url)
print("Database:")
print(df.head(5))

#Videogiochi pubblicati
videogiochi = df["Name"].value_counts()
print("Sono stati pubblicati", len(videogiochi), "videogiochi")
print("\n")

#Generi più popolari
generi = df["Genre"].value_counts()
print(generi)
plt.figure(figsize=(12,6))
plt.plot(generi)
plt.title("Genere più popolari")
plt.xlabel("Generi")
plt.ylabel("Popolarità")
plt.grid(False)
plt.show()
print("\n")

#Evoluzione videogiochi nel tempo
videogiochi_negli_anni = df["Year"].value_counts().sort_index()
plt.figure(figsize=(12,6))
plt.plot(videogiochi_negli_anni.values , videogiochi_negli_anni.index)
plt.title("Evoluzione videogiochi negli anni")
plt.xlabel("Anni")
plt.ylabel("Aumento videogiochi")
plt.grid(False)
plt.show()
print("\n")

#Riprodurre il grafico dell'esercizio

plt.figure(figsize=(12,6))
sns.histplot(data=df, x=["Genre"], y=["Global_Sales"])
plt.title("Vendite per genere")
plt.xlabel("Genere")
plt.ylabel("Milioni di unità")
plt.grid(False)
plt.show()

