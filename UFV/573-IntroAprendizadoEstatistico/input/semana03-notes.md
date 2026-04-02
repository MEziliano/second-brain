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


#### Estimação de ($\sigma^2$)
> Obtido pela decomposição da soma de quadrados dos resíduos ($SS_R$):


$$
\sigma^2 = \dfrac{SS_R}{gl(SS_R)}
$$

em que $SS_R$ é a **Soma de Quadrados dos resíduos** ($SS_R  =\displaystyle\sum^n_{i=1} \hat{e}^2_i$).

O número de graus de liberdade é $n-2$ visto que para a obtenção da $SS_R$ são necessários estimar dois parâmetros no modelo de regressão. 

#### Inferências a respeito dos parâmentros ($\beta_0$ e $\beta_1$)

Adicionar a suposição de Normalidade aos erros ($e_i  \overset{iid}{\sim} N(0, \sigma^2)$).
Desta forma, pelo teorema da combinação linear $Y_i$ também é normal e consequentemente os estimadores dos parâmetros também são normalmente distribuídos, ou seja:

$\hat{\beta_1} \text{\textasciitilde} N \left(\beta_1, \dfrac{\sigma^2}{SQD_x} \right)$ e $\hat{\beta_0} \text{\textasciitilde} N \left[\beta_o, \sigma^2 \dfrac{1}{n} + \dfrac{\bar{X}^2}{SQD_2} \right]$ 

#### Hipóteses $(\beta_0)$

$$
\begin{cases}
   H_0: \beta_1 = \beta_{10}  \\
   H_1: \beta_1  \not = \beta_{10}
\end{cases}
$$

**Estatística de teste**

$$

t = \dfrac{\hat{\beta_1} - \beta_{10}}{ \sqrt{\dfrac{\sigma^2}{SQD_X}}}

$$

**Decisão do teste**

Se $|t| > t_({\alpha / 2 ; n-2})$, rejeitamos $H_0$, em que $tt_({\alpha / 2 ; n-2})$ é o quantil $(1 - \alpha/2)$ da distribuição t de Student com $n-2$ graus de liberdade. 

#### Coeficiente de Determinação
