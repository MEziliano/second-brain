# Semana 02 - Processamento de Imagens

# Semana 02 - Processamento de Imagens

---

### Aula 04 - Realce

- Vídeo
    
    https://www.youtube.com/watch?v=M6e6Btxd0qk
    

- Processamento de Imagens: Realces
- Definição do processamento de imagens, domínio espacial e da frequência
- Filtros (Correlação Cruzada e Convolução), Filtros (suavização e Agudização)
- Transformação Geométrica e Morfológica
- Métricas de Qualidade de imagem.

**Processamento** é toda a modificação feita nos valores de pixel da imagem para determinado fim.  Empregando técnicas como: realce, filtragem, compressão (diminuir recursos computacionais) e detecção de bordas. 

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

<aside>
💡

</aside>

---

## Aula 5  -  Filtros

- Vídeo
    
    https://youtu.be/XblyzmymVcw
    

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

<aside>
💡

</aside>

---

## Aula 6 - Transformação Geométrica e Morfológica - Métricas de Qualidade de Imagem

- Vídeo
    
    https://youtu.be/QuWrhKA5hws
    

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

![image.png](attachment:efa51895-272c-41f5-8a64-48f06bad118d:image.png)