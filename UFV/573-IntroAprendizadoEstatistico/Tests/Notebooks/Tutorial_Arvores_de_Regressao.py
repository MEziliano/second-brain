# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 07:54:50 2025

@author: m.nascimento
"""

import pandas as pd
from sklearn.datasets import fetch_openml

# Carregar o conjunto de dados Boston (alternativa para versões recentes do scikit-learn)
boston = fetch_openml(name='boston',  as_frame=True)
dados = boston.data
boston.data
dados['MEDV'] = boston.target
boston.target
# Exibe as primeiras linhas do DataFrame
print(dados.head())

#Treinamento e validação e ajuste do modelo
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
from sklearn.model_selection import cross_val_score
import numpy as np

# Particionar o conjunto de dados (Treinamento e validação)
X_train, X_test, y_train, y_test = train_test_split(dados.drop('MEDV', axis=1), dados['MEDV'], test_size=0.2, random_state=1)

#Ajuste de uma Árvore alterando valores defalt.
mod1 = DecisionTreeRegressor(random_state=1, min_samples_leaf=5,  min_samples_split=20,  max_depth=4)
mod1.fit(X_train, y_train)

# Resumo (Apenas uma variável foi utilizada na construção da árvore)
print(mod1) #sklearn nao tem summary igual ao R.
print("Features importantes: ", mod1.feature_importances_) #features importantes
print(dados.columns)

# Criar o DataFrame com as importancias: [:-1] significa "selecione todos os elementos da sequência, exceto o último".
imp = pd.DataFrame({'Feature': dados.columns[:-1], 'Importance': mod1.feature_importances_})

# Imprimir o DataFrame
print(imp)

# Apresentação da árvore ajustada
plt.figure(figsize=(20, 10))
plot_tree(mod1, filled=True, feature_names=X_train.columns)
plt.show()



####Poda
# Poda da árvore (em python a poda é feita com ccp_alpha)
path = mod1.cost_complexity_pruning_path(X_train, y_train)
ccp_alphas, impurities = path.ccp_alphas, path.impurities

# Encontrar o melhor ccp_alpha (equivalente ao best=6 no R)
best_ccp_alpha = ccp_alphas[np.argmin(impurities)] #encontra o alpha com o menor impurity
best_ccp_alpha
mod_poda = DecisionTreeRegressor(random_state=1, ccp_alpha=best_ccp_alpha, min_samples_leaf=5,  min_samples_split=20,  max_depth=4)
mod_poda.fit(X_train, y_train)

# Apresentação da árvore podada
plt.figure(figsize=(20, 10))
plot_tree(mod_poda, filled=True, feature_names=X_train.columns)
plt.show()

# Predição (Considerando o modelo sem poda)
yhat = mod1.predict(X_test)
boston_test = y_test

# Calcular o RMSE (Raiz do Erro Quadrático Médio)

from sklearn.metrics import mean_squared_error
RMSE = np.sqrt(mean_squared_error(boston_test, yhat))
print("RMSE:", RMSE)

#Estudo de validacao cruzada.

cv_scores = cross_val_score(mod1, X_train, y_train, cv=10, scoring='neg_mean_squared_error') #cross validation
cv_mse = -cv_scores #pega o valor positivo do mse
plt.plot(range(1, 11), cv_mse, marker='o') #plota os valores do cross validation
plt.xlabel('Fold')
plt.ylabel('MSE')
plt.title('Cross-Validation MSE')
plt.show()

print("Média do MSE:", np.mean(cv_mse)) #imprime a média do mse
print("Desvio padrão do MSE:", np.std(cv_mse)) #imprime o desvio padrão do mse

#Bagging
from sklearn.ensemble import RandomForestRegressor

# Bagging using RandomForestRegressor (mtry=13 means all features)
mod_bag = RandomForestRegressor(n_estimators=100, max_features=13, random_state=1) # random_state for reproducibility
mod_bag.fit(X_train, y_train)

# Model evaluation (Prediction)
yhat_bag = mod_bag.predict(X_test)
RMSE_bag = np.sqrt(mean_squared_error(y_test, yhat_bag))

print(mod_bag)
print(f"RMSE_bag: {RMSE_bag}")

#Random Forest
mod_rf = RandomForestRegressor(n_estimators=100, max_features=4, random_state=1)
mod_rf.fit(X_train, y_train)

# Predictions
yhat_rf = mod_rf.predict(X_test)

# RMSE
RMSE_rf = np.sqrt(mean_squared_error(y_test, yhat_rf))
print(f"RMSE_rf: {RMSE_rf}")

# Criar DataFrame com os valores de RMSE
rmse_data = {
    'Modelo': ['Regression Tree','Bagging', 'Random Forest'],
    'RMSE': [RMSE, RMSE_bag, RMSE_rf]
}

rmse_df = pd.DataFrame(rmse_data)

print(rmse_df)

# Feature Importance for Bagging
i_mod_bag = mod_bag.feature_importances_
print("Feature Importance:")
for feature, importance in zip(X_train.columns, i_mod_bag):
    print(f"{feature}: {importance}")

# Variable Importance Plot
feature_importance = pd.Series(i_mod_bag, index=X_train.columns)
feature_importance.nlargest(13).plot(kind='barh')  # 13 features in Boston dataset
plt.title("Variable Importance")
plt.show()








#Esquemas de Validação

X = dados.drop('MEDV', axis=1)
y = dados['MEDV']

# Holdout
X_train_holdout, X_test_holdout, y_train_holdout, y_test_holdout = train_test_split(X, y, test_size=0.2, random_state=1)

mod_bag.fit(X_train_holdout, y_train_holdout)
yhat_bag_holdout = mod_bag.predict(X_test_holdout)
RMSE_bag_holdout = np.sqrt(mean_squared_error(y_test_holdout, yhat_bag_holdout))

mod_rf.fit(X_train_holdout, y_train_holdout)
yhat_rf_holdout = mod_rf.predict(X_test_holdout)
RMSE_rf_holdout = np.sqrt(mean_squared_error(y_test_holdout, yhat_rf_holdout))

# K-Fold Cross-Validation
from sklearn.model_selection import train_test_split, KFold, LeaveOneOut

kf = KFold(n_splits=5, shuffle=True, random_state=1)

RMSE_bag_kfold = [] #Listas vazias para armazenar os valores de RMSE
RMSE_rf_kfold = []

for train_index, test_index in kf.split(X):
    X_train_kfold, X_test_kfold = X.iloc[train_index], X.iloc[test_index]
    y_train_kfold, y_test_kfold = y.iloc[train_index], y.iloc[test_index]

    mod_bag.fit(X_train_kfold, y_train_kfold)
    yhat_bag_kfold = mod_bag.predict(X_test_kfold)
    RMSE_bag_kfold.append(np.sqrt(mean_squared_error(y_test_kfold, yhat_bag_kfold)))

    mod_rf.fit(X_train_kfold, y_train_kfold)
    yhat_rf_kfold = mod_rf.predict(X_test_kfold)
    RMSE_rf_kfold.append(np.sqrt(mean_squared_error(y_test_kfold, yhat_rf_kfold)))

RMSE_bag_kfold = np.mean(RMSE_bag_kfold)
RMSE_rf_kfold = np.mean(RMSE_rf_kfold)

# Jackknife (Leave-One-Out Cross-Validation)
loo = LeaveOneOut() #Criamos um objeto LeaveOneOut. 

RMSE_bag_jackknife = [] #Listas vazias para armazenar os valores de RMSE
RMSE_rf_jackknife = []

for train_index, test_index in loo.split(X):
    X_train_jackknife, X_test_jackknife = X.iloc[train_index], X.iloc[test_index]
    y_train_jackknife, y_test_jackknife = y.iloc[train_index], y.iloc[test_index]

    mod_bag.fit(X_train_jackknife, y_train_jackknife)
    yhat_bag_jackknife = mod_bag.predict(X_test_jackknife)
    RMSE_bag_jackknife.append(np.sqrt(mean_squared_error(y_test_jackknife, yhat_bag_jackknife)))

    mod_rf.fit(X_train_jackknife, y_train_jackknife)
    yhat_rf_jackknife = mod_rf.predict(X_test_jackknife)
    RMSE_rf_jackknife.append(np.sqrt(mean_squared_error(y_test_jackknife, yhat_rf_jackknife)))

RMSE_bag_jackknife = np.mean(RMSE_bag_jackknife)
RMSE_rf_jackknife = np.mean(RMSE_rf_jackknife)

# DataFrame com os resultados
rmse_data = {
    'Modelo': ['Bagging', 'Random Forest'],
    'Holdout': [RMSE_bag_holdout, RMSE_rf_holdout],
    'K-Fold': [RMSE_bag_kfold, RMSE_rf_kfold],
    'Jackknife': [RMSE_bag_jackknife, RMSE_rf_jackknife]
}

rmse_df = pd.DataFrame(rmse_data)

print(rmse_df)
