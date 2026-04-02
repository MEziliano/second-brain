# [TEORICA] Semana 03 - Predição Regresão Linear Simples e Múltipla 

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

> Qualidade do ajuste
$$
r^2 = \hat{\beta_1} \dfrac{SPD_{XY}}{SQD_Y} = \dfrac{SQ \text{Regressão}}{ SQ \text{Total}} [ 0 \le r^2 \le 1]
$$

Quanto mais próximo a 1 (ou a 100%) melhor o ajuste do modelo. 

### Modelo (Forma Matricial)

$$
Y = X\beta + \epsilon
$$

em que $Y$ é um vetor de dimensão $n \times 1$; $X$ uma matriz de dimensão $ n \times (p+1)$, $\beta$ um vetor de dimensão $(p+1) \times 1$ e, $\epsilon$ um vetor de dimensão $n\times 1$, dados por:

$$
 
\begin{bmatrix}
   Y_1  \\
   Y_2 \\
   \vdots \\
   Y_n 
\end{bmatrix} = 

\begin{bmatrix}
   X_{11} & X_{21} & \dots &  X_{p1} \\
   X_{12} & X_{22} & \dots &  X_{p2} \\
    \vdots & \vdots & \dots & \vdots \\
    X_{1n} & X_{2n} & \dots &  X_{pn} \\
\end{bmatrix}

\begin{bmatrix}
   \beta_{1}  \\
   \beta_{2} \\
   \vdots \\
   \beta_{n} 
\end{bmatrix} +

\begin{bmatrix}
   \epsilon_{1}  \\
   \epsilon_{2} \\
   \vdots \\
   \epsilon_{n} 
\end{bmatrix}

$$

#### Estimação do Vetor de Parâmetros ($\beta$)

**Método dos Mínimos Quadrados**

Da mesma forma que anteriormente, adota-se como estimativas dos parâmetros, os valores que minizam a soma de quadrados das diferenças entre o observado e o predito pelo modelo ajustado (reta), ou seja, o erro. 

$$

Z = _\epsilon T \epsilon = (Y, X\beta)^T (Y - X\beta)

$$

Após algumas álgebras, o estimador do vetor de parâmetros é dados por:

$$

\hat\beta = (X^TX)^{-1}X^TY
$$

em que $(X^TX)^{-1}$ é a inversa da matriz $X^T$

Agora podemos apresentar o mdeolo ajustado $\hat{Y} = X\hat\beta$


#### Estimação $(\sigma^2)$

Obtido pela decomposição da soma de quadrados dos resíduos $(SS_R)$:

$$

\sigma^2 = \dfrac{SS_R}{gl(SS_R)}
$$

em que $SS_R$ é a soma de Quadrados dos resíduos $(SS_R = Y^TY - \hat\beta^TX^TY)$. O número de graus de liberdade é $n-(p+1)$ visto que para obtenção da $SS_R$ são necessários estimar $p+1$ parâmentros. 

#### Inferências a respeito dos parâmentros 

**Hipótese ($\beta_j$)**


$$
\begin{cases}
   H_0: \beta_j = 0  \\
   H_1: \beta_j  \not = 0
\end{cases}


$$
> Estatística de teste
$$

t = \dfrac{\hat{\beta_j} - \beta_{j}}{ \sqrt{\sigma^2C_{jj}}}

$$

em que $C_{jj}$ é o elemento na posição $jj$ da matriz $X^TX$. Especificamente, $V(\beta_j) = \hat{\sigma^2} C_{jj}$


## Regressão Linear Múltipla 

**Decisão do Teste**

Se $|t| > t_{(\alpha/2; n-(p+1))}$, rejeitamos $H_0$ em que $t_{(\alpha/2; n-(p+1))}$ é o quantil $(1- \alpha /2)$ da distribuição de Student com $n- (p+1)$ graus de liberdade. 

### Coeficiente de Determinação Múltipla

**Qualidade do Ajuste**
$$
R^2 = \dfrac{SQ \text{Regressão}}{SQ \text{Total}} = \dfrac{\hat\beta X^TY}{Y^TY} [0 \le R^2 \le 1]
$$

Quanto mais próximo a 1 (ou a 100%) melhor o ajuste do modelo. 

### Coeficiente de Determinação Múltipla Ajustado

Quando maior p maior seu valor.

$$
\bar{R}^2 = \dfrac{R^2 (n-1) - p}{n-1 -p} [0 \le R^2 \le 1]

$$

Quanto mais próximo a 1 (ou a 100%) melhor o ajuste do modelo. 


# [PRÁTICA] - Semana 03 - Predição Regresão Linear Simples e Múltipla 

[VIDEO](https://drive.google.com/file/d/1Yvp2dna_ozTGXqewLp5oi6rUCKAFbkEE/view?usp=sharing)

[VIDEO](https://www.youtube.com/watch?v=nA-FwoF2sss)