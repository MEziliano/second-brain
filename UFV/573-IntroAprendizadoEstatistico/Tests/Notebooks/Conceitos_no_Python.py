# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 15:29:59 2025

@author: m.nascimento
"""



#Vetores e matrizes são frequentemente representados usando a biblioteca numpy

import numpy as np

#Vetor
vetor = np.array([1, 2, 3, 4, 5])
print(vetor)

#Matriz
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matriz)

#Acessar elementos do matriz
vetor[1]
subvetor = vetor[2:4] #Não inclui o 4
print(subvetor)


#Acessar elementos da matriz
#Para acessar um elemento em uma matriz, você especifica o índice da linha e da coluna
elemento = matriz[1, 2]  # elemento será 6 (segunda linha, terceira coluna)
    print(elemento)
    
#Linha inteira
 linha = matriz[0, :]  # linha será [1, 2, 3] (primeira linha)
    print(linha)  

#Coluna Inteira
coluna = matriz[:, 1]  # coluna será [2, 5, 8] (segunda coluna)
    print(coluna)
    
#Submatriz (slicing) 

submatriz = matriz[0:2, 1:3]  # submatriz será [[2, 3], [5, 6]]
print(submatriz)

#Vetor indice
indices_linhas = [0, 2]
    indices_colunas = [1, 2]
    elementos = matriz[indices_linhas, indices_colunas] # elementos será [2, 9]
    print(elementos)


#Dados categóricos podem ser representados usando a biblioteca pandas
import pandas as pd

fator = pd.Series(['A', 'B', 'A', 'C', 'B'])
print(fator)

#DataFrame é uma estrutura de dados tabular em pandas
data = {'col1': [1, 2, 3, 4], 'col2': ['A', 'B', 'C', 'D']}
df = pd.DataFrame(data)
print(df)

#Vetores Indices booleanos

vetor = np.array([1, 5, 2, 8, 3, 7, 4, 6])

# Criar um vetor booleano: True para elementos menores que 5
vetor_booleano = vetor < 5
print("Vetor Booleano:", vetor_booleano)

# Usar o vetor booleano para filtrar o vetor original
elementos_menores_que_5 = vetor[vetor_booleano]
print("Elementos menores que 5:", elementos_menores_que_5)

#Eloementos iguais a 3
elementos_iguais_a_3 = vetor[vetor == 3]
print("Elementos iguais a 3:", elementos_iguais_a_3)

#Elementos dentro de um intervalo
elementos_entre_2_e_6 = vetor[(vetor > 2) & (vetor < 6)]
 print("Elementos entre 2 e 6:", elementos_entre_2_e_6)

#Elementos pares
elementos_pares = vetor[vetor % 2 == 0]
print("Elementos pares:", elementos_pares)


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
colunas = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
iris_df = pd.read_csv(url, header=None, names=colunas)
print(iris_df.head())

# Medidas de posição
# Selecionar apenas as colunas numéricas
numeric_cols = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
mean_values = iris_df[numeric_cols].mean()
print(mean_values)

# Medidas de dispersão
Desv_pad = iris_df[numeric_cols].std()
print(Desv_pad)

var = iris_df[numeric_cols].var()
print(var)

cov = iris_df[numeric_cols].cov()
print(cov)

cor = iris_df[numeric_cols].corr()
print(cor)

#Scarte maiores correlacoes
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))

sns.scatterplot(x='petal_length', y='petal_width', data=iris_df)
plt.title('Scatter Plot entre petal_length e petal_width')
plt.xlabel('petal_length')
plt.ylabel('petal_width')
plt.grid(True)
plt.show()


# Diagrama de dispersão com Seaborn
sns.pairplot(iris_df)
plt.show()

# Diagrama de dispersão com Seaborn
import seaborn as sns
from sklearn.datasets import load_iris
iris = load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
# Diagrama de dispersão com Seaborn
sns.pairplot(iris_df, hue='species')
plt.show()

# Diagrama de dispersão com Seaborn
sns.pairplot(iris_df)
plt.show()

#Grafico de barras

Python



import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Carregando o dataset Iris
iris = sns.load_dataset('iris')

# Selecionando apenas as colunas numéricas para análise
numeric_cols = iris.select_dtypes(include=np.number).columns

# Criando subplots para cada variável numérica
num_cols = len(numeric_cols)
fig, axes = plt.subplots(1, num_cols, figsize=(15, 5))

# Iterando sobre cada variável numérica para criar o gráfico de barras com erro padrão
for i, col in enumerate(numeric_cols):
    media_geral = iris[col].mean()
    erro_padrao_geral = iris[col].sem()
    axes[i].bar([col], [media_geral], yerr=[erro_padrao_geral], capsize=10, color='skyblue', edgecolor='black')
    axes[i].set_ylabel('Média')
    axes[i].set_title(f'Média de {col} com Erro Padrão')
    axes[i].grid(axis='y', linestyle='--')
    axes[i].tick_params(axis='x', rotation=45, ha='right')
    axes[i].set_ylim(0, iris[col].max() + iris[col].sem() * 2) # Ajusta o limite y

plt.tight_layout()
plt.show()
