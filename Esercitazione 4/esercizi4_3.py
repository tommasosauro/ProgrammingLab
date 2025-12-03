import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)
print(df.head(5))
print("\n")

#Conteggio campioni per specie

print("Il numero di campioni per specie è:")
conteggio_campioni = df["species"].value_counts()
print(conteggio_campioni)
print("\n")

#Lunghezza e larghezza media dei petali per specie

media_per_specie = df.groupby("species").mean()
print(media_per_specie["petal_length"] ,"\n", media_per_specie["petal_width"])
print("\n")

#Scatter con lunghezza e larghezza petali

plt.figure(figsize=(12,6))
sns.scatterplot(data=df, x="petal_length", y="petal_width", hue="species")
plt.xlabel("Lunghezza del petalo")
plt.ylabel("Larghezza del petalo")
plt.title("Dimensione dei petali per specie")
plt.legend(title="Specie")
plt.grid(True,alpha=0.2)
plt.show()
print("\n")

#Nuova colonna con l'area dei petali

df["petal_areas"] = df["petal_length"] * df["petal_width"]
print(df["petal_areas"])

#Grafico della distribuzione dell'area del petalo per specie

sns.boxplot(data=df, x="petal_areas", hue="species")
plt.xlabel("Area dei petali")
plt.title("Distribuzione dell'area dei petali")
plt.legend(title="Specie")
plt.grid(True, alpha=0.2)
plt.show()