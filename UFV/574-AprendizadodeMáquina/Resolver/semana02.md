# Questionário

### Questão 1
Redes neurais artificiais foram baseadas nas conexões neuronais biológicas. Assinale a alternativa correta.

a. O perceptron é a modelagem matemática de um neurônio biológico, possuindo 'n' saídas conforme modelagem do projetista ('n' é um número inteiro).

b. O perceptron é a modelagem matemática de um neurônio biológico, possuindo apenas uma saída que pode ser a entrada de outro neurônio artificial.

c. O perceptron é a modelagem matemática múltiplos neurônios biológicos, possuindo diversas saídas que podem ser a entrada de outros neurõnios artificiais.

d. O perceptron é a modelagem matemática de um neurônio biológico, possuindo diversas saídas que podem ser as entradas de outros neurônios artificiais.

> Alternativa B, cada neurõnio pode possuir diversas entradas, mas possi apenas uma saida.

### Questão 2 
Associe a função de ativação com sua respectiva equação.
* Sigmoide
* Degrau unitário
* Tangente hiperbólica
* Sinal


### Questão 3 

Suponha uma rede PMC composta por uma camada de entrada com 10 neurônios, conectada com uma camada escondida com 50 neurônios artificiais e uma camada de saída com 3 neurônios artificiais, para amostras de dados contendo 10 características. Todos os neurônios utilizam a função de ativação ReLU.

Qual é o formato da entrada X? 

a. 1x10 (1 linha e 10 colunas)
b. 50X50 (50 linhas e 50 colunas)
c. 10X10 (10 linhas e 10 colunas)
d. 50X1 (50 linhas e uma coluna)

> 1x10 (1 linha e 10 colunas)

### Questão 4

Suponha uma rede PMC composta por uma camada de entrada com 10 neurônios, conectada com uma camada escondida com 50 neurônios artificiais e uma camada de saída com 3 neurônios artificiais, para amostras de dados contendo 10 características. Todos os neurônios utilizam a função de ativação ReLU.

Quais são os formatos das matrizes de pesos (Wh) e de limiares de ativação (bh) da camada escondida? 
a. Pesos: 1x10
    Limiares: 10x10
b. Pesos: 10x50
     Limiares: 1x50
c. Pesos: 10x10
    Limiares: 10x50
d. Pesos: 1x50
     Limiares: 10x50

> Pesos: 10x50
> Limiares (Biases): 1x50

### Questão 5
Suponha uma rede PMC composta por uma camada de entrada com 10 neurônios, conectada com uma camada escondida com 50 neurônios artificiais e uma camada de saída com 3 neurônios artificiais, para amostras de dados contendo 10 características. Todos os neurônios utilizam a função de ativação ReLU.

Quais são os formatos das matrizes de pesos (Wo) e da matriz de limiares de ativação (bo) da camada de saída?

a. Pesos: 50x3
    Limiar: 1x3
b. Pesos: 50x3
     Limiar: 10x3
c. Pesos: 50x10
    Limiar: 50x3
d. Pesos: 3x10
    Limiar: 3x3

> Pesos: 50x3
> Limiar (Bias): 1x3

### Questão 6
Suponha uma rede PMC composta por uma camada de entrada com 10 neurônios, conectada com uma camada escondida com 50 neurônios artificiais e uma camada de saída com 3 neurônios artificiais, para amostras de dados contendo 10 características. Todos os neurônios utilizam a função de ativação ReLU.

Qual o formato da saída Y da rede PMC?

a. Saida: 1x3
b. Saida: 10x3
c. Saida: 50x3
d. Saida: 3x3

> Saída: 1x3

### Questão 7
Qual o menor número de neurônios na camada de saída necessário para uma rede PMC classificar um e-mail em "Spam" ou "Não-spam"? Qual função de ativação deve ser utilizada na camada de saída desta rede PMC?

a. Apenas um neurônio de saída com função de ativação ReLU.
b. Apenas um neurônio de saída com função de ativação degrau unitário.
c. Dois neurônios de saída com função de ativação sigmoide.
d. Dois neurônios de saída com função de ativação sinal.

>  Resposta Correta: Alternativa B
> Apenas um neurônio de saída com função de ativação degrau unitário.


### Questão 8
Se você quiser construir uma rede neural artificial que identifique números escritos a mão, de 0 a 9, qual o número mínimo de neurônios necessários na camada de saída da rede? Qual função de ativação deve ser utilizada?

a. Dez neurônios de saída com função de ativação softmax.
b. Dez neurônios de saída com função de ativação ReLU.
c. Dez neurõnios de saída com função de ativação degrau sinal.
d. Dez neurõnios de saída com função de ativação logística.

> Resposta Correta: Alternativa A
> Dez neurônios de saída com função de ativação softmax.


### Questão 9
Qual função de ativação é necessária para que uma rede PMC seja de classificação binária?

a. Função de ativação ReLU.
b. Função de ativação tangente hiperbólica.
c. Função de ativação degrau unitário.
d. Função de ativação sigmoide.

> Alternativa D
> Função de ativação sigmoide.

### Questão 10 

Questão 10

Uma rede neural artificial com 'n' neurônios de saída e função de ativação degrau unitário pode ser usada na classificação de elementos com até 2^n (2 elevado a n) classes.

Escolha uma opção:
* Verdadeiro
* Falso

> Verdadeiro