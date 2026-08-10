# Semana 03 - Cor, Segmentação de Imagens e Descritores de Objeto

- **AULA 7:** Cor, Percepção da Cor e Espaço de Cores
- **AULA 8:** Segmentação
- **AULA 9:** Segmentação via CNN e Descritores de Objeto
- **Aula Prática 5:** Espaços de Cores
- **Desafio 5:** Limiarização Global em Espaço RGB
- **Aula Prática 6 **
    - Parte 1: Limiarização e detecção de bordas
- **Desafio 6: Avaliação do modelo U-net**
    - Parte 2: U-net (Rede Neural Convolucional)
- **Aula Prática 7: Descritores de Objeto**
- **AVALIAÇÃO ONLINE 3**


## Aula 07 - Cor e Percepção de cores

[VIDEO](https://www.youtube.com/watch?v=FwcUht_EULU&time_continue=2&embeds_referring_euri=https%3A%2F%2Fava.ufv.br%2F&embeds_referring_origin=https%3A%2F%2Fava.ufv.br)

A imagem pode ser representadas de diversas formas. Computacionalmente, sempre através de uma matriz. 
No olho humano, através das partes específicas dos olhos. Como as córneas, cristalino, retina, íris e o nervo óptico. Na retina, ficam os cones e os bastonetes, que são responsáveis por enxergar as cores. 
A cor é:
* Sensação humana de diferentes esprectros de luz.
* Característicamente perceptual da espécie humana.
* Podemos representar a cor usando um número pequeno e finito de sensores. 

A percepção da cor, por meio da computação é feita através da combinação de pixies. Podendo ser por meio de: 
* Cores aditivas **(RGB)**, onde a soma das cores é igual ao **branco**;
* Cores subtrativas **(CYMK)**, onde remoção das cores é igual ao **preto**.

A absorção ou a refletância de cada comprimento de cor dá a percepção da cor. 

### Descritores da luz
**Matiz**
    * Cor
    * Comprimento de onda  dominante no espectro.

**Saturação**
    * Descreve a brancura de uma luz
    * Quanto menos saturado, mais branco
    * Quanto mais saturado, mais o espectro é concentrado.

**Brilho**
    * Brilho é um atributo de percepção do sistema visual que faz com uma área parece emitir mais ou menos.

### Brilho, intensidade e luminância
* **Intesidade**
    * É a mensuração da potência irradiada da (ou incidente) superfície de um determinado intervalo do espectro magnético( ex.:Watts/m2). Não representa linearmente o brilho.

* **Liminância**
    * É a potência radiante PONDERADA por uma função espectral de sensibilidade que é característica do sistema de visão. Mais pŕoxima do nosso SVH (sistema visual humano).
    * Candelas/m2
    * Na prática, normalizada para 1 com respeito a um "branco".
    * Luminância é proporcional a potência da luz refletida pelo objeto. Nesse sentido luminância é PARECIDO com a intesidade. Porém a composição espectral da luminância está relacionada com a sensibilidade do brilho do sistema visual humano

### Visão colorida
* Cor é o resultado da percpeção da luz, é uma sensação cerebral
* Espectro existe no mundo físico, porém a cor existe somente no olho e no cérebro.
* Brilho, matiz e saturação são atributos de percepção de cor.
* Matiz + saturação = Cromaticidade


### Espaço de cores
* **CUE XYZ**
 * Sistema virtual de cores primárias no qual todos os valores triestímulos são positivos.
    * Y = luminância
    * xz - cromaticidade

* **HSV** - *Hue, Saturation, Value (Brightness)*
* Cromaticidade e Luminância são codificados separadamente.
* No OpenCv
    * Hue - 0 a 179 (pois anda de 2 em 2 graus)
    * S - 0 a 255 
    * Value - 0 a 255


* **CIELAB (L*a*b)**
    * Derivado do CIE XYZ
    * Independe do instrumento
    * Light a (verde/vermelho )e o b (azul/amarelo) as respectivas cores.
    * OpenCV: L - 0; a - 0 a 255; b - 0 a 255
    * Cromaticidade e Luminância são codificados separadamente

* **RGB**
    * Misturam a cromaticidade com luminância na codificação

## Aula 08 - Segmentação de objetos e descritores de forma

[VIDEO](https://youtu.be/ucUCzOaKMKY)
### Segmentação
* **Limiarização**
    1. **Global**: Funciona especialmente em casos de imagens com histogramas bimodais, podendo ser divididas adequadamente com um único valor.
    2. **Adaptativa**: Um limite global pode não ser bom em todos os casos. Aqui, o algoritmo determina o limite para um pixel com base em uma pequena região ao seu redeor. Assim, obtemos limiares diferentes para diferentes regiões da mesma imagem, o que dá melhores resultados para imagens com iluminação variável. 
    3. **Otsu**: Algoritmo de limiarização, proposto por Nobuyuki Otsu [Otsu, 1979]. Determinao valor ideial de um *threshold* que separe os elementes do fundo e da frente da imagem em dois clusters atribuindo a cor branca ou prete para cada um deles. 

* **Detecção de borda**
    * **Sobel**
        * Sobel e Feldman, 1968
        * Filtro Gaussiano
    * **Operador Canny**
        * John F. Canny, 1986
        * Operador Sobel (intensidade)
        * Magnitude do gradiente de direção
        * Supressão de bordas
        * Histerese 

### Descritores de objeto - Forma 
                    Área
Perímetro               - Comprimento
Compacidade - Exetricidade - Retangularidade
Centriode - Orientação - Fator de forma -    Contorno convexo - solidez

------
## Aula 09 -  Segmentação de Imagem via CNN e Descritores de Textura

[VIDEO](https://youtu.be/EtWLving1Lo)

#### Segmentação de Imagens via CNN
1. **Classe 1**: Pixel pertencente ao animal de estimação. 
2. **Classe 2**: Pixel na fronteira do animal de estimação
3. **Classe 3**: Nenhuma das opções acima/Pixel circulante. 


### Descritores de objeto - Textura
Contraste
Dissimilaridade - Homogeneidade
Energia - Correlação - Entropia - Segundo Momento da Média  - *Local Binary Patterns (LBP)*

### Sistema para processamento
**Aquisição >> Pré-processamento >> Segmentação >> Representação >> Interpretação**
