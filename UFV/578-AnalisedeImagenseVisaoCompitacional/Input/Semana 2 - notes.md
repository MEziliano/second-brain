# Semana 02 - Processamento de Imagens

# Semana 02 - Processamento de Imagens

---

### Aula 04 - Realce
<<<<<<< HEAD

- Vídeo
    
    https://www.youtube.com/watch?v=M6e6Btxd0qk
    

- Processamento de Imagens: Realces
=======
<details>
<summary>Video</summary>

[Aula 04 - Realce](https://www.youtube.com/watch?v=M6e6Btxd0qk)
    
</details>

**Processamento de Imagens: Realces**

>>>>>>> 16fdaba (add: ELT578 - Visão Computacional)
- Definição do processamento de imagens, domínio espacial e da frequência
- Filtros (Correlação Cruzada e Convolução), Filtros (suavização e Agudização)
- Transformação Geométrica e Morfológica
- Métricas de Qualidade de imagem.

**Processamento** é toda a modificação feita nos valores de pixel da imagem para determinado fim.  Empregando técnicas como: realce, filtragem, compressão (diminuir recursos computacionais) e detecção de bordas. 

<<<<<<< HEAD
=======

>>>>>>> 16fdaba (add: ELT578 - Visão Computacional)
**Domínio Espacial** 

- Operando sobre os pixels $(x,y)$, sendo ponto a ponto, por meio de operações matemáticas ou por filtros.
- Normalmente nas imagens predomina a baixa frequência
- Em regiões de borda de objetos e em ruídos há alta frequência.
    1. Negativo da imagem - inverte os tons de cinza
    2. Transformação logarítmica - aumentando a faixa dinâmica em regiões escuras e reduzindo a faixa dinâmica em regiões claras. 
    3. Transformação exponencial - Serve para realçar a parte clara (oposto da log.).  
    4. Threshlod - Gerar uma imagem binária
    5. Modificação do histograma - recomendado para quando a imagem possuí valores mal distribuídos.
    6. Equalização - redistribuir tons de cinza
    7. Auto escala - utilizado depois do processamento, dada a distribuição fora do intervalo paramétrico da imagem (0,255)ou não

**Domínio de frequência**

- Horizontal ou vertical
- Transformada de Fourier

$$

    f(x,y) = \frac{1}{MN} \sum_{u=0}^{M-1} \sum_{v=0}^{N-1} F[u,v] \, e^{j\frac{2\pi}{MN}(ux+vy)}

$$

**Realce** obter uma imagem processada para uma aplicação específica, sem regra específica para isso. Sendo o método altamente dependente do problema. Compensando as imperfeições dos sistemas de aquisição e reprodução de imagens.   

<<<<<<< HEAD
<aside>
💡

</aside>
=======
<details>
<summary>
<h3>Resumo</h3>
</summary>

* 📚 Introdução da quarta aula do curso, focada na técnica de realce e processamento de imagens e visão computacional.
* 🗺️ Exploração de conceitos como domínio espacial, domínio da frequência, filtros de suavização, correlação cruzada e convolução.
* 🖼️ Definição de processamento como qualquer modificação nos valores dos pixels para atingir um objetivo específico.
* 🎯 O foco principal do processamento é melhorar a informação desejada, e não necessariamente tornar a imagem mais bonita visualmente.
* 📉 Uso da compressão para reduzir o tamanho de armazenamento e o consumo de recursos computacionais.
* ✂️ Importância da detecção de bordas para isolar objetos de interesse e reduzir a quantidade de dados a serem manipulados.
* 🔢 Diferenciação entre o domínio espacial (valores diretos dos pixels) e o domínio da frequência (uso da Transformada de Fourier).
* ➗ Tratamento da imagem como uma matriz, permitindo a aplicação de diversas operações matemáticas ponto a ponto.
* 〰️ Identificação de áreas de baixa frequência (pouca mudança nos pixels) e alta frequência (bordas e ruídos).
* 🛠️ O realce de imagem é definido como um método altamente dependente do problema específico que se deseja resolver.
* 📷 O objetivo do realce no domínio espacial é compensar imperfeições nos sistemas de captura e reprodução de imagens.
* 🔄 O negativo da imagem inverte os tons de cinza, transformando áreas escuras em claras e vice-versa, sendo um tipo básico de realce.
* 🌑 A transformação logarítmica é ideal para destacar detalhes em regiões escuras, aumentando sua faixa dinâmica.
* ☀️ A transformação exponencial é recomendada para imagens superexpostas, pois expande a faixa dinâmica das áreas claras.
* 🔳 A limiarização transforma a imagem em binária (preto e branco) para facilitar a segmentação e isolamento de objetos.
* 📊 O histograma representa a distribuição estatística do percentual de pixels para cada valor de intensidade (0 a 255 no Open CV).
* ⚖️ A equalização de histograma redistribui os tons de cinza para tornar a imagem mais uniforme e melhorar o contraste.
* 🌈 Embora comum em tons de cinza, a equalização também pode ser aplicada em cada banda do espaço de cor RGB.
* 📏 O filtro de alta escala é usado após o processamento para garantir que os valores dos pixels voltem ao intervalo padrão de 0 a 255.

</details>
>>>>>>> 16fdaba (add: ELT578 - Visão Computacional)

---

## Aula 5  -  Filtros
<<<<<<< HEAD

- Vídeo
    
    https://youtu.be/XblyzmymVcw
    
=======
<details>
<summary>Video</summary>
    
[AULA 05 - FILTROS](https://youtu.be/XblyzmymVcw)
    
</details>
>>>>>>> 16fdaba (add: ELT578 - Visão Computacional)

Um filtro nada mais é do que um tipo de processamento por máscara, ou como também é conhecido, kernel. A modificação do valor do pixel com base nos valores de seu vizinho e em uma máscara. Aplicação exige ancorar um pixel para a aplicação da máscara, normalmente sendo o pixel central. 

**Correlação Cruzada**

- Um kernel desliza sobre a imagem;
- Em cada posição, o produto entre o kernel e a região é calculado;
- A saída é uma medida de similaridade entre kernel e região
- Usada principalmente em **detecção de padrões**, **reconhecimento de imagens** e **alinhamento de imagens**.

**Convolução**

- Semelhante a correlação cruzada, mas primeiro é rotacionado em 180 graus (flip) antes do cálculo.
- É usada em filtragem de imagem, suavização, detecção de bordas e realce de características.

**Transformada de Fourier**

Função Complexa e periódica, se repetindo a cada 2 $\pi$. A inversa da Fourier é a própria imagem do domínio espacial.

$$
   f(p,q) \sum_{u=0}^{M-1} \sum_{v=0}^{N-1} F(m,n) \, e^{{-i\frac{2\pi}{M}pm} \, e^{-i (\frac{2\pi}{N}qn})}

\\
    f(x,y) = \frac{1}{MN} \sum_{u=0}^{M-1} \sum_{v=0}^{N-1} F(u,v) \, e^{j\frac{2\pi}{MN}(ux+vy)}

$$

Uma imagem pode ser vista de duas maneiras: no domínio espacial (como uma grade pixels) ou no domínio de frequência (em termos de padrões de intensidade). A Transformada de Fourier converte uma imagem do domínio espacial para domínio da frequência. 

**Análise da frequência**: A partir da Transformada de Fourier é possível a identificação de padrões e texturas. Uma imagem com muitos detalhes terá uma distribuição mais ampla, já uma imagem mas suave terá uma distribuição mais concentrada em valores baixos. 

**Filtragem de imagem:**  Pode se aplicar filtros para realçar ou remover determinadas características da imagem. 

**Compressão de imagem:** Usada em JPEG, principalmente através da Transformada de Fourier, para representar a imagem de modo mais eficiente.  

**Suavização**

- Borramento, remoção de ruídos (domínio espacial)
- Atenuam ou eliminam componentes de alta frequência (domínio da frequência - filtro passa baixa)

**Agudização**

- Realçar bordas e ruídos (DE)
- Atenuam ou eliminam na baixa frequência (domínio da frequência - filtro passa alta)

<<<<<<< HEAD
<aside>
💡

</aside>
=======
<details><summary><h3>Resumo</h3></summary>

* 🎭 O filtro é um processamento por máscara (ou Kernel) que modifica o valor de um pixel com base em seus vizinhos.
* ⚓ O processo exige "ancorar" a máscara em um pixel, geralmente o central, para realizar o cálculo matemático sobre a imagem.
* 🔢 A imagem é tratada como uma matriz onde cada elemento representa a intensidade do brilho (0 a 255 no Open CV).
* ✖️ A filtragem básica consiste em multiplicar os valores dos pixels da imagem pelos valores correspondentes no Kernel.
* 🔄 A principal diferença entre correlação e convolução é que, na convolução, o Kernel é "flipado" (rotacionado em 180°).
* 🧩 A correlação cruzada mede a similaridade entre o Kernel e a região da imagem, sendo ideal para reconhecimento de padrões.
* 🖼️ Filtros de convolução são amplamente aplicados em suavização, realce de características e detecção de bordas.
* 🧠 O conceito de convolução apresentado é o mesmo fundamento utilizado nas Redes Neurais Convolucionais (CNNs).

* 🌊 A Transformada de Fourier é uma ferramenta matemática que permite analisar imagens e sinais através de suas frequências.
* 📉 O processo divide os componentes da imagem em baixas frequências (áreas homogêneas) e altas frequências (mudanças abruptas).
* 🐕 Bordas de objetos e contornos são considerados regiões de alta frequência devido à variação rápida nos valores dos pixels.
* 🌨️ Ruídos na imagem, como "chuviscos" brancos em um fundo preto, também são identificados como componentes de alta frequência.
* 🔢 No processamento de imagens digitais, utiliza-se a Transformada Discreta de Fourier devido à natureza finita dos pixels (0 a 255).
* 🔄 É possível transformar uma imagem para o domínio da frequência, realizar operações e depois usar a Transformada Inversa para voltar ao domínio espacial.
* ⚖️ O uso do filtro de alta escala é obrigatório ao retornar ao domínio espacial para garantir que os valores dos pixels fiquem no intervalo de 0 a 255.
* 🔍 A análise no domínio frequencial é uma técnica poderosa para identificar padrões complexos e texturas que não são óbvios no domínio comum.

* 🔪 Uso de filtros especializados como Sobel e o operador Canny para a detecção precisa de bordas de objetos.
* 💾 Aplicação da Transformada de Fourier na compressão de dados, sendo uma técnica fundamental para o formato de imagem JPEG.
* 🌫️ O processo de suavização causa o borramento da imagem com o objetivo principal de remover ruídos indesejados.
* 📉 Filtros Passa-Baixa permitem a permanência de frequências baixas enquanto suprimem as altas (bordas e ruídos).
* ⚡ A agudização é o oposto da suavização, focando no realce de bordas e detalhes finos da imagem.
* 📈 Filtros Passa-Alta são utilizados no domínio da frequência para atenuar componentes de baixa frequência e destacar contornos.
</details>
>>>>>>> 16fdaba (add: ELT578 - Visão Computacional)

---

## Aula 6 - Transformação Geométrica e Morfológica - Métricas de Qualidade de Imagem

<<<<<<< HEAD
- Vídeo
    
    https://youtu.be/QuWrhKA5hws
    

=======
<details>
<summary>Video</summary>
    
[AULA 06 - TRANSFORMAÇÃO GEOMÉTRICA E MORFOLÓGICA - MÉTRICAS DE QUALIDADE DE IMAGEM](https://youtu.be/QuWrhKA5hws)
    
</details>
>>>>>>> 16fdaba (add: ELT578 - Visão Computacional)
Transformações geométricas são aquelas feitas para alterar sua forma, tamanho, orientação ou posição sem alterar a essência ou o próprio conteúdo visual. Dentre esse tipo de transformação se destaca dois tipos

- Linear
    - Translação
    - Rotação
    - Escalonamento
    - Cisalhamento (Shear)
    - Reflexão

- Não Linear
    - Projeção
    - Distorção

Transformações Morfológicas são feita a partir de uma operação simples baseadas no formato da imagem. Sendo executadas normalmente em imagens binárias, ou seja, imagens em preto e branco. São permitidas duas entradas: a imagem original e a imagem tratada por um kernel.  As operações morfológicas podem ser:

- erosão: afinando a imagem evitando ruído branco e objetos próximos;
- dilatação: oposto do acima, para unir parte de um objeto quebrado;
- abertura: ambos os acima eliminando ruídos;
- fechamento: dilatação + erosão.

Como saber a qualidade do processamento?

<<<<<<< HEAD
![image.png](attachment:efa51895-272c-41f5-8a64-48f06bad118d:image.png)
=======
<details><summary>Resumo</summary>

* 📐 As transformações geométricas alteram forma, tamanho e orientação da imagem sem mudar seu conteúdo visual básico.
* 🔄 Operações comuns incluem translação, rotação, escalonamento, "flip" (inversão de eixos) e projeção de perspectiva.
* 🎥 A transformação de perspectiva mapeia pontos entre planos bidimensionais e superfícies tridimensionais (reconstrução 3D).
* 📍 No OpenCV com Python, a leitura de coordenadas segue o padrão de colunas (x) e linhas (y) para mapeamento de pontos.
* 🔢 Para aplicar uma transformação de perspectiva, é necessário fornecer dois conjuntos de pontos: os da imagem original e os da saída desejada.
* 🌑 Transformações morfológicas são operações simples baseadas na forma, geralmente aplicadas em imagens binárias (preto e branco).
* 🧪 Essas operações utilizam a imagem original e um Kernel para definir se a ação será de erosão, dilatação, abertura ou fechamento.
* 🤏 A erosão tem como objetivo "afinar" objetos, sendo útil para remover ruídos brancos ou separar objetos que ficaram conectados indevidamente.   

* ➕ A dilatação funciona como o inverso da erosão, sendo útil para unir partes separadas ou preencher falhas em um objeto.
* 🧼 A "abertura" é a combinação de erosão seguida de dilatação, técnica eficaz para remover ruídos sem alterar o tamanho final do objeto.
* 🕳️ O "fechamento" consiste em aplicar a dilatação e depois a erosão, ideal para fechar pequenos buracos internos em objetos de primeiro plano.
* ➰ O gradiente morfológico é uma operação que destaca o contorno do objeto, auxiliando em tarefas futuras de segmentação.
* 📏 A qualidade do processamento é medida comparando uma imagem gerada ($g$) com uma imagem modelo ou ideal ($f$).
* 🔢 Métricas como Erro Máximo e Erro Médio Absoluto quantificam a diferença entre os pixels da imagem processada e da original.
* 📉 O Erro Quadrático Médio (MSE) e sua raiz (RMSE) são ferramentas estatísticas fundamentais para validar a precisão do processamento.
* ✍️ O encerramento do módulo destaca a importância das métricas para avaliação online e a prática em laboratórios síncronos.
</details>
>>>>>>> 16fdaba (add: ELT578 - Visão Computacional)
