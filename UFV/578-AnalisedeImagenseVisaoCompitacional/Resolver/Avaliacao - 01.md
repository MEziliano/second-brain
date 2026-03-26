# Semana 01 - Introdução, conceitos e terminologias

### 01 
Relacione as definições de tabela com os termos correspondentes:

* Refere-se à aplicação de técnicas para melhorar, modificar ou extrair informações de uma imagem digital. Isso pode envolver operações como ajuste de contraste, filtragem, realce de bordas, remoção de ruído e outras manipulações destinadas a melhorar a qualidade ou extrair características específicas da imagem. O objetivo principal deste é preparar a imagem para uma possível classificação ou melhorar sua utilidade.

**[RESPOSTA]** PROCESSAMENTO

* Processo de examinar uma imagem ou um conjunto de imagens para extrair informações ou conhecimentos específicos. Isso envolve a aplicação de algoritmos e técnicas para detectar características, objetos ou padrões na imagem. Este é usado em várias aplicações, como reconhecimento de padrões, detecção de objetos, análise médica e muito mais.

**[RESPOSTA]**  ANÁLISE DE IMAGEM 

* O campo que engloba os outros termos, mas também inclui a interpretação e compreensão do conteúdo visual por sistemas de computador. Isso envolve a capacidade de sistemas computacionais de "ver" o mundo como os seres humanos, identificando objetos, entendendo o contexto visual e tomando decisões com base nas informações visuais. Este é usado em uma variedade de aplicações, desde sistemas de segurança que detectam intrusões até carros autônomos que navegam com base na análise de imagens.

**[RESPOSTA]** VISÃO COMPUTACIONAL

### 02 
Relacione as definições da tabela com os termos correspondentes.
* Este se refere à quantidade de luz presente em uma imagem ou em uma cena. É um componente crítico da qualidade da imagem, pois afeta diretamente a visibilidade e a percepção dos detalhes na imagem. Este pode ser ajustado por meio de configurações de exposição em câmeras fotográficas ou de vídeo, bem como por meio de edição pós-produção em programas de software. Esta característica é essencial para garantir que os detalhes na imagem sejam visíveis e para evitar áreas superexpostas (muito claras) ou subexpostas (muito escuras).

**[RESPOSTA]** BRILHO

* Refere-se à quantidade total de pixels ou pontos que compõem uma imagem digital. Ela é medida em pixels (largura x altura), como, por exemplo, 1920x1080 (Full HD) ou 3840x2160 (4K) em vídeos. Quanto maior for essa característica, maior será a quantidade de detalhes que a imagem pode conter juntamente a uma melhor qualidade de imagem.

**[RESPOSTA]** RESOLUÇÃO ESPACIAL
**[CORREÇÃO]** RESOLUÇÃO DE IMAGEM ❗

* Este se refere à capacidade de uma imagem ou dispositivo de captura de imagens para representar detalhes finos e distinguir entre objetos separados. Ela é frequentemente medida em pixels por polegada em imagens digitais. Esta característica define o quão detalhada será a imagem. Está relacionada também à nitidez e à capacidade de representar linhas finas e detalhes em uma imagem.

**[RESPOSTA]** RESOLUÇÃO DE IMAGEM
**[CORREÇÃO]** RESOLUÇÃO ESPACIAL ❗

### 03

Assinale as alternativas que representam os principais objetivos do processamento de imagem. 

[☑️] A. ~~Inserção de ruído~~ ❗


[☑️] B. Segmentação de objetos


[☑️] C. Transformações geométricas


[☑️] D. Filtragem de ruído


[❌] E. Divisão dos dados em treinamento e validação


[❌] F. Treinamento da rede


[☑️] G. Extração de características

OBS.: Essa questão foi marcada como parcialmente correta. 

### 04
Assinale as alternativas que apresentam exemplos de SVC.


[☑️] A. Monitoramento de Câmeras de Segurança

[❌] B. Sistemas de Armazenamento em Disco

[☑️] C. Reconhecimento facial

[❌] D. Blockchain
 
[❌] E. Sistemas de recomendação

[☑️] F. Reconhecimento de Placas de Veículos

[☑️] G. Rastreamento de Movimento

[☑️] H. Análise de Expressões Faciais

[❌] I. Sistemas de Processamento de Linguagem Natural (NLP)

[❌] J. Classificação de Produtos

[❌] K. Reconhecimento de voz


### 05

Assinale a alternativa que contém a diferença entre a visão computacional e a visão humana.

A. Os sistemas de visão computacional não podem processar informações visuais em tempo real, ao contrário do sistema de visão humano.


B. A visão computacional é inerentemente mais rápida e precisa do que a visão humana.


[☑️] C. Os sistemas de visão computacional dependem de algoritmos e processamento digital de imagens, enquanto a visão humana é baseada na detecção de padrões através de redes neurais biológicas.


D. Os sistemas de visão humano têm a capacidade de aprender e se adaptar, enquanto o sistema de visão computacional é estático e não pode aprender.


E. Os sistemas de visão computacional são limitados pela resolução da câmera que captura a imagem, enquanto os sistemas humanos podem ajustar automaticamente sua acuidade visual.

### 06

Qual o padrão de cores usado na biblioteca Open-cv para manipulação de imagens?

a.RGB

b.CMYK

[☑️] c.BGR

d.GBR


### 07

Assinale abaixo a alternativa que representa o código usado para abrir uma imagem localizada em image_path, em escala de cinza,  e a armazenar na variável img usando a  biblioteca open-cv

a.`img = cv2.imread('image_path')`

[☑️]b.`img = cv2.imread('image_path', cv2.IMREAD_GRAYSCALE)`

c.`img = imgRead.IMREAD_GRAYSCALE()`

d. `img = cv2.imread('image_path')
    img = img.IMREAD_GRAYSCALE`

### 08   

Caso seja necessário visualizar por meio da biblioteca matlplotlib uma imagem que foi aberta pela biblioteca open-cv, não é necessário realizar a conversão do sistema de cores da imagem, visto que ambas as bibliotecas trabalham com o sistema RGB.
Escolha uma opção:
[❌] Verdadeiro
[☑️] Falso


### 09

O tamanho teórico de uma imagem em escala de cinzas (Profundidade 1) é dado pela fórmula T = npx/1024, onde npx é o número total de pixels da imagem. O seu tamanho teórico normalmente é próximo de seu tamanho real.

Escolha uma opção:
[☑️] Verdadeiro 
[❌] Falso ❗

### 10

Assinale abaixo o código que deve ser usado para salvar uma imagem armazenada na variável img no caminho image_path com qualidade 75% usando a biblioteca open-cv.

[❌] a.`cv2.imwrite('image_path', img, cv2.COLOR_BGR2RGB , [int(cv2.IMWRITE_JPEG_QUALITY), 75])`

[☑️] b.`cv2.imwrite('image_path', img, [int(cv2.IMWRITE_JPEG_QUALITY), 75])`

[❌] c.`cv2.imread('image_path', img, [int(cv2.IMWRITE_JPEG_QUALITY), 75])` 

[❌] d. `cv2.imwrite('image_path', img, cv2.COLOR_BGR2RGB , 75)`