# Lista de Execícios Capítulo 04 - Análise Exploratória de Dados
# Análise de Dados com Pandas, Numpy e Matplotlib

# Imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# O dataset contém registros de corridas de táxi
df = pd.read_csv('dados/dataframe.csv', parse_dates = ['Data'], usecols = list(range(0,6)))

# Visualizando os tipos das variáveis
print(df.dtypes)


df.sort_index(inplace = True)
print(df.sample(10))

# Criando uma função para Verificar valores NAN

def sum_nan(df):
    return df.isna().sum()

# Verificando os valores NAN dentro do Dataframe
print(sum_nan(df)) # Existem Valores NAN

# Verificando se esses valores estao presentes nas mesmas linhas
tempo = df['Tempo'].isna()
segundos = df['Segundos'].isna()
minutos = df['Minutos'].isna()
min_por_km = df["Min_Por_Km"].isna()

if ((tempo == segundos).all() & (segundos == minutos).all() & (minutos == min_por_km).all()):
    print("Os valores NaN das colunas estão na mesma linha.")
else:
    print("Os valores NaN das colunas não estão na mesma linha.")


# Verificando o shape do Dataframe
print(df.shape)


# Criando um df com Valores NAN
df_com_nan = df[df.isna().any(axis=1)]

# Criando um Dataframe sem NAN
df_sem_nan = df.dropna(how='any')


#### Respondendo as Perguntas de Negócio ####

# Exercício 1 - Qual o valor máximo da coluna Minutos?
# Observação: Como a coluna Minutos possui valores NAN, vou usar o df_sem_nan.
minuto_max = df_sem_nan["Minutos"].max()
print("O valor máximo da coluna Minutos é: %s" % minuto_max)


# Exercício 2 - Qual o valor mínimo de distância acima de 2.0?
# Observação: Como a coluna Distancia, não possui valores nan, vou usar o dataframe "df"
distancia_max = df.loc[df['Distancia'] > 2, "Distancia"].max()
print("O valor mínimo de distância acima de 2.0 é: %s" % distancia_max)


# Exercício 3 - Crie um plot com a frequência acumulada da coluna Distancia.
distancia = df["Distancia"]

# Cálculo da distribuição cumulativa
p = 1. * np.arange(len(distancia)) / (len(distancia) - 1)

# Plot da distribuição cumulativa
plt.plot(distancia, p)
plt.xlabel("Valores")
plt.ylabel("Probabilidade acumulada")
plt.title("Plot de frequência acumulada da coluna 'Distancia'")
plt.show()


# Exercício 4 - Qual o dia da semana no índice de posição zero?
print(df.iloc[0, 0])


# Exercício 5 - Qual o dia da semana nos índices nas 5 primeiras posições?
print(df.iloc[:6,0])


# Exercício 6 - Extraia todos os dias da semana (em formato texto) e insira em uma nova coluna no dataframe df.
df["Dias_Semana"] = df.Data.map(lambda x: x.strftime("%A"))
print(df.dtypes)


# Exercício 7 - Crie um gráfico de barras com o total da distância percorrida em cada dia da semana.
distancia_dias_semanas = df.groupby("Dias_Semana")["Distancia"].sum().plot(kind = 'bar')
#print(distancia_dias_semanas)


# Exercício 8 - Delete a coluna Tempo do dataframe df.
del df["Tempo"]
print(df.head(5))


# Exercício 9 - Qual o total de corridas de taxi por dia da semana?
total_corridas = df["Dias_Semana"].value_counts()
print(total_corridas)


# Exercício 10 - Qual a média para cada uma das colunas por dia da semana?
medias_corridas_por_dia = df.groupby("Dias_Semana").mean()
print(medias_corridas_por_dia)
