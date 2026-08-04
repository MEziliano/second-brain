# Semana 02 - Introdução às Redes Neurais

## Aula 01 - Introdução às Redes Neurais Artificiais

### Representação dos neurônios biológicos

As RNAs(Redes Neurais Artificiais) servem para imitar o neurônio humano. Não sendo concorrentes das demais arquiteturas já vistam em se tratando de Aprendizado de Máquina.

O percpetron é a representação mais simples de uma RNA (rede neural artificial). Contando apenas com uma saída. Um dos grandes pontes do perceptron é o ajuste de pesos da função.

#### Ajuste de um modelo perceptron

É a fase de treinamento da RNA.

* Ajuste de parâmtros = Fase de Treinamento
* $X^{(k)}$: vetor de entrada da amostra $k$
* $d^{(k)}$: valor desejado para $y$
* $W$: vetor de pesos sinápticos
* $b$: limiar de ativação do perceptron

$$
\begin{cases}
   W^{atual} = W^{anterior} + \eta+(d^{(k)} - y)^{X^{(k)}}\\
   W^{atual} = W^{anterior} + \eta+(d^{(k)} - y)(-1)
   
\end{cases}
$$

* $\eta$: taxa de aprendizagem do treinamento
* $0<\eta<1$
* Geralmente valores entre 0,01% a 10%

### Início do treinamento -  Perceptron:

1. Carregar o conjunto de treinamento para a matriz $𝑋$;
2. Carregar o conjunto de saídas desejadas para o vetor $𝑑$;
3. Concatenar a coluna de valores -1 à matriz $X$, representando a entrada para o $𝑏𝑖𝑎𝑠$;
4. Atribuir valores aleatórios normalizados aos pesos sinápticos $𝑊$, lembrando que $𝑏$ está no vetor $𝑊$;
5. Escolher o valor da taxa de aprendizado $\eta$;
6. Determine o número máximo de épocas de treinamento $𝑒𝑝𝑜𝑐𝑎_{max}$;

### Treinamento de um percpetron

7. Iniciar o contador de épocas do treinamento $(𝑒𝑝𝑜𝑐𝑎 = 0)$;
8. Faça até que $𝑒𝑟𝑟𝑜 = 0$:

   1. Atribua $𝑒𝑟𝑟𝑜 = 0$;
   2. Para cada amostra de treinamento ${𝑋^{(k)}, 𝑑{(k)}}$ 
      2.1. Faça $𝑢 = 𝑋{(k)}𝑊$; 
      2.2. Faça $𝑦 = 𝑠𝑖𝑛𝑎𝑙 (𝑢)$ ; 
      2.3. Se $𝑦 ≠ 𝑑{(k)}$ : 
      a) Faça $𝑊^{atual} = 𝑊^{anterior} + 𝜂(𝑑^{(k)} − 𝑦)𝑋()$; 
      b) Atribua $𝑒𝑟𝑟𝑜 = 1$;
      8.3. Faça $𝑒𝑝𝑜𝑐𝑎 = 𝑒𝑝𝑜𝑐𝑎 + 1$;
      8.4. Se $𝑒𝑝𝑜𝑐𝑎 > 𝑒𝑝𝑜𝑐𝑎_{max}$, pare o treinamento.
      **Fim do treinamento – Perceptron**

### Operação de um perceptron

**Início da fase de operação:**

1. Carregar o vetor de amostra $𝑋$;
2. Concatenar o valor $-1$ à matriz $X$, representando a entrada para o $𝑏𝑖𝑎𝑠$;
3. Carregar o vetor de pesos resultante do treinamento $𝑊$, lembrando que $𝑏$ está no vetor $𝑊$;
4. Faça $𝑢 = 𝑋^{(k)} 𝑊$;
5. Faça $𝑦 = 𝑠𝑖𝑛𝑎𝑙(𝑢)$;
6. Se $𝑦 > 0$:
   1. A amostra $X$ pertence à classe A;
7. Caso contrário:
   1. A amostra X pertence à classe B;
      **Fim da fase de operação.**

### Considerações finais

* Fase de treinamento:
* $𝑒𝑟𝑟𝑜 = 𝑑^{(k)} − 𝑦$
* $𝑦 = 𝑠𝑖𝑛𝑎𝑙(𝑢)$
* Não realiza ajuste fino dos parâmetros do perceptron
* Limitado a problemas de classificações binárias
* Não separa classes não linearmente separáveis

## Aula 02 - Adaline e a Regra Delta

### Otimização de parâmetros do perceptron

**Limitação de um perceptron**

* Ajuste não é feito de maneira ótima
* Converge para qualquer parâmetro que solucione a classificação
* Solução depende do ponto de inicialização dos parâmetros
* Mudar a forma de calcular o erro
* Próprio valor da inferência
* Função de ativação recebe entrada mais próxima da saída

### Cálculo do gradiente descendente (LMS)

* Cálculo do erro:
  $
  \text{erro} = d - u
  $
* LMS:

$$
E(W) = \dfrac{1}{2} \sum^{p}_{k=1} (d^{(k)} - u)^2 = E(W)  \dfrac{1}{2} \sum^{p}_{k=1} (d^{(k)} - X^{(k)}W)^2
$$

* Objetivo:
  * Minimizar $E(W)$
  * Ajustando os valores de $W$
* Gradiente do erro quadrático médio:

$$
\nabla E(W) = \dfrac{\partial E(W)}{\partial W} = - \sum^{p}_{k=1} (d^{(k)} -u)X^{(k)}
$$

* Resultado no ajuste de pesos:

$$
\Delta W = - \eta \nabla E(W) = \eta \sum^{p}_{k=1} (d^{(k)} - u)X^{(k)} \implies W^{atual} = W^{anterior} + \eta \sum^{p}_{k=1} (d^{(k)} u)X^{(k)}
$$

### Algoritmo de treinamento do Adaline

**Início do treinamento – Adaline (com regra Delta):**

1. Carregar o conjunto de treinamento para a matriz $𝑋$ com a entrada do limiar −1;
2. Carregar o conjunto de saídas desejadas para o vetor $𝑑$;
3. Atribuir valores aleatórios normalizados aos pesos sinápticos $𝑊$ (com o $𝑤_0$);
4. Escolher o valor da taxa de aprendizado $\eta$ e para o limar de precisão $\epsilon$;
5. Determine o número máximo de épocas de treinamento $𝑒𝑝𝑜𝑐𝑎_{max}$;
6. Iniciar o contador de épocas do treinamento $(𝑒𝑝𝑜𝑐𝑎 = 0)$;
7. Faça até que $𝐸𝑄𝑀 𝑊^{atual} − 𝐸𝑄𝑀 (𝑊^{anterior}) ≤ 𝜀$:
   1. Faça $𝐸𝑄𝑀 𝑊^{atual} − 𝐸𝑄𝑀 (𝑊^{anterior})$;
   2. Faça $𝐸𝑄𝑀 𝑊^{atual} = 0$;
   3. Para cada amostra de treinamento ${𝑋^{(k)}, 𝑑^{(k)}}$, faça:
      1. $𝑢 = X^{(k)}W$;
      2. $𝐸𝑄𝑀 𝑊^{atual} = 𝐸𝑄𝑀 (𝑊^{atual})+ d^{(k)- u^2}$;
      3. $𝑊^{atual} = 𝑊^{anterior} + \eta(d^{(k)}- u )X^{(k)}$
   4. Faça $𝐸𝑄𝑀 𝑊^{atual} = ^{EQM(W^{atual})}/p$;
   5. Faça $𝑒𝑝𝑜𝑐𝑎 = 𝑒𝑝𝑜𝑐𝑎 + 1$;
   6. Se $𝑒𝑝𝑜𝑐𝑎 > 𝑒𝑝𝑜𝑐𝑎_{max}$ , pare o treinamento.
      **Fim**

### Considerações finais

* Adaptive linear neuron
  * Problemas de classificação linearmente separáveis
  * Aproximador de função linear
* Não é capaz:
  * Problemas de classificação não linearmente separável
  * Aproximar funções não lineares
* Perceptron multicamadas (PMC)

## Aula 03 - Rede Perceptron Multicamadas

### Problemas não lineares

* Problemas de classificação e estimação
  * Topologias lineares
  * Perceptron e Adaline
* Problemas com topologias mais complexas (não lineares)
* Rede Perceptron Multicamadas (PMC)
  * Elementos lineares
  * Ferramentas de otimização
  * Compõem estruturas complexas
* Problema é dividido em várias partes lineaers
* Resolvido por cada perceptron da PMC

### Perceptron

 ![Perceptrom MultiCamadas](.\Docs\images\PMC.png)

### Aplicação do ***backpropagation***

* **Erro médio quadrático**

$$
$
$$

E(k)= \frac{1}{2} \sum^{m}_{j=1} (d_j(k) - y_j^{Lm})^2

$$
$
$$

* **Erro Médio pelo total de amostras:**

$$
$
$$

EQM = \frac{1}{p} \sum^{p}_{k=1} E(k)

$$
$
$$

* **Atualizando os pesos da última camada**

$$
$
$$

W_j^{(Lm)}(t+1) = W_j^{(Lm)}(t) + \eta \delta_j^{(Lm)} y_j^{(LM-1)} \\\delta_J^{(Lm)} = (d_j - y_j^{(LM)})g'(I_j^{(Lm)})

$$
$
$$

* **Atualizando os pesos das camads intermediárias**

$$

$$

W_j^{(L)}(t+1) = W_j^{(L)}(t) + \eta \delta_j^{(L)} y_j^{(L-1)} \\\delta_J^{(L)} = (d_j - y_j^{(LM)})g'(I_j^{(L)})

$$
$
$$

* **Atualizando os pesos da primeira camada**

$$

$$

W_j^{(1)}(t+1) = W_j^{(1)}(t) + \eta \delta_j^{(1)}x_i  \\\delta_J^{(L)} = (d_j - y_j^{(LM)})g'(I_j^{(L)})

$$
$
$$

### Alogritmo de treinamento do PMC

**Início – Fase de treinamento – Rede Perceptron Multicamada:**

1. Carregar o conjunto de treinamento para a matriz $𝑋$ com a entrada do limiar −1;
2. Carregar o conjunto de saídas desejadas para o vetor $𝑑$;
3. Atribuir valores aleatórios e normalizados aos pesos sinápticos $𝑊$ (com o $𝑤$,) de todas as
   camadas da rede;
4. Escolher o valor da taxa de aprendizado $\eta$ e para o limar de precisão $\epsilon$;
5. Determine o número máximo de épocas de treinamento $𝑒𝑝𝑜𝑐𝑎_{max}$;
6. Iniciar o contador de épocas do treinamento (𝑒𝑝𝑜𝑐𝑎 = 0);
7. Faça até que $| EQM^{atual} - EQM^{anterior}| \le \epsilon$
   1. Faça $EQM^{anterior} = EQM^{atual}$
   2. Para todas as amostras de treinamento $\lbrace X^{(k)}, d^{(k)}$, faça
      1. Calcular o valor de $I_k^{(1)}$ e $y_i^{(1)}$ para a primeira camada;
      2. Calcular o valor de $I_k^{(L)}$ e $y_i^{(L)}$ para as camdas intermediárias;
      3. Calcular o valor de $I_k^{(LM)}$ e $y_i^{(LM)}$ para a última camada;
      4. Calcular o valor de $\delta_j^{(LM)}$ para a última camada;
      5. Atualizar o valor de $W_j^{(LM)}$ para a última camada;
      6. Calcular o valor de $\delta_j^{(L)}$ e atualizar $W_j^{(L)}$ para as camadas intermediárias;
      7. Calcular o valor de $\delta_j^{(1)}$ para a primeira camada;
      8. Atualizar o valor $W_j^{(1)}$ para a primeira camada;
   3. Calcular o valor de $y_k^{(LM)}$;
   4. Calcular o erro $EQM^{atual}$;
   5. Faça $epoca = epoca+1$;
   6. Se $epoca >_{max}$, pare o treinanmento

### Algoritmo de operação do PMC

**Início – Fase de operação – Rede Perceptron Multicamada:**

1. Carregar o vetor de amostra $𝑋$;
2. Concatenar o valor -1 à matriz X, representando a entrada para o 𝑏𝑖𝑎𝑠;
3. Carregar o vetor de pesos resultante do treinamento 𝑊 de todas os neurônios e todas as
   camadas;
4. Calcular o valor de  $I_j^{(1)}$ e $y_j^{(1)}$ para a primeira camada;
5. Calcular o valor de  $I_j^{(L)}$ e $y_j^{(L)}$ para todas as camadas intermediárias;
6. Calcular o valor de  $I_j^{(LM)}$ e $y_j^{(LM)}$ para a última camada;
7. Disponibilizar a saída da rede de acordo com os valores de  $y_j^{(LM)}$

### Considerações Finais

**Algoritmo de backpropagation**

* Realiza atualizações nos parâmetros
* Dependendo do tamanho do banco de dados e da complexidade da rede
* Pode ser lento e custoso computacionalmente
  **Outras configurações de backpropagation e métodos de atualização de parâmetros**
* Momentum
* Levenberg-Marquardt
* Gradiente descendente estocástico
  **Perceptron multicamadas (PMC)**
* Combina funções dos elementos mais simples
* Treinamento pode necessitar de refinamento para ser eficiente e com boa generalização

---

## Aula 04 -  Aspectos sobre treinamento de redes neurais artificiais e outros modelos

### Aspectos gerais sobre o treinamneto de modelos

* **Cuidado na preparação e execução do treinamento**

  * Divisão do banco de dados
  * Capacidade de generalização
  * Desempenho do modelo ajustado
* **Interpretabilidade do algoritmo de aprendizado de máquinas**
* **Problemas de regressão e de classificação**

  * Influência na estrutura da RNA
    * Número de neurônios
    * Funções de ativação
    * Indicador de desempenho

### Banco de dados do problema

* **Quantidade grande de exemplos**
  * Principalmente se form um problema multiclasses
  * Identificar dados significativos
  * Balanceamento entre classes
* Divisão do banco de dados em conjunto de treinamento e de teste
  * 70% a 90% para treinamento
  * 30% a 10% para teste
  * Seleção aleatória dos dados
  * Seleção sistemática
    * Validação cruzada de k-participações (*k-fold cross-validation*)

### Validação cruzada k-fold

> A validação cruzada *k-fold* consiste em dividir o conjunto de dados em k participações (folds). A cada iteração, k-1 folds são usados para treinamento e 1 fold é usado para validação. Esse processo é repetido k vezes, usando cada fold uma vez como validação, e o resultado final costuma ser a média das métricas obtidas.

````mermaid
graph LR
    A[k-fold Cross-Validation] --> B[Dividir dados em k folds]
    A --> C[Repetir k vezes]
    C --> D[Treinar com k-1 folds]
    C --> E[Validar com 1 fold]
    A --> F[Calcular média das métricas]
    A --> G[Usar Stratified k-fold em classificação]

````

### Interpretação de uma PMC

* Redes PMC com uma camada escondida
  * resolvem muitos problemas não lineares
    ![PMC]('./Docs/images/PMC.png')

    * playground do tensorflow
        * Ambiente educacional de construção de redes de perceptron multicamadas. 


### Underfitting e Overfitting


### Topologia da Cruva de EQM

### Arquitetura típica para PMC de regressão


### Arquitetura típica para PMC de classificação

#### Consideraçãoes finais