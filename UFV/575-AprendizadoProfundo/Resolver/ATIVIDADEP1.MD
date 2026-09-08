Crie um Notebook no Google Colab com o nome [ELT575_Semana2_<Matrícula>], modificando o campo <Matrícula> pela sua matrícula do Sapiens. As implementações requeridas pela atividade devem estar explícitas neste notebook (todos os códigos, resultados obtidos e resposta requeridas em cada passo). Ao final, envie o link do notebook como resposta da tarefa (LEMBRE-SE DE DEIXAR O ACESSO AO NOTEBOOK PÚBLICO - sem isso, não haverá correção). Tente organizar o notebook em seções.

Link para notebook Image_classification_CNN: https://colab.research.google.com/drive/1r0pIj6INqqhnOwctukEYmih84GTTTiqN?usp=sharing

Repita o exemplo Image_classification_CNN usando o dataset CIFAR-10 (https://www.tensorflow.org/datasets/catalog/cifar10), também disponível no Tensorflow. As imagens agora tem a forma 32 x 32 x 3, sendo necessário fazer ajustes na rede para esse caso. Recomendado executar usando o recurso de GPU do Colab agilizar os treinamentos das redes.

Houve muita diferença no desempenho da rede treinada quando comparado ao exemplo? 

Experimente adicionar mais dois blocos de camadas Conv2D (64 filtros 3x3 - relu) + MaxPooling (2 x 2) antes da camada Flatten e compare os resultados.

Seguindo o modelo modificado no item anterior, experimente adicionar um Dropout de 20% após cada camada MaxPooling. Comente os resultados obtidos.

