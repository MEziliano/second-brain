# KIT DE REVISÃO: PROCESSAMENTO INTELIGENTE DE SINAIS
## 1. FOLHA DE ESTUDO DE UMA PÁGINA (RESUMO EXECUTIVO CONCEITUAL)
###  Ideia 1: Dualidade do Tempo e Amostragem de Nyquist
* **Tempo Contínuo vs. Tempo Discreto:** Sinais no tempo contínuo $(x(t)$) são representados por funções de variáveis reais ininterruptas e denotados por parênteses. Sinais no tempo discreto $(x[n]$) existem apenas em instantes inteiros $(n$) e são representados por colchetes.
* **Processo de Amostragem:** A amostragem converte o mundo analógico no digital coletando valores em intervalos regulares de tempo $(T_s$).
* **Teorema de Nyquist-Shannon:** Para evitar a perda de informação e a sobreposição espectral (*aliasing*), a frequência de amostragem $(f_s$) deve ser estritamente maior ou igual ao dobro da maior frequência contida no sinal original ($(f_M$)):
  $[f_s \ge 2 f_M \quad \text{ou} \quad \omega_s \ge 2 \omega_M \quad.$]

###  Ideia 2: Classificação de Sinais (Determinísticos vs. Aleatórios; Energia vs. Potência)
* **Determinísticos vs. Aleatórios:** Sinais determinísticos são completamente descritos por funções matemáticas exatas. Sinais aleatórios (como ruído de medição) não possuem equação determinística no tempo e são modelados por estatística e Funções de Densidade de Probabilidade (PDF).
* **Sinais de Energia (1ª Classe):** Têm duração finita no tempo. Possuem energia total finita ($(0 < E_\infty < \infty$)) e potência média nula ($(P_\infty = 0$)).
  $[E_\infty = \int_{-\infty}^{\infty} |x(t)|^2 dt \quad \text{ou} \quad E_\infty = \sum_{n=-\infty}^{\infty} |x[n]|^2 \quad.$]
* **Sinais de Potência (2ª Classe):** Têm duração infinita (como senóides puras e sinais periódicos). Possuem energia total infinita ($(E_\infty = \infty$)) e potência média finita ($(0 < P_\infty < \infty$)).
  $[P_\infty = \lim_{T \to \infty} \frac{1}{T} \int_{-T/2}^{T/2} |x(t)|^2 dt \quad \text{ou} \quad P_\infty = \lim_{N \to \infty} \frac{1}{2N+1} \sum_{n=-N}^{N} |x[n]|^2 \quad.$]

###  Ideia 3: Abstração de Sistemas LIT (Linearidade e Invariância no Tempo)
* **Linearidade:** Exige o cumprimento simultâneo do Princípio da Superposição:
  1. **Aditividade:** $(H\{x_1 + x_2\} = H\{x_1\} + H\{x_2\}$).
  2. **Homogeneidade:** $(H\{a \cdot x_1\} = a \cdot H\{x_1\}$).
  * *Regra da Entrada Nula:* Todo sistema estritamente linear deve obrigatoriamente produzir saída nula para entrada nula: $(H\{0\} = 0$).
* **Invariância no Tempo:** O comportamento do sistema não muda com o passar do tempo. Um atraso de $(t_0$) na entrada produz exatamente o mesmo atraso de $(t_0$) na saída: $(H\{x(t - t_0)\} = y(t - t_0)$).

###  Ideia 4: Convolução e Memória de Sistemas
* **Decomposição por Impulso:** Qualquer sinal discreto pode ser escrito como uma soma de impulsos unitários deslocados e escalados: $(x[n] = \sum x[k]\delta[n-k]$).
* **Resposta ao Impulso ($(h[n]$) ou $(h(t)$)):** É a saída do sistema quando a entrada é um impulso unitário ($(\delta[n]$) ou $(\delta(t)$)). Em sistemas LIT, ela caracteriza o sistema completamente.
* **Mecanismo Operacional:** Inverter no tempo, deslocar pelo instante $(n$) ou $(t$), multiplicar ponto a ponto e somar/integrar a área sobreposta:
  $[y[n] = x[n] * h[n] = \sum_{k=-\infty}^{\infty} x[k]h[n-k] \quad,$]
  $[y(t) = x(t) * h(t) = \int_{-\infty}^{\infty} x(\tau)h(t-\tau)d\tau \quad.$]
* **Duração do Vetor de Saída:** A convolução de dois vetores discretos finitos de tamanhos $(N_1$) e $(N_2$) resulta em um vetor de saída com duração de:
  $[N_{out} = N_1 + N_2 - 1.$]

### Ideia 5: Domínio da Frequência, Transformada de Fourier e Filtragem
* **Teorema da Convolução:** A convolução no domínio do tempo corresponde a uma multiplicação simples no domínio da frequência:
  $[\mathcal{F}\{x(t) * h(t)\} = X(j\omega) \cdot H(j\omega) \quad.$]
* **Filtro Anti-Aliasing Analógico:** Deve ser obrigatoriamente um filtro passa-baixas analógico posicionado no hardware **antes do conversor A/D** para limitar a largura de banda e impedir o *aliasing*.
* **Estilos de Filtros Reais:**
  * **Butterworth:** Resposta maximamente plana na banda passante, sem oscilações.
  * **Chebyshev:** Transição de corte mais rápida na banda de rejeição, mas introduz ondulações (*ripples*).
  * **Bessel:** Resposta de **fase linear**, preserva a forma temporal do sinal sem introduzir sobressinais.
* **Efeito Gibbs e Filtro Ideal:** Um filtro passa-baixas ideal tipo "parede de tijolos" (*brick-wall*) possui resposta ao impulso temporal do tipo $(sinc(t)$), cujas caudas infinitas geram oscilações artificiais (*ringings*) e sobressinais ao redor de transições rápidas.

---

## 2. TABELA DE ERROS COMUNS E COMO CORRIGI-LOS

| Erro Comum | Conceito Incorreto (Armadilha) | Correção Rigorosa & Explicação |
| :--- | :--- | :--- |
| **Erro 1: Offset em Sistemas** | Achar que $(y(t) = 2x(t) + 3\text{ V}$) é linear por ser uma reta ($(y = ax + b$)). | **Incorreto.** O termo $(+3\text{ V}$) quebra a homogeneidade e a aditividade. Se $(x(t)=0$), a saída é $(3\text{ V} \neq 0$). Para $(x_1=1\text{V} \to y_1=5\text{V}$); se dobrarmos a entrada ($(x_2=2\text{V}$)), a saída passa a ser $(7\text{V} \neq 10\text{V}$). |
| **Erro 2: Classificação de Sinais Truncados** | Acreditar que uma gravação de 10 minutos de uma onda senoidal é um sinal de potência com energia infinita. | **Incorreto.** A senóide matemática pura de $(t=-\infty$) a $(+\infty$) é sinal de potência. Ao truncá-la ou gravá-la por um tempo finito (10 min), a integral de seu quadrado converge para um valor finito, tornando-a estritamente um **sinal de energia** ($(E_\infty < \infty, P_\infty = 0$)). |
| **Erro 3: Ignorar a Memória na Convolução** | Confundir a convolução $(x(t)*h(t)$) com a simples multiplicação ponto a ponto $(x(t) \cdot h(t)$). | **Incorreto.** A multiplicação ponto a ponto assume um sistema estático (sem memória). Em sistemas com memória, a saída depende do histórico passado da entrada. A inversão e deslocamento $(h[n-k]$) servem para alinhar e acumular o passado sobre o presente. |
| **Erro 4: Dimensionar Buffer de Convolução** | Alocar um buffer de saída com o mesmo tamanho da entrada ($(N_1$)) na convolução discreta. | **Incorreto.** O tamanho correto do buffer de saída é $(N_{out} = N_1 + N_2 - 1$). O espaço extra ($(N_2 - 1$)) guarda o transiente de descida (a cauda de decaimento da memória do sistema). Alocar apenas $(N_1$) corta a resposta e gera estalos numéricos. |
| **Erro 5: Filtro Digital Anti-Aliasing Pós-A/D** | Achar que um filtro digital em software (DSP) consegue eliminar o *aliasing* após a conversão A/D. | **Incorreto.** Quando ocorre *aliasing*, as frequências altas rebatem e se somam sobre as frequências baixas de forma matematicamente **indistinguível**. O filtro anti-aliasing precisa ser um filtro passa-baixas **analógico pré-A/D**. |
| **Erro 6: Filtro Ideal "Parede de Tijolos"** | Acreditar que o corte retangular perfeito na frequência (filtro ideal) é sempre a melhor escolha prática. | **Incorreto.** No tempo, o corte retangular perfeito corresponde a uma resposta ao impulso $(sinc(t)$) com caudas infinitas. Isso gera oscilações artificiais (*ringings*) e sobressinais em transições (**Efeito Gibbs**), além de ser não-causal. |

---

## 3. DEZ QUESTÕES DE REVISÃO ORDENADAS POR DIFICULDADE

### Nível Básico (Questões 1 a 3)

#### **Questão 1**
Como se diferenciam simbolicamente a representação de um sinal no tempo contínuo e no tempo discreto?
* **Resposta:** O tempo contínuo utiliza variáveis reais entre parênteses, como $(x(t)$). O tempo discreto utiliza índices inteiros entre colchetes, como $(x[n]$).

#### **Questão 2**
Considere os sinais $(x_1[n]$) e $(x_2[n]$). Se $(x_1[-n] = x_1[n]$) e $(x_2[-n] = -x_2[n]$), qual é a classificação de cada sinal quanto à simetria? O que deve ser o valor de $(x_2$)?
* **Resposta:** $(x_1[n]$) é um sinal **par** e $(x_2[n]$) é um sinal **ímpar**. Todo sinal ímpar discreto no tempo deve necessariamente valer zero na origem: $(x_2 = 0$).

#### **Questão 3**
Explique a diferença entre um sistema estático e um sistema dinâmico. Dê um exemplo de cada um.
* **Resposta:** Um sistema estático não possui memória; sua saída no presente depende apenas da entrada no mesmo instante (ex.: resistor $(v(t) = R \cdot i(t)$) ou amplificador). Um sistema dinâmico possui memória; sua saída depende de valores presentes e passados da entrada (ex.: capacitor $(v(t) = \frac{1}{C}\int i(\tau)d\tau$) ou filtro de média móvel).

---

### Nível Intermediário (Questões 4 a 6)

#### **Questão 4**
O sistema discreto $(y[n] = 2x[n] + 5$) é linear? Prove testando a propriedade da homogeneidade com um fator de escala $(a = 2$).
* **Resposta:** **Não é linear.** Para $(x_1[n]$), $(y_1[n] = 2x_1[n] + 5$). Se multiplicarmos a entrada por $(a=2$), a entrada passa a ser $(2x_1[n]$), gerando a saída real $(y_{real}[n] = 2(2x_1[n]) + 5 = 4x_1[n] + 5$). No entanto, pela homogeneidade esperava-se $(2 \cdot y_1[n] = 4x_1[n] + 10$). Como $(y_{real} \neq 2y_1$), a homogeneidade é violada. Além disso, para $(x[n]=0 \to y[n]=5 \neq 0$).

#### **Questão 5**
Determine a classificação (energia ou potência) de uma gravação de áudio de 5 minutos descrita por $(x(t) = 3\cos(100\pi t) \cdot [u(t) - u(t - 300)]$).
* **Resposta:** Trata-se de um **sinal de energia**. Embora a onda senoidal pura e infinita seja um sinal de potência, o termo de janelamento $([u(t) - u(t - 300)]$) limita a existência do sinal ao intervalo $([0, 300\text{ s}]$). A integral do quadrado da amplitude resulta em um valor real e finito ($(0 < E_\infty < \infty$)), garantindo potência média nula no horizonte infinito ($(P_\infty = 0$)).

#### **Questão 6**
Um bloco de sinal de áudio $(x[n]$) com $(N_1 = 500$) amostras passa por um filtro digital FIR $(h[n]$) com $(N_2 = 120$) amostras. Qual deve ser o tamanho do buffer de saída $(y[n]$) alocado na memória para evitar truncamento?
* **Resposta:** O buffer de saída deve ter exatamente $(N_{out} = N_1 + N_2 - 1$) posições:
  $[N_{out} = 500 + 120 - 1 = 619 \text{ amostras}.$]
  As 119 amostras adicionais contêm o transiente de descida (a cauda de decaimento do filtro).

---

### Nível Avançado (Questões 7 a 9)

#### **Questão 7**
Calcule a convolução discreta $(y[n] = x[n] * h[n]$) para as sequências $(x[n] =$) para $(n=$) e $(h[n] =$) para $(n=$).
* **Resposta:** Aplicando a fórmula $(y[n] = \sum x[k]h[n-k]$):
  * $(y = xh = 3 \times 1 = 3$)
  * $(y = xh + xh = (3 \times 1) + (2 \times 1) = 5$)
  * $(y = xh + xh = (3 \times 1) + (2 \times 1) = 5$)
  * $(y = xh = 2 \times 1 = 2$)
  * Vetor resultante: $(y[n] =$) para $(n=$). Duração: $(2 + 3 - 1 = 4$) amostras.

#### **Questão 8**
Um sinal analógico contém componentes de frequência até $(2\text{ kHz}$), mas apresenta um ruído de interferência em $(7\text{ kHz}$). Se o sinal for amostrado a $(f_s = 5\text{ kHz}$) sem um filtro anti-aliasing analógico, em qual frequência aparente o ruído de $(7\text{ kHz}$) reaparecerá dentro da banda base digitalizada?
* **Resposta:** Com $(f_s = 5\text{ kHz}$), a frequência limite de Nyquist é $(f_s/2 = 2,5\text{ kHz}$). Como a frequência do ruído ($(7\text{ kHz}$)) excede o limite de Nyquist, ela sofre *aliasing* (rebatimento espectral). A frequência rebatida aparente $(f_{aliased}$) é dada por:
  $[f_{aliased} = |7\text{ kHz} - 2 \times 5\text{ kHz}| = |-3\text{ kHz}| = 3\text{ kHz} \to |3\text{ kHz} - 2,5\text{ kHz}| \implies 2\text{ kHz}.$]
  O ruído de $(7\text{ kHz}$) rebaterá exatamente em $(2\text{ kHz}$), corrompendo diretamente a borda do sinal útil.

#### **Questão 9**
Você está projetando um monitor cardíaco de UTI (ECG) para detectar picos de tensão rápidos e sem distorção visual de forma de onda. Qual estilo de filtro passa-baixas de 4ª ordem deve ser selecionado entre Butterworth, Chebyshev e Bessel? Justifique com base nas propriedades de fase e tempo.
* **Resposta:** Deve-se escolher o **Filtro Bessel**. O filtro Bessel é o único que possui resposta de **fase linear** em relação à frequência, o que significa que todos os componentes de frequência sofrem exatamente o mesmo atraso de tempo. Isso preserva o formato temporal da onda sem introduzir sobressinais artificiais (*overshoots*) ou oscilações que poderiam gerar alarmes falsos de arritmia no monitor. O Chebyshev geraria oscilações na subida do pico.

---

### Nível Mestre / Desafio (Questão 10)

#### **Questão 10**
Um engenheiro deseja filtrar um áudio $(x[n]$) com $(N_1 = 40.000$) amostras por um filtro $(h[n]$) com $(N_2 = 10.000$) amostras usando a FFT. Ele calcula `X = FFT(x, 40000)`, `H = FFT(h, 40000)`, multiplica $(Y = X \cdot H$) e aplica `IFFT(Y)`. 
1. Por que o final da música reapareceu sobreposto no início da gravação? 
2. Como corrigir o código para obter a convolução linear exata?
* **Resposta:**
  1. A multiplicação direta de transformadas discretas na frequência realiza uma **convolução circular** no tempo de período $(N=40.000$). Como o tamanho necessário para a convolução linear exata é $(N_{out} = N_1 + N_2 - 1 = 40.000 + 10.000 - 1 = 49.999$) amostras, ao escolher uma FFT de apenas $(40.000$) pontos, as $(9.999$) amostras excedentes da cauda deram a volta (*wrap-around*) e se somaram ao início do sinal.
  2. Para corrigir, deve-se aplicar o preenchimento com zeros (*zero-padding*) nos vetores de entrada antes de calcular a FFT, garantindo que o tamanho da FFT atinja:
     $[N_{FFT} \ge N_1 + N_2 - 1 \implies N_{FFT} \ge 49.999 \text{ pontos (ex: } 65.536 \text{ pontos para potência de 2)}.$]

---

## 4. PLANO DE REVISÃO DE 7 DIAS

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    CRONOGRAMA DE CONSOLIDAÇÃO (7 DIAS)                  │
├───────┬──────────────────────────────────┬──────────────────────────────┤
│ Dia   │ Foco do Dia                      │ Ação Prática                 │
├───────┼──────────────────────────────────┼──────────────────────────────┤
│ Dia 1 │ Sinais, Amostragem e Energia     │ Rever Ideias 1 e 2; responder│
│       │                                  │ às Questões 1, 2 e 5.        │
├───────┼──────────────────────────────────┼──────────────────────────────┤
│ Dia 2 │ Propriedades de Sistemas LIT     │ Rever Ideia 3; fazer o teste │
│       │                                  │ de linearidade na Questão 4. │
├───────┼──────────────────────────────────┼──────────────────────────────┤
│ Dia 3 │ Resposta ao Impulso e Convolução │ Rever Ideia 4; resolver a    │
│       │                                  │ Convolução da Questão 7.     │
├───────┼──────────────────────────────────┼──────────────────────────────┤
│ Dia 4 │ Tamanho do Buffer e Transientes  │ Rever Erro 4 e resolver a    │
│       │                                  │ dimensão da Questão 6.       │
├───────┼──────────────────────────────────┼──────────────────────────────┤
│ Dia 5 │ Fourier, Aliasing e Amostragem   │ Rever Ideia 5; resolver o    │
│       │                                  │ aliasing da Questão 8.       │
├───────┼──────────────────────────────────┼──────────────────────────────┤
│ Dia 6 │ Estilos de Filtros e FFT         │ Rever Tabela de Erros 5 e 6; │
│       │                                  │ resolver Questões 9 e 10.    │
├───────┼──────────────────────────────────┼──────────────────────────────┤
│ Dia 7 │ Simulação Global e Diagnóstico   │ Refazer as 10 questões sem   │
│       │                                  │ consulta em 45 minutos.      │
└───────┴──────────────────────────────────┴──────────────────────────────┘
```

---

## 5. GUIA DE FONTES ESPECÍFICAS PARA CONSULTA RÁPIDA

### Fontes em PDF (Capítulos e Seções Exatas)

1. **`Apostila ELT 576 Atualizada.pdf`**:
   * **Capítulo 1.1 e 1.6 (Páginas 3, 18–20):** Definições de sinais contínuos/discretos e equações de Energia ($(E_\infty$)) e Potência ($(P_\infty$)).
   * **Capítulo 2.1 (Páginas 22–25):** Classificação de Sistemas — Invariância no tempo, Linearidade (Aditividade e Homogeneidade - Exemplo 2.2).
   * **Capítulo 3.1 (Páginas 30–35):** Somatório de Convolução Discreta, decomposição por impulsos e Exemplo 3.1 com cálculo e gráfico.
   * **Capítulo 4.1 e 4.3 (Páginas 39, 41–43):** Transformada de Fourier, Efeito Gibbs e Tabela de Propriedades (Convolução no tempo).
   * **Capítulo 5.1 e 5.2 (Páginas 48–61):** Tipos e Estilos de Filtros (Passa-Baixa, Passa-Alta, Passa-Faixa, Chebyshev, Bessel e Butterworth).

2. **`ELT 576.pdf`**:
   * **Seção 1 (Páginas 10–12):** Classes de Sinais de Energia e Potência (fórmulas limite de $(T \to \infty$)).
   * **Seção 3.1 (Páginas 23–25):** Propriedades da Soma de Convolução e conceito de Memória de Sistemas.
   * **Seção 4 e 5 (Páginas 46–50):** Amostragem, Espectro de Trem de Impulsos, *Aliasing* e Condicionamento Analógico Anti-Aliasing pré-A/D.

---