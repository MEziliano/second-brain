# Semana 02 - 

### 01 

Selecione abaixo a alternativa que apresenta alguns dos métos usados para realce de imagens digitais.

[❌] a. Mudança de perspectiva,  suavização, transformação exponencial e  limiarização.

[❌] b. Negativo da Imagem,  suavização, transformação exponencial e translação.

[❌] c. Negativo da Imagem,  suavização, transformação exponencial e  limiarização.

[☑️] d. Negativo da Imagem, transformação logarítmica,transformação exponencial e  limiarização.

>**Justificativa técnica**:
Esses quatro métodos são técnicas clássicas de realce por transformação de intensidade (point processing), amplamente descritas na literatura de processamento digital de imagens (ex.: Gonzalez & Woods):
* **Negativo da imagem**: inverte a faixa de intensidade, útil para realçar detalhes em imagens escuras.
* **Transformação logarítmica**: comprime a faixa dinâmica de valores altos e expande os valores baixos, realçando regiões escuras.
* **Transformação exponencial** (também chamada de lei de potências ou gama): ajusta o contraste de forma não linear, realçando claras ou escuras conforme o valor do expoente.
* **Limiarização**: converte a imagem em binária, realçando estruturas e contornos ao separar objeto e fundo.
 ---


### 2 multipla escolha
Associe a técnica de realce com suas respectivas propriedades.

* Inverte os tons de cinza, não possui muito uso prático.
**[RESPOSTA]** Negativo da imagem

* Interessante para realçar parte escura de uma imagem.
**[REPOSTA]** transformação logarítmica

* Interessante para realçar parte clara de uma imagem.
**[RESPOSTA]** transformação exponencial

* Recomendado para quando uma imagem possuí valores mal distribuídos, ou seja, o contraste foi mal explorado.
**[RESPOSTA]** modificação do histograma

----

### QUESTÃO 3

"Aplicação exige ancorar um pixel para aplicar a convolução com o filtro, normalmente o pixel central. Posiciona o pixel âncora no pixel que desejamos filtrar."

A afirmação acima se refere a qual tipo de filtragem de imagens digitais?

[ ] a.  Agudização.

[ ] b.  Suavização.

[ ] c. Análise de histograma.

[☑️] d. Processamento por máscara.

---

### Questão 4 

Associe a métrica de qualidade de imagem com sua respectiva equação

 * $ 
MAE  = \dfrac{1}{MN} \sum^m_{x=1} \sum^n_{y=1} |f(x,y) - g(x,y)| 
$, Erro médio absoluto

* $MSE  = \dfrac{1}{MN} \sum^m_{x=1} \sum^n_{y=1} [f(x,y) - g(x,y)] ^2
$, erro médio quadrático, 
* $ PSNR = 10\log_{10}(\dfrac{L^2_{max}}{MSE})
$, relação sinal-ruído de pico 

* $ME = max|f(x,y) - g(x,y)|
$ erro médio

---

### Questão 5
Em um sistema de análise de imagem, diferentes transformações geométricas podem ser aplicadas a uma imagem, alterando sua aparência de maneiras distintas. Considerando o impacto dessas transformações, qual delas modifica a relação espacial entre objetos na imagem de maneira não linear, distorcendo a profundidade e a perspectiva dos elementos?

[❌] a.  Rotação

[☑️] b. Transformação de perspectiva

[❌] c.  Translação

[❌] d.  Análise de distribuição de frequências

---
### Questão 6

Suponha que exista uma imagem armazenada na variável Im. A seguir, o seguinte código é rodado.

Im = cv2.subtract(255,Im)

Qual o conteúdo da nova variável Im ?

[☑️] a. Uma imagem com o negativo da imagem armazenada em Im.

[❌] b. Uma imagem com a parte clara realçada em relação à imagem armazenada em Im.

[❌] c. Uma imagem com a subtração dos pixels da imagem armazenada em Im.

[❌] d. Uma imagem com a transformação logaritmica da imagem armazenada em Im.

---
### Questão 7

Associe a imagem com a técnica de realce que foi aplicada.


----

### Questão 8

Considere a imagem abaixo:

