# Semana 01 - Introdução, Conceitos e Terminologias

* **Aula 1**: Introdução à Dados de Imagens
* **Aula 2**: Dia a dia com Visão Computacional
* **Aula 3**: Introdução ao Sistema de Visão Computacional
* **Aula Prática**: Comandos Básicos para Análise de Imagens
* **DESAFIO**: Tamanho de armazenamento RGB
* **AVALIAÇÃO ONLINE 1**
-----
  
### Aulas Teóricas 

#### 01 - Introdução à Dados de  Imagens

[VIDEO AULA - 01](https://www.youtube.com/watch?v=BSR2ZcZQJH4)

 * O que é uma imagem? O que define uma imagem? <u>**Uma imagem projetada é um representação de uma matriz**</u>, pois dentro de cada pixel, a menor unidade de uma imagem, há um valor, ainda que representado de maneira binária (0 e 1). 
 * Uma imagem colorida nada mais é do que a visualização de cada canal viśivel de cores para os olhos humano **(RGB, Red, Green, Blue)**. <br>
 * 🎓 Introdução à disciplina de Análise de Imagens e Visão Computacional, focando inicialmente na compreensão de conceitos e terminologias básicas da área. <br>
* 🖼️ Definição de imagem no contexto computacional, exemplificada em três categorias: **colorida (três canais)**, **tons de cinza (intensidades variadas)** e **preto e branco (binária)**.<br>
* 🎨 Imagens coloridas são compostas por três canais de cores (Vermelho, Verde e Azul - RGB), cuja combinação forma a diversidade de cores percebida pelo olho humano. <br>
* 🔢 O computador "enxerga" a imagem como uma matriz, onde cada célula possui um valor numérico de intensidade (ex: em imagens preto e branco, 0 representa a cor preta/ausência e 1 representa o branco). <br>
* 🌈 Porém, as imagens não se limitam à faixa do visível (400nm a 700nm), podendo ser formadas por outros comprimentos de onda, como o infravermelho (próximo, intermediário e distante). <br>
* 🌱 O uso do infravermelho é essencial na agronomia para calcular o NDVI (índice de vegetação), que ajuda a monitorar se as plantas estão saudáveis, doentes ou sofrendo estresse hídrico.


### Aula 02 - Visão Computacional no dia-a-dia

[VIDEO AULA 02](https://www.youtube.com/watch?v=AzsjiYbuECc)

* O Objetivo da Visão Computacional é o desenvolvimento de algoritmos que possam processar, analisar e interpretar imagens digitais ou sequências de vídeo. Ao realziar a extração de informações relevantes de dados visuais, os sistemas de visao computacional podem tomar decisões, reconhecer objetos ou padrões e entender o conteúdo de imagens ou vídeos.  <br>
* 📱 Uso Cotidiano: Aplicação comum em autenticação biométrica de celulares, incluindo reconhecimento de impressão digital, facial e de retina. <br>
* 👥 Redes Sociais: Utilização de reconhecimento facial para sugestão e marcação automática de pessoas em fotos com base em bancos de dados. <br>
* 🚗 Setor Automotivo: Emprego na detecção de objetos para veículos autônomos e sistemas de assistência à direção (sensores de faixa e tráfego lateral). <br>
* 👷 Segurança do Trabalho: Uso em sistemas de vigilância para verificar conformidade, como a detecção automática do uso de EPIs (ex: capacetes). <br>
* 🏭 Controle de Qualidade: Aplicação na indústria para inspeção e remoção de objetos indesejados ou defeituosos em linhas de produção (ex: pedras em meio a frutas). <br>
* 🏥 Medicina: Auxílio vital no diagnóstico de doenças (como detecção de nódulos e problemas cardíacos) e suporte em cirurgias via realidade aumentada. <br>

* 👓 Realidade Aumentada (RA): Tecnologia que sobrepõe elementos digitais ao mundo real, tendo sido popularizada por jogos como Pokémon GO e hoje aplicada em soluções comerciais. <br>
* 💄 Consultoria Virtual: Marcas de cosméticos utilizam IA e câmeras de celulares para analisar a pele do cliente (rugas, olheiras) e recomendar produtos personalizados sem necessidade de testes físicos.<br>
* 🛒 Caixas de Autoatendimento: Supermercados combinam sensores de peso e câmeras de visão computacional sobre os caixas para registrar produtos corretamente e monitorar possíveis erros ou furtos.<br>
* 🔞 Conformidade Regulatória: O sistema visual consegue identificar categorias de produtos, como bebidas alcoólicas, e bloquear a venda automaticamente caso esteja fora do horário permitido por lei.<br>
* 🏪 Lojas Autônomas (Amazon Go): Estabelecimentos sem caixas ou atendentes, onde o cliente entra com QR Code e um denso sistema de câmeras no teto rastreia e cobra automaticamente os itens retirados das prateleiras.<br>
* 📊 Mapeamento de Hábitos: A visão computacional em lojas físicas gera dados valiosos sobre o comportamento do consumidor, como horários de compra e preferências, integrando-os ao perfil digital do cliente.<br>
* 🔍 Busca Visual: Ferramentas como o Google Lens permitem que o usuário fotografe um objeto desconhecido (como uma flor) para identificá-lo e descobrir onde comprá-lo. <br>

<h3> Aula 03</h3>
<details><summary> Introdução ao Sistema de Visão Computacional</summary>
*  🧠 Analogia com a visão humana: O sistema computacional imita o processo biológico, onde a luz refletida pelos objetos é captada, convertida em estímulos e processada para identificar o que está na cena (como diferenciar frutas).
<br>
* 📷 Variedade de sensores: Ao contrário do olho humano, a máquina utiliza diferentes sensores (RGB, 3D Time of Flight, infravermelho, etc.) que podem ser acoplados a câmeras ou satélites para gerar diversos tipos de imagem.
<br>
* 👁️ Limitações e subjetividade humana: A visão humana é restrita ao espectro visível e depende de interpretações subjetivas (como avaliar a condição corporal de um animal), mas tem a vantagem de se adaptar bem a variações de luz e contexto.
<br>
* 🤖 Capacidade computacional expandida: A visão computacional pode "enxergar" faixas invisíveis ao homem (do raio-X ao infravermelho), apresentando bom desempenho, desde que o modelo seja treinado especificamente para a tarefa desejada.
<br>
* 📏 Modelos computacionais oferecem medidas exatas (como valores RGB) mas são sensíveis à luz e específicos para cada tarefa, ou seja, um modelo treinado para suínos não funciona para bovinos.
<br>
* 💾 Diferente da rápida adaptação humana baseada na experiência de vida, a máquina depende de bases de dados ricas para o treinamento e de hardware potente para a velocidade de processamento.
<br>
* ⚙️ O processamento de imagem não visa necessariamente melhorar a estética visual, mas sim extrair e simplificar informações (como cor e formato) para fins de automação.
<br>
* 🔍 A análise de imagem é a etapa de interpretação dos dados processados, transformando características visuais em informações úteis, como usar a cor roxa para identificar uma uva.
<br>
* 🧮 Existe uma diferença clara nos objetivos da análise: a "classificação" lida com variáveis categóricas (qual é a fruta?), enquanto a "predição" lida com variáveis contínuas (qual é o peso?).
<br>
* 🧠 A Visão Computacional une algoritmos e técnicas para interpretar imagens ou vídeos, permitindo que o sistema reconheça padrões e tome decisões autônomas.
<br>
* 📉 O objetivo principal do processamento de imagens é reduzir o volume de dados, isolando o objeto de interesse (segmentação) para tornar a análise mais rápida e eficiente.
<br>
* 💡 Fisicamente, uma imagem é definida como uma função contínua resultante da interação entre uma fonte de energia (iluminância) e a superfície do objeto (reflectância).
<br>
* 🌑 A reflectância varia de 0 a 1: superfícies como veludo absorvem a luz (baixa reflectância), enquanto paredes brancas a refletem quase totalmente.
<br>
* 🔳 No contexto digital, a imagem é tratada como uma matriz matemática onde o Pixel é o menor elemento e contém a informação visual.
<br>
* 🐍 Em linguagens como Python, a escala de cinza é representada de 0 a 255 (e não 1 a 256), onde 0 representa o preto absoluto e 255 o branco total.
<br>
* 🌗 Imagens binárias são aquelas que possuem apenas um bit de informação de cor ($k=1$), ou seja, são estritamente preto e branco.
<br>
* 🔢 Resolução de cores: Uma imagem de 8 bits possui $2^8 = 256$ níveis de cinza, enquanto uma imagem binária ($k=1$) possui apenas $2^1 = 2$ cores (preto e branco).
<br>
* 🌈 Composição RGB: Imagens coloridas são formadas pelo somatório de três canais monocromáticos de 8 bits: Vermelho, Verde e Azul, que juntos criam a percepção de cor completa.
<br>
* 💾 Armazenamento de dados: A unidade básica de armazenamento é o Byte, que equivale a 8 bits; cada pixel de uma imagem monocromática padrão armazena exatamente 1 Byte de informação de brilho.
<br>
* 📏 Cálculo de tamanho (Cinza): O tamanho teórico de arquivo é calculado multiplicando as dimensões da imagem; por exemplo, uma imagem $500 × 500$ em escala de cinza ocupa aproximadamente $244 \text{ KB}$.
<br>
* 📦 Peso de imagens coloridas: Arquivos coloridos ocupam o triplo do espaço das imagens em tons de cinza (para a mesma resolução), pois cada pixel precisa armazenar dados para os três canais de cor simultaneamente.
</details>
<br>

[VIDEO AULA 03](https://www.youtube.com/watch?v=yf3tVfV_59Y&t=2S)

-----

| 🗂  **Palavras-Chaves** | 📝 **Anotações** |
|-------------------------|------------------|
| •  |  |
| •  |  |
| •  |  |
---
### 📌 Resumo

