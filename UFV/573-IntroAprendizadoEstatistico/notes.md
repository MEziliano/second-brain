# Semana I - Intrdução a Estatística Univariada e Multivariada
 O conteúdo temático reúne alguns conceitos importantes para melhor entender os aspectos teóricos da metodologias estatísticas utilizadas na solução de problemas de classificação, predição e reconhecimento de padrões. Nesse semana, você deverá ler o material e escutar as aulas. 

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
$\bar{X} = \dfrac{X_1 + X_2 + ... + X_n}{n} = \dfrac{\sum^n_i X_i}{n}$ 
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

**Medidas de Posição e Dispersão Uni e Multivariada**

**Covariança e Correlação**

**Diagrama de Dispersão**