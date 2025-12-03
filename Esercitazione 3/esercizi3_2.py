#Esercitazione 3
#Esercizio 1

import pandas as pd
import matplotlib.pyplot as plt 
from datasets import load_dataset

dataset = load_dataset('lukebarousse/data_jobs')
df = dataset['train'].to_pandas()
df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])

df.sort_values("salary_year_avg", ascending=False, inplace=True)

plt.figure(figsize=(10,5))
plt.bar(df['salary_year_avg'] , df['job_title_short'])
plt.title("Salario medio annuo per titolo di lavoro")
plt.xlabel("Salario medio annuo")
plt.ylabel("Titolo di lavoro")   
plt.xticks(rotation=45)
plt.show()