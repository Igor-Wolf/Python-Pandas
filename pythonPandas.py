import pandas as pd

df = pd.read_csv('dataset/Gapminder.csv', sep=';')

#Visualizando as 5 primeiras linhas

print(df.head())

df = df.rename(columns={"country":"País", "continent":"continente", "year":"Ano", "lifeExp":"Expec. de vida", "pop":"Pop Total", "gdpPercap":"PIB"})

print(df.head(10))
#Total  de linhas e colunas
print(df.shape)
#Retorna apenas as colunas
print(df.columns)
#Retorna o tipo dos objetos na tabela
print(df.dtypes)
#Retorna as ultimas linhas
print(df.tail())
#Descreve
print(df.describe())
#Filtros
print(df["continente"].unique())
#Filtro Oceania
oceania = df.loc[df["continente"]== "Oceania"]
print(oceania.head())
oceania["continente"].unique()
#Agrupamento de dados
print(df.groupby("continente")["País"].nunique())
print(df.groupby("Ano")["Expec. de vida"].mean())
print(df["PIB"].mean())
print(df["PIB"].sum())