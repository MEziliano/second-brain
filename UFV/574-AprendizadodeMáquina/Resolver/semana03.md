# Semana 3  Cluster

### 1. 
Leia atentamente as afirmações abaixo, compostas por uma asserção e uma razão. Em seguida, selecione a alternativa que melhor descreve a relação entre elas.

Asserção: O algoritmo K-means minimiza a soma das distâncias quadradas dos pontos aos centroides dos clusters.
Razão: O K-means calcula a densidade dos pontos ao longo de múltiplas iterações para determinar o agrupamento ideal.

Questão 1Resposta

a. Asserção e razão estão corretas, e a razão explica corretamente a asserção.
b. Asserção e razão estão corretas, mas a razão não explica a asserção.
c. A asserção está correta, mas a razão está incorreta.
d. A asserção está incorreta, mas a razão está correta.
e. Tanto a asserção quanto a razão estão incorretas.

**RESPOSTA** [C]
<details><summary> Explicação </summary>

**Por que a Asserção está correta?** O que o K-means está realmente tentando otimizar matematicamente? Ele busca minimizar a variância dentro de cada cluster. Matematicamente, isso é a soma das distâncias euclidianas ao quadrado entre cada ponto e o centróide do seu cluster (conhecido como WCSS - Within-Cluster Sum of Squares ou Inertia).

**Por que a Razão está incorreta?** O K-means usa densidade? Pense em como o algoritmo define os limites de um cluster. Ele desenha "círculos" (esferas em n-dimensões) baseados em distância a partir de um ponto central. Quem usa densidade na verdade são algoritmos como DBSCAN ou Mean Shift. O K-means falha miseravelmente se os clusters tiverem densidades muito diferentes ou formatos não-esféricos.
</details>

### 2. 
Leia atentamente as afirmações abaixo, compostas por uma asserção e uma razão. Em seguida, selecione a alternativa que melhor descreve a relação entre elas.

Asserção: O coeficiente de silhueta para os clusters representados na imagem indica que o agrupamento foi bem-sucedido para a maioria dos pontos, mas poderia ser melhorado.
Razão: Na análise da silhueta, valores negativos ou próximos de zero mostram que os pontos estão mal alocados ou situados na fronteira entre clusters. 

a. Asserção e razão estão corretas, e a razão explica corretamente a asserção.
b. Asserção e razão estão corretas, mas a razão não explica a asserção.
c. A asserção está correta, mas a razão está incorreta.
d. A asserção está incorreta, mas a razão está correta.
e. Tanto a asserção quanto a razão estão incorretas.
**RESPOSTA** [A]
<details><summary> Explicação </summary>
Asserção (correta):
O que o gráfico mostra? A maior parte da "massa" é azul (valores positivos) → a maioria dos pontos está bem alocada. 
Mas repare nos clusters 1 e 3: eles têm "caudas" vermelhas (valores negativos até ≈ −0.4) → alguns pontos foram provavelmente atribuídos ao cluster errado.
Conclusão: agrupamento bom para a maioria, porém imperfeito → "poderia ser melhorado" (ajustar k, escalar features, outro algoritmo...). ✔️
📌 Razão (correta):
A silhueta é s(i)=b(i)−a(i)/max⁡(a(i),b(i)) ∈[−1,1]
 onde 
a = distância média intra-cluster e b = menor distância média aos clusters vizinhos.
s≈+1 → ponto bem agrupado 🟢
s≈0 → ponto na fronteira entre clusters 🟡
s menor 0 → ponto provavelmente no cluster errado 🔴
</details>

### 3. 

Leia atentamente as afirmações abaixo, compostas por uma asserção e uma razão. Em seguida, selecione a alternativa que melhor descreve a relação entre elas.

Asserção: A métrica de Silhueta é utilizada para avaliar a qualidade dos clusters criados pelo K-means.
Razão: O coeficiente de Silhueta mede a compacidade dos clusters em relação à distância média entre os pontos e o centroide.

a. Asserção e razão estão corretas, e a razão explica corretamente a asserção.
b. Asserção e razão estão corretas, mas a razão não explica a asserção.
c. A asserção está correta, mas a razão está incorreta.
d. A asserção está incorreta, mas a razão está correta.
e. Tanto a asserção quanto a razão estão incorretas.

**RESPOSTA** [C]
<details><summary> Explicação </summary>
sserção (correta):
A Silhueta avalia a qualidade de qualquer particionamento, inclusive o do K-means. ✔️
Detalhe importante: ela é agnóstica ao algoritmo — só precisa dos rótulos dos clusters e da matriz de distâncias. Por isso funciona até com DBSCAN.
📌 Razão (incorreta):
O que a razão descreve ("distância média entre os pontos e o centroide") é, na verdade, a Inércia / WCSS — a função objetivo que o K-means minimiza, e não a Silhueta. 🚫
A Silhueta não usa centroides. Ela compara distâncias ponto a ponto:
a(i) = distância média do ponto aos outros pontos do mesmo cluster (coesão);
b(i) = menor distância média do ponto aos pontos do cluster vizinho (separação);

s(i)= 
max(a(i),b(i))
b(i)−a(i)
​
 ∈[−1,1].
Ou seja: a razão troca a definição de Silhueta (coesão × separação entre pontos) pela definição de Inércia (ponto × centroide).
</details>


### 4. 

Leia atentamente as afirmações abaixo, compostas por uma asserção e uma razão. Em seguida, selecione a alternativa que melhor descreve a relação entre elas.

Asserção: O K-means é robusto a outliers, pois os pontos distantes não influenciam os centroides dos clusters.
Razão: O algoritmo calcula a média de todos os pontos em um cluster para determinar o centroide, o que inclui os outliers.

a. Asserção e razão estão corretas, e a razão explica corretamente a asserção.
b. Asserção e razão estão corretas, mas a razão não explica a asserção.
c. A asserção está correta, mas a razão está incorreta.
d. A asserção está incorreta, mas a razão está correta.
e. Tanto a asserção quanto a razão estão incorretas.
**RESPOSTA** [D]
<details><summary> Explicação </summary>
Asserção (incorreta):
O K-means é sensível a outliers, não robusto. 🚫
Pense: o que acontece com uma média aritmética quando você insere um valor extremo? Ela é "puxada" na direção dele. Um único outlier distante pode deslocar o centroide e distorcer todo o particionamento (além de inflar o WCSS, já que a distância é ao quadrado).
📌 Razão (correta):
O passo de atualização do K-means recalcula o centroide como a média de todos os pontos atribuídos ao cluster — outliers inclusos. ✔️
É exatamente esse mecanismo que torna o algoritmo vulnerável: a razão contradiz a asserção, em vez de sustentá-la.
</details>

### 5. 
Leia atentamente as afirmações abaixo, compostas por uma asserção e uma razão. Em seguida, selecione a alternativa que melhor descreve a relação entre elas.

Asserção: No aprendizado supervisionado, o modelo utiliza dados rotulados para aprender.
Razão: O aprendizado supervisionado é baseado em identificar padrões nos dados sem a necessidade de um conjunto de treinamento com rótulos pré-definidos.

a. Asserção e razão estão corretas, e a razão explica corretamente a asserção.
b. Asserção e razão estão corretas, mas a razão não explica a asserção.
c. A asserção está correta, mas a razão está incorreta.
d. A asserção está incorreta, mas a razão está correta.
e. Tanto a asserção quanto a razão estão incorretas.


**RESPOSTA** [C]
<details><summary> Explicação </summary>
Asserção (correta):
Aprendizado supervisionado = aprender um mapeamento 

f:X→Y a partir de pares rotulados 
(𝑥𝑖, 𝑦𝑖)(xi ,yi). ✔️
Exemplos: classificação, regressão — seu dia a dia.
📌 Razão (incorreta):
"Identificar padrões sem rótulos" é a definição de aprendizado NÃO supervisionado (clustering, redução de dimensionalidade). 🚫
A razão descreve o oposto do conceito da asserção — é a definição do paradigma vizinho (como o K-means das questões anteriores!).
</details>


### 6. 
Asserção: O K-means é amplamente utilizado para segmentação de clientes no mercado.
Razão: Porque o K-means pode identificar grupos com características similares, permitindo estratégias de marketing personalizadas.

a. Asserção e razão estão corretas, e a razão explica corretamente a asserção.
b. Asserção e razão estão corretas, mas a razão não explica a asserção.
c. A asserção está correta, mas a razão está incorreta.
d. A asserção está incorreta, mas a razão está correta.
e. Tanto a asserção quanto a razão estão incorretas.

**RESPOSTA** [A]
<details><summary> Explicação </summary>
K-means é o algoritmo "de livro-texto" para segmentação de clientes (ex.: análise RFM — Recência, Frequência, Valor Monetário). ✔️
📌 Razão (correta):
O algoritmo agrupa clientes por similaridade (menor distância ao centroide) → clusters internamente homogêneos e externamente distintos. ✔️
Grupos homogêneos = segmentos acionáveis → campanhas personalizadas, pricing, retenção. 🎯

</details>