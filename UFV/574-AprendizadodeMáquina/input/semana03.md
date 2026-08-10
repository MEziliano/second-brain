# Semana 03 - Aprendizado Não Supervisionado

## Aula 01 - Introdução ao Aprendizado Não Supervisionado
### Introdução 
* Reconhece e agrupa padrões entre as amostras
* Dados não rotulados contam uma história
* Descobrir padrões podem servir em aplicações:
    * Tomada de decisões estratégicas: segmentação de clientes
    * Identificação de tendências e comportamentos emergentes
    * Auxílio em sistemas de recomendações, personalização e descoberta de produtos.

### Aplicações do aprendizado não supervisionado
* **Segmentação de mercado**
    * Agrupar clientes com comportamentos semelhantes
    * Recomendar produtos que tenham potencial de compra para um grupo de clientes
    * Indicar produtos (músicas, filmes, séries, livros) baseado no comportamento do cliente.
* **Análise de anomalias**
    * Verificar se as características de determinadas amostras estão coerentes com as demais
* **Reconhecimento de padrões em imagens**
    * Selecionar e destacar (máscara) partes de imagem
* **Redução de dimensionalidade**
    * Transformar características de uma imagem (*pixels*) em distâncias para um grupo

------

## Aula 02 - Algoritmo K-means

* Um dos algoritmos de agrupamento mais utilizado
* Dividir  um conjunto de dados em K clusters
* Minimiza a variablidade dentro de cada cluster. 

### Histórico de desenvolvimento do algoritmo
* 1956 - Introduzido por Hugo Steinhaus, Contexto matemático de particionamento de dados;
* 1957 - Formalizado como algoritmo por Stuart Llyod, Compressão de dados na Bell Labs;
* 1967 - James McQueen, popularização do termo *K-means*, abordou questões de aplicações práticas. 
* 2006 - Arthur e Vassilvitskii introduziram o conceito do *K-means ++*. Reduzir os problemas de convergência local. 

#### Pseudocódigo do modelo:
1. Escolha do número de k de clusters.
    * Influência diretamente o resultado do modelo (hiperparâmetro).
    * Reuquer experimentação (executar o ajuste para diferentes valores de k)
2. Inicialização dos centróides.
    * Pode ser feita de forma aleatória ou otimizada (*K-means ++*)
    * Influencia diretamente nas chances de resultar em soluções ótimas ou subótimas. 
3. Atribuição de pontos aos grupos com centróides mais próximos.
    * Critério de utilizado para definir a distância da amostra para o centroide.
        * Distância Euclidiana
        * Distância de Manhattan (*block distance*)
        * Similaridade de cosseno
4. Recalculo dos centróides a partir das amostras aos cluster associado.
5. Iteração até atingir algum critério de parada. 
    * Convergência: quando os centriodes não se movem mais que a tolerância.
    * Nṕumero máximo de iterações: o ajuste é interrompido quando a convergência não é alcançada.

### Algoritmo K-means: Avaliação do modelo
*  **Soma dos erros internos (SSE) ou soma dos quadrados intra-clusters(WCSS)**
$$

SSE = \sum^{n}_{i=1} (x_i - x_c)²

$$
* $x_i$ é o valor das coordenadas da amostra
* $x_c$ é o valor das coordenadas do cluster daquela amostra

* **Coeficiente de silhueta**
$

s(i) =  \dfrac{b(i) - a(i)}{max(a(i), b(i))}

$
* $a(i)$ é a média da distância das amostras do mesmo cluster para a amostra $i$
* $b(i)$ é a média da distância das amostras do clsuter mais próximo para a amostra $i$. 

### Limitações do algoritmo k-means
* Escolha do número de clusters
* Sensibilidade a *outliers* 
* Cluster de forma específica. Bom para distâncias radiais, mas para outros formados não, como meia lua ou elipses. 
* Depêndecia da inicialização. 
* Escolha da métrica de similiridade

### Aplicações do K-means
* Exploração de dados. Uma continuação da análise exploratória de dados inicial.
* Descoberta de agrupamentos naturais. 
* Redução de dimensionalidade e resumo de dados.  
* Segmentação de imagens
* Análise de clientes.
* Detecção de anomalias. 