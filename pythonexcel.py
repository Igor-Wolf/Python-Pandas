#Manipulando das do excel com pandas, Conceitos
import pandas as pd
import matplotlib.pyplot as plt

#leitura dos arquivos
df1 = pd.read_excel('dataset/Aracaju.xlsx')
df2 = pd.read_excel('dataset/Fortaleza.xlsx')
df3 = pd.read_excel('dataset/Natal.xlsx')
df4 = pd.read_excel('dataset/Recife.xlsx')
df5 = pd.read_excel('dataset/Salvador.xlsx')

print(df1.head())

#juntar as planilhas
df= pd.concat([df1,df2,df3,df4,df5])

#Exibindo as 5 primeiras linhas
print(df.head())

#Exibindo as 5 ultimas linhas
print(df.tail())

#Exibindo uma amostra aleatoria com 5 linhas
print(df.sample(5))

#verificando o tipo de dado e cada coluna
print(df.dtypes)

#Alterar o tipo de dado de uma coluna
df["LojaID"] = df ["LojaID"].astype("object")

print(df.dtypes)
#--------------------------------------------------------------------------------

#Consultando linhas com valores faltantes
print(df.isnull().sum())

#Substituindo os valores nulos pela média
df["Vendas"].fillna(df["Vendas"].mean(), inplace=True)

print(df.isnull().sum())

#Substituindo os valores nulos por zero
df["Vendas"].fillna(0, inplace=True)

#Apagando as linhas com valores nulos
df.dropna(inplace=True)

#Apagando as linhas com valores nulos com base apenas e 1 coluna
df.dropna(subset = ["Vendas"], inplace=True)

#Removendo linhas que estejam com valores faltantes em todas as colunas
df.dropna(how="all", inplace=True)

#--------------------------------------------------------------------------------

#Criando colunas novas
df["Receita"] = df["Vendas"].mul(df["Qtde"])
print(df.head())

df["Recita/Vendas"] = df["Receita"] / df["Vendas"]
print(df.head())

#Retornando a maior receita
print(df["Receita"].max())

#Retornando a menor receita
print(df["Receita"].min())

#nlargest
print(df.nlargest(3,"Receita"))

#nsmallest
print(df.nsmallest(3,"Receita"))

#Agrupamento por cidade
print(df.groupby("Cidade") ["Receita"].sum())

#Ordenando o conjunto de dados
print(df.sort_values("Receita", ascending=False).head(10))

#--------------------------------------------------------------------------------

#Trabalhando com datas 

#Transformando a colunade data em tipo inteiro
df["Data"] = df["Data"].astype("int64")

#Verificando o tipo de dado de cada coluna
print(df.dtypes)

#Transformando a coluna de data em data
df["Data"] = pd.to_datetime(df["Data"])
print(df.dtypes)

#Agrupamento por ano
df.groupby(df["Data"].dt.year)["Receita"].sum()

#Criando uma nova coluna com o ano
df["Ano_Venda"] = df["Data"].dt.year

print(df.sample(5))

#Extraindo o mês e o dia
df["mes_venda"], df["dia_venda"] = (df["Data"].dt.month, df["Data"].dt.day)
print(df.sample(5))

#Retornando a data mais antiga
print(df["Data"].min())

#Calculando a diferença de dias

df["diferenca_dias"] = df["Data"] - df["Data"].min()

print(df.sample(5))

#Criando coluna com trimestre

df["trimestre_vendas"] = df["Data"].dt.quarter
df.sample(5)

#Filtrando as vendas de 2019 do mês de março

vendas_marco_19 = df.loc[(df["Data"].dt.year == 2019) & (df["Data"].dt.month == 3)]

print(vendas_marco_19)

print(df["LojaID"].value_counts(ascending=False))

#-----------------------------------------------------------------------------------------------

#Visualização de dados

#Grafico de barras

df["LojaID"].value_counts(ascending=False).plot.bar()
plt.show()

#Grafico de barras horizontais
df["LojaID"].value_counts().plot.barh()
plt.show()

df["LojaID"].value_counts(ascending=True).plot.barh()
plt.show()

#Grafico de pizza
df.groupby(df["Data"].dt.year)["Receita"].sum().plot.pie()
plt.show()

#Total de vendas por cidade
print(df["Cidade"].value_counts())

#adicionando um título e alterando o nome dos eixos

df["Cidade"].value_counts().plot.bar(title = "Total vendas pro cidade")
plt.xlabel("Cidade")
plt.ylabel("Total de Vendas")
plt.show()

#Alterando a cor

df["Cidade"].value_counts().plot.bar(title = "Total vendas pro cidade", color="red")
plt.xlabel("Cidade")
plt.ylabel("Total de Vendas")
plt.show()

#Alterando o estilo verificar na documentação do matplotlib
plt.style.use("ggplot")

df.groupby(df["mes_venda"])["Qtde"].sum().plot(title= "Total de produtos vendidos por mês")
plt.xlabel("Mês")
plt.ylabel("Total Produtos Vendidos")
plt.legend()
plt.show()

print(df.groupby(df["mes_venda"])["Qtde"].sum())

#Selecionando apenas as vendas de 2019

df_2019 = df[df["Ano_Venda"]== 2019]

#Total de produtos vendidos por mês

df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum().plot(marker ="v")
plt.xlabel("Mês")
plt.ylabel("Total Produtos Vendidos")
plt.legend()
plt.show()

#histograma

plt.hist(df["Qtde"], color="orangered")
plt.show()

#grafico de dispersão

plt.scatter(x=df_2019["dia_venda"], y = df_2019["Receita"])
plt.show()

#Salvando em png

df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum().plot(marker= "v")
plt.title("Quatidade de produtos vendidos x mês")
plt.xlabel("Mês")
plt.ylabel("Total Produtos Vendidos")
plt.legend()
plt.savefig("grafico QTDE x MES.png")