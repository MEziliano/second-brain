# Semana 01 - Exploração de dados

# Introdução

Matéria ministrada pelo professor Rodolfo Neves.

**Conteúdo**

* Banco de dados, tratamento nos dados, limpeza e inserção de dados.
* Extração de características dos conjuntos
* Apredizado supervisionado: Redes Neurais artificiais (RNA)
* Aprendizado não-supervisionado: K-means
* Aprendizado por reforço: Q-learning e o dilema da exploração e explotação (*Reinforcement Learning*)


<details><summary> Documentação de pacotes</summary>

A documentação dos pacotes que vamos utilizar no decorrer da disciplina podem ser acessadas pelos links a seguir.

> Semana 1:

* NumPy: https://numpy.org/doc/2.0/reference/index.html#reference
* Pandas: https://pandas.pydata.org/docs/user_guide/index.html#user-guide
* Matplotlib.pyplot: https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html
* Seaborn: https://seaborn.pydata.org/api.html
* Folium: https://python-visualization.github.io/folium/latest/reference.html
* Folium.Plugins.MarkerCluster: https://python-visualization.github.io/folium/latest/user_guide/plugins/marker_cluster.html
* Scikit-learning.preprocessing: https://scikit-learn.org/stable/modules/preprocessing.html
    * OrdinalEncoder: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html
    * OneHotEncoding: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html
    * StandardScaler: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html
    * MinMaxScaler: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html
> Semana 2:

* Scikit-learning:
    * LinearModel: https://scikit-learn.org/stable/api/sklearn.linear_model.html
        * Perceptron: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Perceptron.html
    * Model Selection: https://scikit-learn.org/stable/api/sklearn.model_selection.html
        * Train-test-split: https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
        * RandomizedSearchCV: https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html
    * TensorFlow: https://www.tensorflow.org/api_docs
        * Keras: https://www.tensorflow.org/api_docs/python/tf/keras
    * Scikeras.wrappers: https://adriangb.com/scikeras/stable/
        * KerasRegressor: https://adriangb.com/scikeras/stable/generated/scikeras.wrappers.KerasRegressor.html
    * SciPy.Stats: https://docs.scipy.org/doc/scipy/reference/stats.html
        * Reciprocal: https://docs.scipy.org/doc/scipy-0.16.1/reference/generated/scipy.stats.reciprocal.html
    * Pickle: https://docs.python.org/3/library/pickle.htmlA documentação dos pacotes que vamos utilizar no decorrer da disciplina podem ser acessadas pelos links a seguir.
</details>


# Aula 01 - Introdução ao aprendizado de máquina
Aprendizado de máquina é o termo que se dá a capacidade de determinado software de otimizar ou maximizar ou minimizar um conjunto de um parametro dadao um determinado conjunto de dados. 

**Contexto histórico**

Apesar de muito usado atualmente, o aprendizado de máquina surgiu na segunda guerra mundial, com os esforços dos aliados de desenvendar as mensagens do alemães. Ao término da guerra houve um período sem grandes avanços significativos. 

**Introdução**
| Aprendizado Humano |  Aprendizado de Máquina | 
| ------------------ | ----------------------- |
| Aprende aos poucos | pode aprender com apenas uma vez| 
| Aprendizado por meio de exemplo| Aprendizado por meio de dados|
| Adquire habilidades | Identifica padrões| 

**Contextualização**
* Aprendizado de máquinas é datado da II Guerra Mundial.
    * Limitação de processamento esfriou o desenvolvimento, o que ficou conhecido como *inverno da IA*
* Alta capacidade de processamento das máquinas
* Grande quantidade de dados disponíveis
* Maiores empresas de dados: Facebook, Google, Microsoft, Amazon

**Modelos de ML**
<br>
$y = f(x)$, onde $y$ representa as saídas, ou seja uma predição, umaestimação do valor. $f$ representa uma função otimizada, que são os modelos e os algoritmos. E, por fim, $(x)$ representa as entradas, o que pode ser imagens, sons, valore e características. 

### Tipos de Treinamentos
| Supervisionado | Não Supervisionado| 
| -------------  | ----------------- |
| Entradas rotuladas|  Entradas |
| Regressão linear, Redes Neurais, etc| Clusterização, Kmeans, Aprendizado por reforço|
|sadídas para futuraas amostras | saídas agrupadas por clusters|


### **Etapas da Construção de um modelo de ML**
1. Formulação do problema
* Aumentar vendas
* Perfil de cliente
* Sexo
* Idade
* Religião
* Estado civil
* Gasto médio na loja
* Dados das compras
* Produto
* Gasto médio por compra
* Ocasião
2. Seleção e adaptação do banco de dados
* Compra
* Camisa manga longa
* Camisa manga curta
* Camiseta casual
* Camiseta regata
3. Pré-processamento do banco de dados
Retirar inconsistências
    * Valores em branco
    * Especificações erradas
    * Outliers
* Transformação de dados
* Estado civil:
    * Solteiro = 1
    * Casado = 2
    * Divorciado = 3
    * Viúvo = 4
* Descartar dados não
relevantes
4. Separação do banco de dados em dados de
treinamento e dados de validação
Dados de treinamento
    * 70% do banco de dados
* Dados de validação
    * 30% do banco de dados
* Separação 70/30
    * Até 90/10
5. Treinamento do modelo com os dados de
treinamento
* Ajuste na função
    * 𝑦 = 𝑓(𝑥)
* 𝑓(𝑥) pode ser:
*  Máquina de vetor de suporte
    * Rede neural artificial
    * Sistema nebuloso
6. Validação do modelo e estimativa de
desempenho com os dados de validação
* Dados de validação
* Métricas de desempenho
* Escolha do melhor
modelo
7. Implementação do modelo para a aplicação

# Aula 02 - Tipos de dados e tratamentos de dados
### Tipos de dados
* Estabelecer relações entre entradas e saídas conhecidas
* Aplicar as relações desenvolvidas para dados não conhecidos

* **Qualitativos** (categóricos)
    * Não assume valores numéricos
    * **Nominal**: Não ordenados. Ex.: gênero, estado civil, religião...
    * **Ordinário**: ordenados. Ex.: Tamanho de roupa, meses do ano, alfabeto...

* **Quantitativos**
    * Medidos em números
    * **Discretos**: valores contávies e determinados. Ex.: Idade em anos, marchas de um carro...
    * **Contínuos**: quantidade dentro de um intervalo. Ex.: Altura e peso de uma determinada pessoa.


### Ferramentas para exploração dos dados
| Ferramentas descritivas | Ferramentas de inferência|
| ---------------------------- | ------------------------ |
| Medidias de tendência central| Teste de hipótese|
| Média <br> Mediana <br> Moda | Análise da variância (ANOVA)| 
| Medidas de dispersão |Teste Chi Quadrado |
| Intervalor <br> Desvio Padrão| Regressão Linear|
| Distribuição das frequências| |
| Histogramas| | 

 ### Explroração dos dados

* **Inspeção do banco de dados**

    1 . Conhecer as variáveis do banco de dados
    * Nomes
    * Características
    * Intervalo máximo e mínimo

    2 . Reconhecer dados ausentes ou inválidos
    * Tratar ou desconsiderar estes dados
    
    3 . Conhecer a distribuição dos dados
    * Evitar dados destoantes (*outliers*)
    * Considere $\mu$ a média de uma variável $x$e desvio padrão $\sigma$
    * Se $\mu - 3\sigma > x_i > \mu + 3\sigma$, provavelmente $x_i$ é um outlier
    * Na dúvida, realizar o ajuste do modelo com e sem estes valores

### Exemplo com dados que atrapalham
| Nome | Sexo | idade | Altura (m) | Peso (kg) | Consumo de regrigerante (L/semana) |
| ------- | --- | ----- | ----------| ----------| ------------------------------------| 
| Bárbara | F | 25 | 1,65 | 59,6| 04|  
| Danilo | M | 32 | 1,70| 96| 1,2| 
| Gabriela | F | 51| 1,62| 55,4| 0,1| 
| Joaquim | M | 35| 1,57| 60,0 | 1,0| 
| Melina| F | 63 | 1,75| 70,0| 0,6|
| Patrick| M |46| 1,80| 103,0| 1,3| 
| Tatiane |F | 75 | 1,52| 50,3| 0,0|

$
\mu_A = \dfrac{04+1,2+0,1+1,0+0,6+1,3+0,0}{7} = 1,171 \text{L/semana} 
\sigma_A = \sqrt{\dfrac{\sum^n_{i=1} (x_i \mu_a)^2}{n}} = 0,853 \text{L/semana} \\
\mu_B = \dfrac{1,2+0,1+1,0+0,6+1,3+0,0}{6} = 0,7 \text{L/semana}  
\sigma_B = \sqrt{\dfrac{\sum^n_{i=1} (x_i \mu_b)^2}{n}} = 0,467 \text{L/semana}
$ 

# Aula 03 - Relação entre variáveis e extração de características