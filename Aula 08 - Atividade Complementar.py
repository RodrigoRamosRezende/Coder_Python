import pandas as pd

#Abra o arquivo "best-selling game consoles.xlsx" em um DataFrame
df = pd.read_excel("best-selling game consoles.xlsx", sheet_name='consoles')

#Substitua a palavra "NES" por "Nitendinho" no nome dos consoles e deixe todos os nomes em maiúsculos
df["Console Name"] = df["Console Name"].str.replace("NES", "Nitendinho").str.upper()

#Filtre o nome dos consoles com data de release depois de 2010
df = df[df["Released Year"] > 2010]

#Substitua os missing values pela string "missing"
df = df.fillna("missing")

#Filtre os consoles que foram descontinuados a menos de 2 anos da data de release
df = df[(df["Discontinuation Year"] - df["Released Year"]) < 2]

#Exiba o DataFrame resultante após todas as operações
print("\nDataFrame após as operações:")
print(df)
#De um Describe
print("Descrição da base de dados:")
print(df.describe().round())
##De um Info da Base
print("\nInformações da base de dados:")
print(df.info())