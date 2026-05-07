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