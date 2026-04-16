###Codigos Regressão - Tutorial

#install pandas
import pandas as pd

# Lendo um arquivo txt (formato comum para dados tabulares)
dados = pd.read_csv('C:/Moyses/Research_Moyses/2025/Phyton/dados_exemplo_reg.txt', sep='\t')
print(dados)

# Print the shape of the DataFrame (rows, columns)
print(dados.shape)

# imprime linhas iniciais
print(dados.head())

# cria um resumo  estatístico
print(dados.describe())

#Linear Regression
 
X = dados[['temperatura', 'dias', 'pureza', 'producao']]
y = dados['consumo']

#Correlograma
df = pd.DataFrame(dados)

import seaborn as sns
import matplotlib.pyplot as plt

# Calcular a matriz de correlação
correlation_matrix = df.corr()

# Criar o correlograma usando seaborn
plt.figure(figsize=(10, 8))  # Ajuste o tamanho da figura conforme necessário
sns.heatmap(correlation_matrix,annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Correlograma da Matriz de Correlação')
plt.show()

# Criar o painel de scatter plots para cada par de colunas numéricas
sns.pairplot(df)

# Exibir o gráfico
plt.show()



#pip install statsmodels.api
import statsmodels.api as sm

X = sm.add_constant(X)  # Adiciona o intercepto
mod1 = sm.OLS(y, X).fit()
print(mod1.summary())


#Install formulas
import statsmodels.formula.api as smf
mod2 = smf.ols(formula='consumo ~ temperatura + dias + pureza + producao ', data=df).fit()
print(mod2.summary())

#Acessando elementos
mod1.params
mod1.pvalues
mod1.rsquared


#Modelo de regressão linear simples
X2 = dados[['temperatura']]
X2 = sm.add_constant(X2)
mod2 = sm.OLS(y, X2).fit()
print(mod2.summary())

#Predição de um novo valor
novo = pd.DataFrame({'const':[1], 
                     'temperatura': [51]})

predicao = mod2.predict(novo)
print(predicao)
