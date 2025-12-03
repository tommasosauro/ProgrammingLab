import pandas as pd

sales = pd.DataFrame(
    data={
        "employee": [
            "Katrina",
            "Guanyu",
            "Jan",
            "Roman",
            "Jacqueline",
            "Paola",
            "Esperanza",
            "Alaina",
            "Egweyn",
        ],
        "sales": [14, 17, 6, 12, 8, 3, 7, 15, 5],
        "year": [2018, 2019, 2020, 2018, 2020, 2019, 2019, 2020, 2020],
    }
)

print("Database iniziale")
print(sales)
print("\n")

#Mostra le maggiori 10 vendite
sales_ordinate = sales["sales"].sort_values()
print("Le 10 maggiori vendite sono:")
print(sales_ordinate.head(10))
print("\n")

#Mostra i dati del 2018
sales_2018 = sales[sales["year"]==2018] #sales.query("year == 2018")
print(sales_2018) 
print("\n")

#Vendite maggiori di 13 nel 2018
sales_2018_maggiori_di_13 = sales_2018[sales_2018["sales"] > 13] #sales.query("sales > 13")
print(sales_2018_maggiori_di_13)
print("\n")

#Mostra tutto tranne i casi in cui le vendite sono maggiori di 13 e l'anno è il 2018
sales_fix = sales[sales["year"] != 2018]
sales_fix = sales_fix[sales["sales"] < 13]
print(sales_fix)
print("\n")

#Mostra solo i dati dove le vendite diviso per 3 sono maggiori di 3
sales_fix2 = sales[(sales["sales"] / 3) > 3]
print(sales_fix2)
print("\n")

#Mostra i dipendenti i cui nomi sono alfabeticamente dopo la J
dipendenti_J = sales[sales["employee"] > "J"]
print(dipendenti_J)