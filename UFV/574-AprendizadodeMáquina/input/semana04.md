# Semana 04 - Aprendizado por reforço

## Aula 01 -  Introdução ao Aprendizado por Reforço
### Introdução 

* Paradigma de aprendizado diferente dos demais
* Os agentes podem aprender por interação com o ambiente
* Dados são fornecidos pelo ambiente
* Aprender com o ambiente pode ser aplicado em:
    * Jogos
    * Robótica
    * Navegação autonoma
    * Operação em bolsa de valores


| Característica | A. Supervisionado | A N Supervisionado | A por reforço|
| -------------- | ------------------ | ------------------ | ------------| 
| **Dados**| Dados rotulados | Dados não rotulados | Observação e recompensas|
| **Objetivo**| Predição de rótulos | Descoberta de padrões | Maximizar recompensa| 
| **Ex. de aplicação** | Classificação de e-mails | Segmentação de clientes | Jogos e controle de processos| 
| **Ex. Algoritmo**| Regressão linear, Arv. Decisão | K-means e PCA | Q-Learning, Deep Q-Learning, Métodos dos gradientes| 


### Fundamentos do aprendizado por reforço

Estado $S_t$, Recompensa $r_t$ e ação $a_t$. Loop **Agente** mais $r_{t+1}$ e $s_{t+1}$ com as interações com o **ambiente**.

### Aula 02 - Processo de decisão de Markov e política de ações

#### Ambiente de Aprendizado
* Local onde o agente aprende o valor de suas ações.
* **DEVE** ser um ambiente simulado
* Quanto mais próximo da realidade, melhor!
* Representado por cadeias de Markov
    * Processo de Markov
    * Processo de Decisão de Markov (PDM)
#### Processo de Markov
* Relação entre estados de um processo
* Transição de estados
* Probabilidade de transição de estados
    * Ex.: *Metereologia*, Ensolarados para chuvosos e etc. 
    * Ex.: Rotina de Dilbert. Reunião, café, trabalho e casa. 

Obs.: Existem cadeias de Markov com fim! Como por exemplo, quando tem um labirinto como ambiente. 
* Objetivo de um agente: maximizar a recompensa total

$
G_t =  R_{t+1} + \gamma R{_t+2} + \gamma² R_{t+2} ... = \sum^{k=T-1}_{t=0} \gamma^t R_{t+1} 
$

com $0 \leq \gamma \leq 1$

* Propriedade do MDP
    * **Markovianidade**: Proximo estado depende apenas do anterior
     $P(s_{t+1} | s_t, a_t, s_{t-1}, ... ) + P(s_{t+1}| s_t, a_t)     $
    * **Estacionariedade**: Probabilidades de transição permace constante

#### Função de valor dos estados
* Esperança de recompensa para um estado
$ V(s) = E[G_t|S_t= s] \displaystyle\sum_{s \isin S} P(s_{+1}|s_t) R_{t+1} $
Obs.: Basicamente, levar em consideração todas as recompensas disponíveis. Assim, como um espaço amostral leva em consideração todas as possibilidades.  

### Processo de decisção de Markov
* Comparando a função de recompensa no MDP

    $G_t =  R_{t+1} + \gamma R{_t+2} + \gamma² R_{t+2} ... = \sum^{k=T-1}_{t=0} \gamma^t R_{t+1} 
    $

com $0 \leq \gamma \leq 1$

* E a função valor dos estados

    $ V(s) = E[G_t|S_t= s] \displaystyle\sum_{s \isin S} P(s_{+1}|s_t) R_{t+1} $

#### Agentes e suas ações
* Até aqui, o MDP foi apenas observado
* Agente por meio da ação faz a transição do estado. 
* A política de ação é dado por:
    $ \pi (a|s) = P(A_t =a | S_t=s)$
* Probabilidade do agente realizar uma ação dado um determinado estado
    * **Determinística**, se a chance de realizar uma ação é de 100%
    * **Não determinístico**, se possuir outras possibilidades