# Semana 03 - Predição Regresão Linear Simples e Múltipla 

* Introdução
* Regressão Linear Simples
* Modelo, Estimação e Inferência
* Regressão Linear Múltipla
* Modelo, Estimação e Inferência


### Introdução 

* **regressão**: tem por objetivo obter ima relação funcional entre uma variável dependente `(Y)` e uma ou mais variáveis independentes ou explicativas `(X)`. 

* Regressão Simples. 
* Regressão Múltipla. 

## Regressão Linear Simples

### Modelo

<center>

$y_i = \beta_0 - \beta_1X_i + e_i$ 

</center>

em que $y_i$ é o i-ésimo valor variável dependente; $X_i$ é o i-ésimo valor da variável independente; $\beta_0$ é o **intercepto**; $\beta_1$ é o coeficiente angular e; $e_i$ é o erro aleatório. 

O erro representa todas as variações não consideradas no modelo e, além disso é considerado que o mesmo tem a média igual a zero $(E(\varepsilon_1=0))$, vairância constante $(V(\varepsilon_i)=\sigma^2)$ e são não correlacionadaos $(COV(\varepsilon_i, \varepsilon_j)=0)$. 

### Estimação dos Parâmetros $(\beta_0$ e $\beta_1)$ 
#### Método dos Mínimos Quadrados
> Adota como estimatias dos parâmetros, os valores que minizm a soma de quadrados das diferenças entre o observado e o predito pelo modelo ajustado (reta), ou seja, erro. 

<center>

$Z=\displaystyle\sum_{i=1}^n e_i^2 = \displaystyle\sum_{i=1}^n(y_i - \beta_0 - \beta_1 X_i)^2$

</center>

Após algumas álgebras, os estimados dos parâmetros são dados por 

<center>

$\hat{\beta_0} = \bar{y} - \hat{\beta_1} \bar{X} e \hat{\beta_1} = \dfrac{SPD_{XY}}{SQD_{X}}$

</center>

em que: $\bar{y}$ é a média de $Y$; $\bar{X}$ é a média de $X, SPD_{XY}$ $=\displaystyle\sum_{i}X_i Y_i - \dfrac{\sum_i X_i Y_i}{n}$ é a soma do produto dos desvios de $X$ e $Y$ e; $SQD_X = \sum_i X_i ^2 - \dfrac{(\sum_i X_i)^2}{n}$  é a soma dos quadrados dos desvios de $X$. <br>

Agora podemos apresentar o modelo ajustado $\hat{y_i} = \hat{\beta_0} - \hat{\beta_1}X_i$
