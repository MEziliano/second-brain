# Semana 03 - Cor, segmentação de imagens e descritores

## Questão 01 

Qual é a principal função das camadas de filtragem em uma Rede Neural utilizada para o processamento de imagens?

* A. Realizar a convolução entre os filtros e a imagem para extrair características relevante
* B. Aplicar funções de ativação como ReLU para tornar a rede mais complexa
* C. Agrupar características extraídas em camadas intermediárias
* D. Classificar a imagem de entrada
* E. Reduzir o tamanho da imagem de entrada para economizar recursos computacionais


### Camadas de Filtragem em CNNs

| **Tópico** | **Detalhes** |
| :--- | :--- |
| **Conceito Central** | Camadas de filtragem (convolucionais) em redes neurais para processamento de imagens. |
| **Função Principal** | **Extrair características** (*features*) da imagem, como bordas, texturas e padrões, através da operação matemática de **convolução** entre os filtros (*kernels*) e a matriz de pixels da imagem. |
| **Distratores Comuns** | • *Pooling*: Reduz dimensionalidade e agrupa características (Opções C e E).<br>• *Ativação (ReLU)*: Adiciona não-linearidade, mas é uma etapa complementar aplicada *após* a convolução (Opção B).<br>• *Camadas Densas*: Realizam a classificação final com base nas características extraídas (Opção D). |


Análise das Alternativas
> * A. Correta.  A convolução é a operação fundamental dessas camadas para criar mapas de características (feature maps).
> * B. Incorreta. A ReLU é uma função de ativação, não a função primária da camada de filtragem em si.
> * C e E. Incorretas. Descrevem a função das camadas de Pooling (ex: Max Pooling), que geralmente vêm depois da convolução.
> * D. Incorreta. A classificação é tarefa das camadas finais (Fully Connected / Dense).


## Questão 02 
Após realizar uma segmentação adequada em uma imagem, obtêm-se uma imagem binária com a borda do objeto segmentado. Qual informação NÃO pode extraída dessa imagem obtida? 

* A. Área 
* B. Orientação
* C. Retangularidade
* D. Histograma de cor
* E. Centroide


### Extração de Características em Imagens Binárias

| **Tópico** | **Detalhes** |
| :--- | :--- |
| **Conceito Central** | Uma imagem **binária** contém apenas dois valores (ex: 0 e 1, ou preto e branco), representando a presença (objeto) ou ausência (fundo). |
| **O que se perde** | Toda a informação de **cor** e, muitas vezes, de **textura** fina da imagem original. |
| **O que se mantém** | Informações **geométricas** e **morfológicas** (forma, tamanho, posição e distribuição espacial dos pixels). |

> Análise das Alternativas
> * A. Área: Pode ser extraída (contando o número de pixels com valor "1" dentro da borda).
> * B. Orientação: Pode ser extraída calculando os momentos da imagem (eixo principal da forma).
> * C. Retangularidade:  Pode ser extraída (razão entre a área do objeto e a área do seu retângulo delimitador / bounding box).
> * D. Histograma de cor:  **NÃO pode ser extraído**. Um histograma de cor mapeia a frequência de diferentes cores (canais RGB, HSV, etc.). Como a imagem é binária, ela só tem 1 ou 2 "cores" (preto e branco), tornando impossível recuperar o histograma de cor do objeto original a partir apenas dela.
> * E. Centroide: Pode ser extraído calculando o centro de massa (média das coordenadas X e Y dos pixels do objeto).



## Questão 03

A seguir estão técinicas de segmentação de imagens, EXCETO:
* A. Detecção de bordas
* B. Cluster
* C. Filtragem
* D. Watershed
* E. Limiarização


###  Técnicas de Segmentação de Imagem

| **Tópico** | **Detalhes** |
| :--- | :--- |
| **Conceito Central** | Segmentação é o processo de partitionar uma imagem em múltiplos segmentos (conjuntos de pixels) para simplificar sua representação e facilitar a análise. |
| **Técnicas de Segmentação** | • **Limiarização (Thresholding):** Separa por intensidade (ex: Otsu).<br>• **Detecção de Bordas:** Encontra descontinuidades para delimitar regiões.<br>• **Clustering (Agrupamento):** Agrupa pixels similares (ex: K-Means).<br>• **Watershed (Bacia Hidrográfica):** Abordagem morfológica baseada em topografia. |
| **O que NÃO é Segmentação** | **Filtragem** (suavização, realce) é uma etapa de **pré-processamento** ou **realce**, usada para preparar a imagem, mas não para partitioná-la em regiões de interesse por si só. |

---

###  Análise das Alternativas

*   **A. Detecção de bordas:**  (É técnica de segmentação). Usada para encontrar os contornos que separam diferentes regiões.
*   **B. Cluster:**  (É técnica de segmentação). Algoritmos como K-Means agrupam pixels com características similares (cor, textura) sem rótulos prévios.
*   **C. Filtragem:**  **EXCEÇÃO (Resposta Correta).** A filtragem (ex: filtro da média, Gaussiano, mediana) altera os valores dos pixels para reduzir ruído ou realçar características, mas **não** divide a imagem em regiões ou objetos segmentados. É uma etapa de *pré-processamento*.
*   **D. Watershed:**  (É técnica de segmentação). Trata a imagem como um relevo topográfico e "inunda" as bacias para separar objetos tocando-se.
*   **E. Limiarização:**  (É técnica de segmentação). A forma mais básica de segmentação, convertendo a imagem em binária com base em um valor de corte de intensidade.


## Questão 04

"O processo de _________, quando necessário, tem o objetivo de dividir a imagem inicial em vários objetos de interesse, conforme a significância deles para a reconstituição plena da imagem ou partes específicas de interesse."
Após a leitura do texto acima, assinale a opção que completa corretamente a lacuna vazia:

* A. Aquisição
* B. Predição
* C. Pré-processamento
* D. Segmentação
* E. Representação


###  Etapas do Pipeline de Visão Computacional

| **Tópico** | **Detalhes** |
| :--- | :--- |
| **Conceito Central** | A palavra-chave da questão é **"dividir a imagem... em vários objetos de interesse"**. Isso é a definição de livro-texto de **Segmentação**. |
| **Pipeline Clássico** | 1. **Aquisição:** Captura da imagem.<br>2. **Pré-processamento:** Melhoria da imagem (ex: remover ruído, ajustar contraste).<br>3. **Segmentação:** **Divisão** da imagem em regiões ou objetos de interesse.<br>4. **Representação/Descrição:** Extrair *features* (área, perímetro, cor) dos objetos segmentados.<br>5. **Reconhecimento/Classificação:** Rotular o objeto (ex: "é uma bola"). |

---

### Análise das Alternativas

*   **A. Aquisição:**  Incorreta. É apenas a captura da imagem pelo sensor/câmera.
*   **B. Predição:**  Incorreta. Termo mais associado a modelos estatísticos/ML, não à etapa de divisão espacial da imagem.
*   **C. Pré-processamento:**  Incorreta. Prepara a imagem (ex: suavizar), mas não a divide em objetos.
*   **D. Segmentação:** **Correta.** Segmentar significa literalmente dividir em segmentos (partes ou objetos de interesse), isolando-os do fundo (*background*).
*   **E. Representação:**  Incorreta. Ocorre *após* a segmentação. É o processo de transformar o objeto segmentado em uma forma adequada para processamento computacional (ex: contornos, esqueletos).



## Questão 05 

Qual é a diferença entre as funções `cv2.threshold` e `cv2.adaptiveThreshold`?


A. A função `cv2.threshold` aplica um valor de limiar constante para todos os pixels da imagem, enquanto a função `cv2.adaptiveThreshold` aplica um valor de limiar variável para cada pixel da imagem, baseado em uma janela gaussiana

B. A função `cv2.threshold` calcula um valor de limiar ótimo para toda a imagem, enquanto a função `cv2.adaptiveThreshold` aplica um valor de limiar arbitrário para cada pixel da imagem

C. A função `cv2.threshold` aplica um valor de limiar fixo para todos os pixels da imagem, enquanto a função `cv2.adaptiveThreshold` calcula um valor de limiar adaptativo para cada região da imagem, levando em conta as variações de iluminação

D. A função `cv2.adaptiveThreshold` aplica um valor de limiar global para toda a imagem, enquanto a função `cv2.threshold`  aplica um valor de limiar local para cada pixel da imagem

E. A função `cv2.adaptiveThreshold` calcula um valor de limiar baseado na média dos pixels da imagem, enquanto a função `cv2.threshold` calcula um valor de limiar baseado na mediana dos pixels da imagem


---

###  Limiarização (Thresholding) no OpenCV

| **Tópico** | **Detalhes** |
| :--- | :--- |
| **Conceito Central** | Limiarização converte imagens em escala de cinza em imagens binárias (preto e branco) com base na intensidade dos pixels. |
| **Global (`cv2.threshold`)** | Aplica **um único valor** de corte para **toda a imagem**. Funciona bem apenas se a iluminação for perfeitamente uniforme. |
| **Adaptativo (`cv2.adaptiveThreshold`)** | Calcula **diferentes valores** de corte para **diferentes regiões** (blocos) da imagem, baseando-se na vizinhança local. |
| **O "Pulo do Gato"** | O método adaptativo é a solução clássica para imagens com **iluminação não uniforme** ou gradientes de luz. Ele pode usar a *Média* ou a *Soma Ponderada Gaussiana* da vizinhança. |

---

###  Análise das Alternativas

*   **A. Incorreta.**  Embora o adaptativo calcule para cada pixel, ele **não** se baseia *apenas* em uma janela gaussiana. Ele pode usar a média aritmética simples (`ADAPTIVE_THRESH_MEAN_C`) ou a gaussiana (`ADAPTIVE_THRESH_GAUSSIAN_C`). Restringir apenas à gaussiana torna a alternativa errada.
*   **B. Incorreta.**  O `cv2.threshold` padrão não calcula um valor "ótimo" automaticamente (a menos que você passe a flag específica do método de Otsu, mas a função em si recebe um valor fixo).
*   **C. Correta.**  Descreve perfeitamente a essência: o global usa um valor fixo, enquanto o adaptativo calcula limiares para diferentes regiões, sendo robusto a **variações de iluminação**.
*   **D. Incorreta.**  Inverteu completamente os conceitos das duas funções.
*   **E. Incorreta.** O `cv2.threshold` não calcula limiar baseado na mediana.

## Questão 06
Assinale a alternativa correta referente a função das linhas de código abaixo:


`blue_lower = 0`
`blue_upper = 200`
`mask = (blue >= blue_lower) & (blue <= blue_upper)`
`bc = blue.copy()`

* A. A função das linhas de código é criar uma cópia da imagem original e zerar os valores dos pixels que não estão no intervalo de azul definido
* B. A função das linhas de código é criar um vetor com os valores dos pixels azuis da imagem e plotar um histograma com eles
* C. A função das linhas de código é segmentar a imagem em três canais de cores e aplicar um filtro azul em cada um deles
* D. A função das linhas de código é criar uma máscara que seleciona apenas os pixels azuis da imagem e cria uma nova imagem com eles
* E. A função das linhas de código é converter a imagem para o espaço de cores HSV e extrair a matiz azul da imagem




### Segmentação por Cor com NumPy

| **Linha de Código** | **O que faz** |
| :--- | :--- |
| `blue_lower = 0` / `blue_upper = 200` | Define os **limites inferior e superior** do intervalo de interesse do canal azul. |
| `mask = (blue >= blue_lower) & (blue <= blue_upper)` | Gera uma **máscara booleana** (`True`/`False`): `True` onde o pixel de azul está dentro do intervalo, `False` caso contrário. |
| `bc = blue.copy()` | Cria uma **cópia (nova imagem)** a partir do canal/arranjo azul, que servirá de base para aplicar a segmentação. |

---

### Análise das Alternativas

*   **A. Incorreta.**  O código cria a cópia, mas **não há nenhuma linha zerando pixels** (ex: `bc[~mask] = 0`). Essa operação viria *depois*.
*   **B. Incorreta.**  Não há vetorização para histograma nem chamada de plotagem (`plt.hist`).
*   **C. Incorreta.**  O código não separa a imagem em 3 canais (BGR/RGB) nem aplica filtros.
*   **D. Correta.**  A lógica é exatamente: criar uma **máscara booleana** que isola os pixels de azul dentro do intervalo e criar uma **nova imagem (cópia)** associada a esses pixels.
*   **E. Incorreta.**  Não há nenhuma conversão para **HSV** (ex: `cv2.cvtColor(img, cv2.COLOR_BGR2HSV)`) nem extração de matiz.


## Questão 07 

Qual é o efeito da função `cv2.threshold(I,127,50,cv2.THRESH_BINARY)`?

* A. Aplica um limiar fixo de 127 à imagem I e atribui o valor de 50 aos pixels acima do limiar
* B.  Aplica um limiar fixo de 50 à imagem I e atribui o valor de 127 aos pixels abaixo do limiar
* C. Aplica uma escala de cinza na imagem utilizando uma normalização em 127
* D. Aplica um limiar fixo de 127 à imagem I e atribui o valor de 50 aos pixels abaixo do limiar
* E. Aplica um limiar fixo de 50 à imagem I e atribui o valor de 127 aos pixels acima do limiar


### `cv2.threshold` no OpenCV

| **Tópico** | **Detalhes** |
| :--- | :--- |
| **Assinatura da Função** | `cv2.threshold(src, thresh, maxval, type)` |
| **Parâmetros do Exemplo** | • `src` = `I` (imagem de entrada)<br>• `thresh` = `127` (valor do limiar)<br>• `maxval` = `50` (valor máximo atribuído)<br>• `type` = `cv2.THRESH_BINARY` |
| **Lógica do `THRESH_BINARY`** | • Se `pixel > thresh` (127) → recebe o valor `maxval` (50).<br>• Se `pixel <= thresh` (127) → recebe o valor `0`. |

---

###  Análise das Alternativas

*   **A. Incorreta.**  Aplica o limiar fixo de 127 e, pela regra do `THRESH_BINARY`, atribui o `maxval` (50) aos pixels que estão **acima** desse limiar. (Os abaixo ou iguais viram 0).
*   **B. Incorreta.**  Inverteu os valores de `thresh` e `maxval`.
*   **C. Incorreta.**  A função não faz conversão de escala de cinza ou normalização, ela binariza.
*   **D. Correta.**  No `THRESH_BINARY`, os pixels *abaixo* do limiar recebem `0`, não o `maxval`. (Isso seria o comportamento do `THRESH_BINARY_INV`).
*   **E. Incorreta.**  Novamente, inverteu os valores de `thresh` e `maxval`.


## Questão 08 

Qual é o objetivo da linha de código:
"`cv2.imread('/drive/caminho/generico/sudoku.jpg', cv2.IMREAD_GRAYSCALE)`"

* A. Ler uma imagem colorida do sudoku e converter para escala de cinza
* B. Apenas lê a imagem colorida do sudoku
* C. Ler uma imagem em escala de cinza do sudoku e converter para colorida
* D. Ler uma imagem em escala de cinza do sudoku e aplicar um filtro de mediana
* E. Ler uma imagem colorida do sudoku e aplicar um filtro de mediana

###  Leitura de Imagens com `cv2.imread`

| **Tópico** | **Detalhes** |
| :--- | :--- |
| **Assinatura da Função** | `cv2.imread(filename, flags)` |
| **Parâmetros do Exemplo** | • `filename` = `'/drive/caminho/generico/sudoku.jpg'`<br>• `flags` = `cv2.IMREAD_GRAYSCALE` (ou `0`) |
| **Comportamento da Flag** | A flag `IMREAD_GRAYSCALE` instrui o OpenCV a **descartar os canais de cor** (RGB/BGR) durante a leitura e carregar a imagem diretamente como uma matriz 2D de **escala de cinza** (onde cada pixel representa apenas a intensidade/luminosidade). |
---
### Análise das Alternativas

*   **A. Correta.**  A imagem original (`.jpg`) é colorida, mas a flag `cv2.IMREAD_GRAYSCALE` faz com que o OpenCV a leia e a **converta para escala de cinza** imediatamente, resultando em uma matriz 2D em vez de 3D.
*   **B. Incorreta.**  Se quisesse apenas ler a imagem colorida, a flag seria `cv2.IMREAD_COLOR` (ou `1`, que é o padrão).
*   **C. Incorreta.**  Faz o oposto do que a flag propõe.
*   **D e E. Incorretas.**  A função `cv2.imread` apenas carrega a imagem. Para aplicar filtros (como o de mediana), seria necessário chamar outra função posteriormente, como `cv2.medianBlur()`.

## Questão 09 

Assinale a alternativa que representa a função das linhas de código a seguir:

`im2 = cv2.imread('/content/drive/MyDrive/ELT578/SEMANA_3/cow.jpg', cv2.IMREAD_GRAYSCALE)`
`cow_new = cv2.Sobel(im2,-1,1,0)`
`print(cow_new.dtype)`
`print(cow_new.min)`
`print(cow_new.max)`
`cow_new= (cow_new.astype(float)-cow_new.min())/(cow_new.max()-cow_new.min())*255`
`cow_new = np.uint8(cow_new )`
'cv2_imshow(cow_new)'

A. Aplicar o operador de Sobel na imagem em escala de cinza, normalizar os valores dos pixels entre 0 e 255, converter o tipo de dados para inteiro sem sinal de 8 bits e mostrar a imagem resultante

B.Aplicar o operador de Canny na imagem em escala de cinza, normalizar os valores dos pixels entre -1 e 1,  converter o tipo de dados para ponto flutuante de 32 bits e mostrar a imagem resultante


C.Aplicar o operador de Laplace na imagem em escala de cinza, normalizar os valores dos pixels entre 0 e 255, converter o tipo de dados para inteiro sem sinal de 8 bits e mostrar a imagem resultante


D.Aplicar o operador de Sobel na imagem em escala de cinza, normalizar os valores dos pixels entre 0 e 1, converter a imagem para HSV e mostrar a imagem resultante


E.Aplicar o operador de Canny na imagem em escala de cinza, normalizar os valores dos pixels entre 0 e 255, converter o tipo de dados para inteiro sem sinal de 8 bits e mostrar a imagem resultante



### Pipeline de Detecção de Bordas e Normalização

| **Trecho de Código** | **Função no Pipeline** |
| :--- | :--- |
| `cv2.imread(..., IMREAD_GRAYSCALE)` | Carrega a imagem já convertida para 1 canal (escala de cinza). |
| `cv2.Sobel(im2, -1, 1, 0)` | Aplica o **Operador de Sobel** para calcular o gradiente (bordas) na direção X (`dx=1, dy=0`). O `-1` mantém o mesmo tipo de dado da entrada. |
| `(... - min) / (max - min) * 255` | Aplica a **Normalização Min-Max**. Escala os valores dos pixels para ficarem estritamente no intervalo de **0 a 255**. |
| `np.uint8(...)` | Converte os valores normalizados (que agora são `float`) de volta para **inteiro sem sinal de 8 bits** (`uint8`), que é o formato padrão para exibição de imagens. |
| `cv2_imshow(...)` | Exibe a imagem final resultante. |
---
###  Análise das Alternativas

*   **A. Correta.**  Descreve perfeitamente a sequência: Sobel -> Normalização (0-255) -> Conversão para `uint8` (inteiro sem sinal de 8 bits) -> Exibição.
*   **B e E. Incorretas.**  O código usa `cv2.Sobel`, não `cv2.Canny`.
*   **C. Incorreta.**  O código usa `cv2.Sobel`, não o operador de Laplace (`cv2.Laplacian`).
*   **D. Incorreta.**  A normalização multiplica por 255 no final (indo de 0 a 255, não de 0 a 1) e converte para `uint8`, não para o espaço de cor HSV.