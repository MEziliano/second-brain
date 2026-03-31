# Semana I - Intrdução a Estatística Univariada e Multivariada
 O conteúdo temático reúne alguns conceitos importantes para melhor entender os aspectos teóricos da metodologias estatísticas utilizadas na solução de problemas de **classificação, predição e reconhecimento de padrões**. Nesse semana, você deverá ler o material e escutar as aulas. 

Nesta semana, além da apostila da disciplina o aluno pode consultar o roteiro de aulas de Iniciação à Estatística disponível no link abaixo. Esse material é parte da disciplina EST 105 da Universidade Federal de Viçosa a qual sou professor a 15 anos. Especificamente, a consulta deve ser ao Capítulo 2 que aborda Estatística Descritiva. Nesse material, além das medidas apresentadas nos slides são encontradas outras medidas de posição e dispersão. É importante ressaltar que para o entendimento das metodologias multivariadas de aprendizado estatístico o pesquisador deve entender os conceitos de média, variância, covariância e correlação.

----
**Introdução** 

O que é ciência estatística? É um ramo da matemática que se debruça sobre os dados. Buscando a *coleta, a organização, apresentação, análise e interpretação*  de forma que auxilie na tomada de decições. 
Um dos principais conceitos estatísticos é a diferencição entre **População e Amostra**.
* **População**: Conjunto de indivíduos/objetos que apresentam pelo menos uma característica em comum.
* **Amostra**: Subconjunto da população. 

Dentro da estatística existe uma divisão entre dois principais focos, sendo elas: a estatística descritiva e a estatística inferencial. 

A estatística descritiva visa a resumir os dados obtidos após a amostragem. Utiliza de medidas descritivas. Essas conclusões são válidas apenas para a amostra de dados que estão sendo estudadas.   

Já a estatística inferencial utiliza de conjuntos de técnicas que possibilitam extrapolar os resultados obtidos em um subconjunto de dados (**amostra representativa**)para um conjunto maior (**população**).  

## **Estatística descritiva univariada**

### Medidas de Posição

Também conhecido como *medidas de tendência central*, são medidas que ajudam a compreender um ponto em comum a todos os dados. Geralmente, um ponto central, por isso o nome medidas de tendência central. **Exemplo**: *Média aritmética,* média ponderada, mediana, moda… <br>
<center>

$\bar{X} =\dfrac{X_1 + X_2 + ... + X_n}{n}=\dfrac{\sum^n_i X_i}{n}$ 

</center>

### Medidas de Disperção
Buscam compreender o grau variabilidade das observações de um conjunto de dados. Exemplo:  *<u>Variância</u>, <u>Desvio padrão</u>, <u>Quartis</u>*… 

<center>

$s^2_X = V(X) = \dfrac{\sum^n_{i=1} (X_i - \bar{X})²}{n-1} = \dfrac{\sum^n_{i=1} - \dfrac{\sum^n _{i=1} X_i} {n})²}{n-1}$ 

$S_x = \sqrt{s²_X}$

</center>

## **Estatística descritiva multivariada**
**Medidas de Posição**
* Vetor de Médias
<center>

$Y _{4 X 3} = \begin{bmatrix}
   7 & 9  & 9 \\
   4 & 6 & 11 \\
   4 & 2 & 5 \\
   5 & 5 & 7
 \end{bmatrix} $

</center>

Seja uma amostra aleatória onde $Y_1, Y_2, ..., Y_j, ..., Y_n$, então a média amostral é definida por:

<center>

$\bar{Y} = \dfrac{1}{n} \lbrack \displaystyle\sum_{j=1}^n Y_j
        \rbrack = \dfrac{1}{n} Y^T 1  = \begin{bmatrix}
\bar{Y}_1 \\
\bar{Y}_2 \\
\vdots\\
\bar{Y}_p \\
\end{bmatrix}$

</center>
 
**Medidas de Dispersão e Associação**

- Matriz de Variâncias e covariâncias;

- Matriz de Correlação;

# Semana II - Conceitos Estatísticos no Python 

**Fundamentos do Python** 

```python
peso = 60.5
peso
>> 60.5
```

**Vetores no Python** 🐍

- Armazena conjunto de valores do mesmo tipo sob um mesmo nome;
- Em geral usando a biblioteca numpy: `import numpy as np`
- Para criar vetores usaremos `np.array([])` para indicar ao Python os elementos que formam o vetor separando-os por vírgulas. Por exemplo:
```python
peso = np.array([60.5, 70, 69.8, 101.20])
print(peso)
>> [60.5, 70, 69.8, 101.20]
```


**Matrizes no Python** 🎲 

São vetores com propriedade especial, que e é a dimensão;

- Exemplo: Suponha que temos oito números que correspondem as produções, em kg, de 2 genótipos em 4 ambientes.

```python
matriz = np.array([[10, 14,9, 23], [42, 11, 13, 54]])
print(matriz)
>> [[10, 14, 9, 23]
    [42, 11, 13, 54]]
```

**Dataframes**
Objeto utilizado para armazenar tabelas.
```python
import pandas as pd 
```

Exemplo de criação de um dataframe:

```python
print(notas_inform)
>>          mat     turma     notas
>> 0        2355        t1      10.3
>> 1        3456        t2      93
>> 2        2334        t3      14.2
>> 3        5456        t6      15.2
```
- Acessando os elementos de um datafram

```python
elemento = notas_inform.iloc[1, 1]
print(f"notas.inform[2, 2]: {elemento}")
notas.inform[2, 2] : t2
coluna_mat = notas_inform['mat']
print(f"notas.inform mat:\n{coluna_mat.to_list()}")
notas.inform[mat]:
[2355, 3456, 2334, 5456]
```

**Vetores Índices booleanos**
- Podemos criar vetores índices para acessar elementos dos
objetos.
- Exemplo: Vetor índice.
```python 
vetor = np.array([1, 5, 2, 8, 3, 7, 4, 6])
vetor_booleano = vetor < 5
print("Vetor Booleano:", vetor_booleano)
Vetor Booleano: [ True False True False True False True]

elementos_menores_que_5 = vetor[vetor_booleano]
print("Elementos menores que 5:", elementos_menores_que_5)
Elementos menores que 5: [1 2 3 4]
``` 
## Medidas Descritivas

**Medidas de Posição e Dispersão Uni e Multivariada**

```python
numeric_cols = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
mean_values = iris_df[numeric_cols].mean()
print(mean_values)
sepal_length 5.843333
sepal_width 3.054000
petal_length 3.758667
petal_width 1.198667
dtype: float64


Desv_pad = iris_df[numeric_cols].std()
print(Desv_pad)
sepal_length 0.828066
sepal_width 0.433594
petal_length 1.764420
petal_width 0.763161
dtype: float64

var = iris_df[numeric_cols].var()
print(var)
sepal_length 0.685694
sepal_width 0.188004
petal_length 3.113179
petal_width 0.582414
dtype: float64


numeric_cols = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
mean_values = iris_df[numeric_cols].mean()
print(mean_values)
sepal_length 5.843333
sepal_width 3.054000
petal_length 3.758667
petal_width 1.198667
dtype: float64
```

**Diagrama  de Disperção**
```python

cor = iris_df[numeric_cols].corr()
print(cor)
              sepal_length  sepal_width   petal_length   petal_width
sepal_length  1.000000     -0.109369      0.871754      0.817954
sepal_width  -0.109369      1.000000     -0.420516     -0.356544
petal_length  0.871754     -0.420516      1.000000      0.962757
petal_width   0.817954     -0.356544      0.962757      1.000000
```


**Covariança e Correlação**

**Diagrama de Dispersão**