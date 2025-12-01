import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print(f"1. Il dataset ha {df.shape[0]} righe e {df.shape[1]} colonne\n")

print("2. Valori mancanti PER OGNI COLONNA:")
null_counts = df.isnull().sum()
for column, count in null_counts.items():
    if count > 0:
        print(f"   '{column}': {count} valori mancanti ({count/len(df)*100:.1f}%)")
    else:
        print(f"   '{column}': {count} valori mancanti")
print()

print("2. Valori mancanti per colonna (formato tabellare):")
print(df.isnull().sum())
print()

embarked_mode = df['Embarked'].mode()[0]
df['Embarked'].fillna(embarked_mode, inplace=True)
print(f"3. Valori mancanti in 'Embarked' sostituiti con: {embarked_mode}")
print(f"   Valori mancanti in 'Embarked' dopo il fill: {df['Embarked'].isnull().sum()}\n")

print(f"4. Righe prima della rimozione: {df.shape[0]}")
df = df.dropna(subset=['Age'])
print(f"   Righe dopo aver rimosso i valori mancanti in 'Age': {df.shape[0]}")
print(f"   Righe rimosse: {891 - df.shape[0]}")
print()

duplicates = df.duplicated().sum()
print(f"5. Righe duplicate: {duplicates}")
if duplicates > 0:
    print("   Prime righe duplicate:")
    print(df[df.duplicated()].head())
print()

age_by_class = df.groupby('Pclass')['Age'].mean()
print("6. Età media dei passeggeri per classe:")
for pclass, avg_age in age_by_class.items():
    print(f"   Classe {pclass}: {avg_age:.2f} anni")
print()

print("7. Visualizzazione distribuzione età per classe...")
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
for pclass in sorted(df['Pclass'].unique()):
    sns.kdeplot(df[df['Pclass'] == pclass]['Age'], label=f'Classe {pclass}')
plt.title('Distribuzione dell\'età per classe (Density Plot)')
plt.xlabel('Età')
plt.ylabel('Densità')
plt.legend()

plt.subplot(1, 2, 2)
sns.boxplot(x='Pclass', y='Age', data=df)
plt.title('Distribuzione dell\'età per classe (Box Plot)')
plt.xlabel('Classe')
plt.ylabel('Età')

plt.tight_layout()
plt.show()

print("8. Visualizzazione distribuzione età per classe e sesso...")
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
for sex in df['Sex'].unique():
    for pclass in sorted(df['Pclass'].unique()):
        subset = df[(df['Sex'] == sex) & (df['Pclass'] == pclass)]
        if not subset.empty:
            sns.kdeplot(subset['Age'], label=f'{sex} - Classe {pclass}')
plt.title('Distribuzione dell\'età per sesso e classe (Density Plot)')
plt.xlabel('Età')
plt.ylabel('Densità')
plt.legend()

plt.subplot(1, 2, 2)
sns.boxplot(x='Pclass', y='Age', hue='Sex', data=df)
plt.title('Distribuzione dell\'età per classe e sesso (Box Plot)')
plt.xlabel('Classe')
plt.ylabel('Età')
plt.legend(title='Sesso')

plt.tight_layout()
plt.show()
