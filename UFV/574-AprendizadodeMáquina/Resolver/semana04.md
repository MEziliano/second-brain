# Semana 04 - Aprendizado por reforço


### Questão1  

Leia atentamente as afirmações abaixo, compostas por uma asserção e uma razão. Em seguida, selecione a alternativa que melhor descreve a relação entre elas.

* **Asserção**: O Deep Q-Learning resolve a limitação do Q-Learning em lidar com espaços de estado contínuos.
* **Razão**: Redes neurais profundas no Deep Q-Learning são utilizadas para aproximar a função Q(s,a).

a.Asserção e razão estão corretas, e a razão explica corretamente a asserção.

b.Asserção e razão estão corretas, mas a razão não explica a asserção.

c.A asserção está correta, mas a razão está incorreta.

d.A asserção está incorreta, mas a razão está correta.

e.Tanto a asserção quanto a razão estão incorretas.
> RESPOSTA: [A]
<DETAILS><SUMMARY> EXPLICAÇÃO</SUMMARY>

A alternativa correta é a **a. Asserção e razão estão corretas, e a razão explica corretamente a asserção.**

**Explicação**:

* **Asserção (Correta):** O Q-Learning tradicional utiliza uma tabela (Q-table) para armazenar os valores de cada par estado-ação ($s, a$). Quando o espaço de estados é contínuo ou excessivamente grande, torna-se impossível armazenar todas as combinações em uma tabela, limitação esta que o Deep Q-Learning consegue contornar.
* **Razão (Correta e justificativa):** Para resolver o problema de espaços contínuos/grandes, o Deep Q-Learning substitui a tabela por uma rede neural profunda (Deep Neural Network), que atua como um **aproximador de funções**, estimando o valor da função $Q(s, a)$ de forma generalizada para qualquer estado de entrada. Portanto, a utilização da rede neural é exatamente o mecanismo que permite lidar com essa limitação.
</DETAILS>

### Questão 2

* **Asserção**: A função de valor V(s) no aprendizado por reforço estima o retorno esperado a partir de um estado s.
* **Razão**: A função V(s) considera a política seguida pelo agente para calcular o retorno esperado.

a.Asserção e razão estão corretas, e a razão explica corretamente a asserção.

b.Asserção e razão estão corretas, mas a razão não explica a asserção.

c.A asserção está correta, mas a razão está incorreta.

d.A asserção está incorreta, mas a razão está correta.

e.Tanto a asserção quanto a razão estão incorretas.
> Resposta [A]
<details>
<summary>Explicação</summary>

A alternativa correta é a **a. Asserção e razão estão corretas, e a razão explica corretamente a asserção.**

### Explicação:

* **Asserção (Correta):** A função de valor de estado $V(s)$ no aprendizado por reforço mede o quão "bom" é para um agente estar em um determinado estado $s$, calculando formalmente o retorno esperado (soma dos *rewards* futuros descontados) a partir daquele ponto.
* **Razão (Correta e justificativa):** O valor obtido em $V(s)$ não é absoluto, pois depende diretamente da estratégia que o agente adota — ou seja, a **política** ($\pi$). O retorno esperado muda dependendo de quais ações o agente tem probabilidade de tomar no futuro, o que justifica e define matematicamente a função de valor como $V^\pi(s)$. Portanto, a razão explica o mecanismo pelo qual a asserção é calculada.
</details>

### Questão 3

* **Asserção**: A política π(a∣s) define a probabilidade de selecionar uma ação a em um estado 
s.
* **Razão**: A política sempre garante a escolha da ação que maximiza a recompensa imediata.

a.Asserção e razão estão corretas, e a razão explica corretamente a asserção.
b.Asserção e razão estão corretas, mas a razão não explica a asserção.
c.A asserção está correta, mas a razão está incorreta.
d.A asserção está incorreta, mas a razão está correta.
e. Tanto a asserção quanto a razão estão incorretas.
> RESPOSTA [C]
<details>
<summary>EXPLICAÇÃO</summary>
A alternativa correta é a **c. A asserção está correta, mas a razão está incorreta.**

### Explicação:

* **Asserção (Correta):** A política $\pi(a \mid s)$ representa formalmente a distribuição de probabilidade de um agente escolher uma determinada ação $a$ dado que ele se encontra no estado $s$.
* **Razão (Incorreta):** A política **não** garante necessariamente a escolha da ação que maximiza a recompensa *imediata* (o que caracterizaria apenas uma abordagem míope ou gulosa / *greedy*). No aprendizado por reforço, uma política (especialmente a ótima) busca maximizar o **retorno cumulativo a longo prazo** (recompensas futuras descontadas), o que pode exigir que o agente escolha ações com recompensas imediatas menores ou até negativas se isso levar a estados muito mais vantajosos no futuro.
</details>

### Questão 4 

* **Asserção**: No método Q-Learning, a tabela Q(s,a) é atualizada com base na recompensa recebida e no valor estimado do próximo estado.
* **Razão**: O Q-Learning é um método off-policy, pois utiliza uma política diferente para a escolha de ações durante o aprendizado.

a.Asserção e razão estão corretas, e a razão explica corretamente a asserção.

b.Asserção e razão estão corretas, mas a razão não explica a asserção.

c.A asserção está correta, mas a razão está incorreta.

d.A asserção está incorreta, mas a razão está correta.

e.Tanto a asserção quanto a razão estão incorretas.

> RESPOSTA [B]
<details><summary>EXPLICAÇÃO</summary>


* **Asserção (Correta):** No Q-Learning, a atualização da tabela $Q(s, a)$ utiliza a regra de Bellman, que se baseia na recompensa imediata recebida ao tomar a ação e no valor estimado do próximo estado (especificamente, considerando o valor máximo possível para o próximo estado, $\max_{a'} Q(s', a')$).
* **Razão (Correta, mas não explica a asserção):** O Q-Learning é de fato um algoritmo *off-policy* porque a política utilizada para gerar o comportamento (exploração, como $\epsilon$-greedy) é diferente da política que está sendo avaliada e otimizada (que assume a escolha da ação ótima $\max Q$). No entanto, o fato de ser *off-policy* não é a **causa** ou a explicação direta de a tabela Q ser atualizada com base na recompensa e no próximo estado (isso é uma característica fundamental da aprendizagem por diferenças temporais/equação de Bellman, válida tanto para métodos *on-policy* quanto *off-policy*).
</details>


### Questão 5 
* **Asserção**: O aprendizado por reforço é um método adequado para problemas onde a sequência de ações influencia os resultados futuros.
* **Razão**: Em aprendizado por reforço, o objetivo do agente é maximizar a recompensa imediata obtida a cada ação.

a.Asserção e razão estão corretas, e a razão explica corretamente a asserção.

b.Asserção e razão estão corretas, mas a razão não explica a asserção.

c.A asserção está correta, mas a razão está incorreta.

d.A asserção está incorreta, mas a razão está correta.

e.Tanto a asserção quanto a razão estão incorretas.
> RESPOSTA [c]
<DETAILS>
<SUMMARY>EXPLICAÇÃO</SUMMARY>


* **Asserção (Correta):** O aprendizado por reforço é ideal para problemas sequenciais de tomada de decisão (processos de decisão de Markov), onde as ações tomadas no presente afetam diretamente os estados futuros e, consequentemente, os resultados a longo prazo.
* **Razão (Incorreta):** O objetivo do agente no aprendizado por reforço **não** é maximizar a recompensa imediata, mas sim maximizar o **retorno cumulativo total ao longo do tempo** (a soma das recompensas futuras descontadas). Muitas vezes, o agente precisa abrir mão de uma recompensa imediata (ou até aceitar uma punição momentânea) para alcançar um objetivo maior no futuro.
</DETAILS>

### Questão 6 
Considere um agente de aprendizado por reforço treinado para jogar xadrez. Qual é a definição mais precisa do agente e suas ações nesse contexto?

a.O agente é o tabuleiro de xadrez, e as ações são as peças disponíveis.

b.O agente é o algoritmo de aprendizado, e as ações são as decisões de movimento das peças.

c.O agente é o jogador de xadrez, e as ações são os movimentos possíveis das peças no tabuleiro.

d.O agente é o oponente, e as ações são as estratégias usadas no jogo.

>RESPOSTA[C]
<DETAILS>
<SUMMARY>EXPLICAÇÃO</SUMMARY>

* No Aprendizado por Reforço, o **agente** é a entidade que toma as decisões e interage com o ambiente (neste caso, o programa ou modelo que atua como o jogador de xadrez).
* As **ações** representam o conjunto de escolhas ou movimentos válidos que o agente pode realizar no ambiente em um dado estado (ou seja, mover uma peça para uma nova casa válida no tabuleiro).
* A alternativa (b) erra ao definir o agente como o "algoritmo de aprendizado" em vez do tomador de decisões (o jogador), e as demais estão incorretas pois confundem o agente com componentes passivos ou com o adversário.
</DETAILS>


### Questão 7 

Em um sistema de aprendizado por reforço onde um robô aspirador de pó é treinado para limpar uma sala, qual das seguintes opções melhor define o ambiente?

a. As decisões tomadas pelo robô sobre onde se mover.

b. O espaço físico da sala, incluindo obstáculos e sujeira.

c. A tabela Q utilizada para armazenar os valores das ações.

d. O algoritmo usado para treinar o modelo.
> RESPOSTA [B]
<DEATILS>
<SUMMARY>EXPLICAÇÃO</SUMMARY>


* No Aprendizado por Reforço, o **ambiente** é tudo aquilo com o qual o agente interage, ou seja, o mundo externo onde o agente observa estados, executa ações e recebe recompensas. Para o robô aspirador, o ambiente é o espaço físico (a sala) contendo os móveis, paredes, obstáculos e os locais sujos que precisam ser limpos.
* As decisões do robô representam as **ações**, a tabela Q é uma estrutura interna de dados/memória do algoritmo, e o algoritmo de treinamento é o método de aprendizado, não o ambiente.
<DETAILS>


### Questão 8 
Em um jogo de labirinto onde o objetivo é alcançar uma saída, qual das opções a seguir pode ser uma definição apropriada de recompensa?

a. O número de passos dados pelo agente em cada rodada.

b. A quantidade de memória consumida pelo algoritmo.

c. Um valor positivo dado ao agente quando ele encontra a saída.

d. O mapeamento dos caminhos possíveis no labirinto.

>RESPOSTA [C]
<DETAILS>
<SUMMARY>EXPLICAÇÃO</SUMMARY>
A alternativa correta é a **c. Um valor positivo dado ao agente quando ele encontra a saída.**

### Explicação:

* No Aprendizado por Reforço, a **recompensa** (reward) é o sinal numérico que o ambiente envia ao agente para indicar quão desejável foi o resultado de uma ação ou estado. Encontrar a saída do labirinto é o objetivo principal, portanto, atribuir um valor positivo (e muitas vezes alto) nessa situação serve como o feedback principal para reforçar o comportamento correto.
* As outras opções representam métricas de desempenho computacional (memória), uma estrutura estática (mapeamento de caminhos) ou uma penalidade opcional (número de passos, que geralmente é um custo ou penalidade por passo, e não a definição primária de recompensa pelo objetivo).
</DETAILS>