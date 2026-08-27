# Questionário 

### Questão 1
Que tipo de problema o dataset pretende resolver?

A.O problema que trata o dataset é o de regressão, com o objetivo de estimar o preço de casas.
B. O problema que trata o dataset é o de classificação, com o objetivo de estimar qual categoria cada casa pertence.
C. O problema que trata o dataset é o de clusterização, com o objetivo de juntar grupos de casas que se relacionam de alguma maneira.
D. O problema que trata o dataset é o de regressão, com o objetivo de estimar o número de moradores em uma casa.
E. O problema que trata o dataset é o de classificação, com o objetivo de estimar o lugar onde fica determinada casa.

> O foco do dataset é prever o valor de uma casa dada as suas características do banco de dados. Como o problema tenta prever um número em um intervalo contínuo, este é um problema de regressão.
---

### Questão 2
Qual é a variável do problema que um modelo de aprendizado de máquina pode ter como valor alvo (desejado)?

A. Price
B. Address
C. Date
D. Regionname
E. Method

> O dataset procura prever preço de casas baseados em suas características, logo, a variável alvo é "Price", que é a variável referente ao preço da casa.

----

### Questão 3

Assinale todas as alternativas que apresentam o nome das variáveis presentes no dataset:
OBS: Marcar uma alternativa incorreta anula o acerto de uma alternativa marcada corretamente.

A.Address
B.Bedroom2
C.Longtitude
D.Distance
E.Number_of_Bathrooms
F.YearSale
G.ocean_proximity
H.Median

> *Address, Bedroom2, Longitude, Distance*

----

### Questão 4
Quantas amostras estão presentes no dataset?

> *13580*

------
### Questão 5

Quantos dados estão presentes no dataset?

A.21
B.13580
C.285180
D.135800
E.206400

> O dataset possui 13580 amostras com 21 variáveis cada, logo: 13580 * 21 = 285180

-----

### Questão 6

Todas as alternativas abaixo apresentam uma variável qualitativa, exceto:

A.Date
B.Type
C.Regionname
D.Method
E.Rooms

> A variável "Rooms" é uma varíavel quantitativa, pois, representa uma quantidade (neste caso, o número de quartos na casa).
É possível observar também que todas as outras variáveis no banco de dados são do tipo "object".

----


### Questão 7

Determine se as variáveis a seguir são discretas ou contínuas:


1 - Price Em branco 1 Contínua

2 - Rooms Em branco 2 Discreta
 
3 - Longtitude Em branco 3 Contínua
 
4 - YearBuilt Em branco 4 **discreta**
 
5 - Lattitude Em branco 5 Contínua

> A variável "Rooms" é uma variável discreta, já que não existe 1.5 quartos, apenas valores inteiros.
"YearBuilt" também é discreta, já que se trata do ano de construção da casa, e não há motivos para colocar que a casa foi construida no ano 1990.1. Todas as outras variáveis são discretas por apresentarem variações nas casas decimais e isto pode ser visto nos dados
 
-----
### Questão 8

Qual das alternativas abaixo apresenta a variável com maior número de dados faltantes ou inválidos?

A. BuildingArea
B. CouncilArea
C. Car
D. Method
E. Regionname

> BuildingArea possui 7130 dados não faltantes.
> CouncilArea possui 12211 dados não faltantes.
> Car possui 13518 dados não faltantes.
> Method possui 13580 dados não faltantes.
> Regionname possui 13580 dados não faltantes.

----

### Questão 9

Qual das variáveis quantitativas do dataset apresenta maior grau de correlação em relação à variável alvo?


A. LandSize
B. BuildingArea
C.YearBuilt
D. Rooms
E. Bedroom2

> LandSize possui coeficiente de correlação igual a 0.037.
BuildingArea possui coeficiente de correlação igual a 0.091.
YearBuilt possui coeficiente de correlação igual a -0.324.
Rooms possui coeficiente de correlação igual a 0.497.
Bedroom2 possui coeficiente de correlação igual a 0.476. 


----
### Questão 10

"O OrdinalEncoder é frequentemente usado para codificar variáveis categóricas nominais (categorias sem uma ordem implícita), ele também pode ser usado para codificar variáveis categóricas ordinais (categorias com uma ordem implícita). No entanto, o OneHotEncoder é especificamente projetado para lidar com variáveis categóricas ordinais e é geralmente mais adequado para esse propósito."

A afirmativa anterior é:
Questão 10Escolha uma opção:
Verdadeiro
Falso 

> Falso