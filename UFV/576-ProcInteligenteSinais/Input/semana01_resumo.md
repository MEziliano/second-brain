KIT DE REVISÃO CONSOLIDADA: SINAIS, SISTEMAS E CONVOLUÇÃO (ELT 576)

# 1. FOLHA DE ESTUDO DE UMA PÁGINA (RESUMO EXECUTIVO CONCEITUAL)

A teoria formal de Sinais e Sistemas constitui a fundação matemática essencial para a engenharia moderna, atuando como o elo rigoroso entre os fenômenos físicos e a sua manipulação computacional ou eletrônica. Os sinais representam grandezas físicas que carregam informações sobre o comportamento de processos naturais ou artificiais, enquanto os sistemas são as entidades físico-matemáticas encarregadas de modificar, filtrar e processar essas informações. Uma compreensão conceitual unificada — abrangendo a transição do tempo contínuo para o discreto, os princípios de linearidade e invariância temporal e as representações no domínio da frequência — é um pré-requisito indispensável no projeto de engenharia. A negligência desses fundamentos acarreta falhas catastróficas de modelagem, como a corrupção irreversível de dados por aliasing em conversões analógico-digitais, o estouro de buffers de memória em tempo de execução ou a perda de estabilidade e imprevisibilidade no comportamento dinâmico de filtros e controladores.

1.1 Dualidade do Tempo e Amostragem de Nyquist

A descrição matemática de sinais subdivide-se fundamentalmente em contínua e discreta no tempo:

* Sinal em Tempo Contínuo x(t): Definido em um continuum temporal t \in \mathbb{R}, podendo assumir infinitos pontos em qualquer intervalo observável. É a representação natural de ondas sonoras, variações de temperatura ou sinais de tensão analógica.
* Sinal em Tempo Discreto x[n]: Definido estritamente para valores inteiros da variável temporal (n \in \mathbb{Z}), denotado formalmente por colchetes. O sinal é indefinido entre instantes consecutivos (n e n+1).

A transição do domínio analógico para o digital exige os processos de amostragem e discretização. Como o processamento digital envolve uma quantidade finita de amostras, a conversão do sinal contínuo para a sequência x[n] deve respeitar o Teorema da Amostragem de Nyquist (f_s \ge 2f_M). A amostragem realizada abaixo da taxa crítica de Nyquist gera o fenômeno do aliasing (sobreposição espectral), no qual componentes de alta frequência são irremediavelmente rebatidos e distorcidos como frequências mais baixas na sequência discreta. Esse processo acarreta perda irreversível da informação original, sendo impossível restaurá-la via processamento em software pós-amostragem.

       Sinal Analógico Contínuo x(t)
                   │
                   ▼
     ┌───────────────────────────┐
     │  Filtro Anti-Aliasing     │ (Remove componentes f > fs/2)
     └─────────────┬─────────────┘
                   │
                   ▼
     ┌───────────────────────────┐
     │ Conversor A/D (Amostrador)│ (Amostragem na taxa fs >= 2fM)
     └─────────────┬─────────────┘
                   │
                   ▼
        Sinal Discreto x[n]


1.2 Classificação de Sinais e Dinâmica de Energia vs. Potência

Sinais determinísticos contrapõem-se aos aleatórios ou estocásticos quanto à sua previsibilidade:

* Sinais Determinísticos: Podem ser perfeitamente definidos por equações matemáticas analíticas (ex.: exponenciais complexas x(t) = A e^{j(\omega t + \sigma)} ou ondas senoidais). Seus valores futuros são previstos de forma exata.
* Sinais Aleatórios / Estocásticos: Apresentam incerteza e aleatoriedade inerentes (ex.: ruído térmico, ruído gaussiano com média zero e variância unitária). Não possuem equação determinística, sendo descritos por ferramentas estatísticas e funções de densidade de probabilidade (PDF), representadas empiricamente via histogramas.

A classificação energética determina a métrica de análise aplicável:

* Sinais de Energia: Sinais não periódicos de duração finita cuja integral do quadrado do módulo converge para um valor finito (0 < E_x < \infty), implicando potência média nula (P_x = 0): E_x = \int_{-\infty}^{\infty} |x(t)|^2 dt < \infty
* Sinais de Potência: Sinais periódicos e de duração infinita, onde E_x \to \infty. Sua caracterização ocorre pela potência média calculada ao longo do período T: P_x = \frac{1}{T} \int_{T} |x(t)|^2 dt < \infty

Nota operacional: Qualquer sinal periódico ideal atua rigorosamente como sinal de potência. Porém, ao sofrer truncamento temporal no mundo real (ex.: uma gravação senoidal truncada por uma janela retangular de duração T_0), o sinal transforma-se em um sinal de duração finita, passando a ser classificado estritamente como um sinal de energia.

1.3 Abstração de Sistemas LIT e a Regra Vital da Entrada Nula

Um sistema transforma um sinal de entrada x em uma saída y, denotado por y = H\{x\}. A classe dos sistemas Lineares e Invariantes no Tempo (LIT) constitui a base do processamento clássico:

* Linearidade: Exige a verificação simultânea do princípio da superposição:
  1. Aditividade: H\{x_1(t) + x_2(t)\} = H\{x_1(t)\} + H\{x_2(t)\} = y_1(t) + y_2(t)
  2. Homogeneidade / Escalamento: H\{a \cdot x_1(t)\} = a \cdot H\{x_1(t)\} = a \cdot y_1(t), para a \in \mathbb{C}.
* Teste da Entrada Nula: Como consequência direta e indeferível da homogeneidade (a = 0), todo sistema genuinamente linear DEVE produzir resposta nula para uma entrada nula: H\{0\} = 0 Qualquer presença de offset, bias ou termo constante (b \neq 0) na relação de entrada e saída (como na equação y(t) = a \cdot x(t) + b) viola essa condição, tornando o sistema não linear (sistema afim).
* Invariância no Tempo: Assegura que o comportamento dinâmico do sistema não se altera ao longo do tempo. Se y_1(t) é a resposta a x_1(t), a resposta a uma entrada atrasada x_2(t) = x_1(t - t_0) será estritamente a saída atrasada na mesma proporção: y_2(t) = y_1(t - t_0).

1.4 Convolução, Memória e a Geometria Temporal dos Sistemas

A resposta de qualquer sistema LIT a uma entrada arbitrária é completamente determinada pela sua resposta ao impulso unitário (h[n] no discreto ou h(t) no contínuo). A decomposição do sinal de entrada em uma soma ponderada de impulsos deslocados permite obter a saída através da operação de convolução:

* Convolução no Tempo Discreto (Somatório): y[n] = x[n] * h[n] = \sum_{k=-\infty}^{\infty} x[k] h[n - k]
* Convolução no Tempo Contínuo (Integral): y(t) = x(t) * h(t) = \int_{-\infty}^{\infty} x(\tau) h(t - \tau) d\tau

A resposta ao impulso mapeia também as propriedades operacionais do sistema:

* Memória: Sistemas estáticos (sem memória) possuem saída dependente apenas do instante atual (ex.: y(t) = k \cdot x(t)). Sistemas dinâmicos possuem memória, com a saída dependendo de valores passados ou futuros (ex.: acumuladores, integradores ou equações diferenciais/diferenças).
* Causalidade: Um sistema é causal se a saída em t_0 depende exclusivamente de entradas em instantes t \le t_0. No domínio discreto, um sistema LIT é causal se e somente se h[n] = 0 para todo n < 0. Sistemas não causais dependem de valores futuros (viáveis em processamento off-line em computadores, mas irrealizáveis em tempo real).
* Regra de Suporte Temporal (Suporte Finito Discreto): Se uma sequência x[n] possui N_1 amostras não nulas e h[n] possui N_2 amostras não nulas, o comprimento do sinal de saída y[n] resultante da convolução linear será rigorosamente igual a: N_{out} = N_1 + N_2 - 1

1.5 Domínio da Frequência, Filtragem e Decomposição de Fourier

A Transformada de Fourier atua como uma ferramenta de decomposição integral que transfere a análise do domínio do tempo para o domínio da frequência, decompondo sinais complexos em somatórios infinitos de exponenciais complexas e senoides: X(j\omega) = \int_{-\infty}^{\infty} x(t) e^{-j\omega t} dt

* Teorema da Convolução: A operação de convolução no domínio do tempo equivale à multiplicação algébrica simples no domínio da frequência.
  * No tempo contínuo: \mathcal{F}\{x(t) * h(t)\} = X(j\omega) \cdot H(j\omega)
  * No tempo discreto (DTFT / DFT): \mathcal{F}\{x[n] * h[n]\} = X(e^{j\omega}) \cdot H(e^{j\omega}) \quad \text{ou, em frequências discretas (DFT):} \quad X[k] \cdot H[k] Ressalva formal: Diferencia-se rigidamente os índices do domínio do tempo (n) e do domínio da frequência (\omega para frequência contínua ou k para bins discretos de frequência).
* Efeito Gibbs: O truncamento de uma série de Fourier infinita para a aproximação de sinais contendo descontinuidades (como a onda quadrada) gera oscilações e sobressinais (ringing) persistentes nas bordas da descontinuidade. Esse efeito demonstra analiticamente por que o filtro ideal do tipo "parede de tijolos" (brick-wall) é irrealizável fisicamente, apresentando uma resposta ao impulso não causal e infinitamente oscilatória no tempo (\text{sinc}(t)).
* Arquitetura de Filtragem e Trade-Offs Clássicos: Filtros digitais e analógicos são classificados quanto às bandas de seleção em: Passa-Baixas, Passa-Alta, Passa-Faixa e Rejeita-Faixa. Os principais estilos aproximativos apresentam trade-offs operacionais marcantes:
  1. Butterworth: Apresenta resposta de magnitude máxima plana na faixa de passagem, sem ripple, ao custo de uma transição mais suave entre as faixas.
  2. Chebyshev: Proporciona uma atenuada taxa de transição (corte abrupto), porém introduz oscilações (ripple) na faixa de passagem (Tipo I) ou de rejeição (Tipo II).
  3. Bessel: Destaca-se pela resposta de fase estritamente linear, garantindo um atraso de grupo constante e preservando a forma de onda temporal sem distorção de fase.
* Aplicações Clínicas (Análise de EEG): A Transformada de Fourier e os filtros são indispensáveis na extração de características em sinais com baixa relação sinal-ruído, como o Eletroencefalograma (EEG), subdividido nas bandas espectrais: Delta (0,5\text{--}4\text{ Hz}), Theta (4\text{--}8\text{ Hz}), Alfa (8\text{--}13\text{ Hz}), Beta (13\text{--}30\text{ Hz}) e Gama (>30\text{ Hz}).

Com o domínio dessa base conceitual rigorosa, é possível antecipar os equívocos analíticos mais frequentes observados na prática de modelagem e simulação computacional de sistemas.

# 2. TABELA DE ERROS COMUNS E COMO CORRIGI-LOS

A diagnose sistemática de falhas conceituais desempenha um papel pedagógico crucial no amadurecimento técnico do engenheiro. A identificação proativa de armadilhas matemáticas intuitivas previne erros grosseiros de especificação de hardware, sobrecarregamento de buffers em tempo de execução e interpretações incorretas dos dados espectrais obtidos em simulações.

Erro Conceitual / Equívoco Típico	Por que o Raciocínio Falha (Causa Raiz)	Correção Rigorosa e Regra Prática	Impacto Prático no Projeto/Análise
1. Classificar y(t) = a \cdot x(t) + b (b \neq 0) como sistema linear.	O aluno confunde a geometria cartesiana de uma reta (y = ax + b) com a definição estrita de operador linear na engenharia.	Regra da Entrada Nula: Testar se H\{0\} = 0. Na equação com bias, para x(t) = 0, y(t) = b \neq 0. O sistema é afim/não linear. Para ser linear, o termo constante b deve ser zero.	Invalidação completa das técnicas de superposição, resposta ao impulso e análise de Fourier no sistema.
2. Assumir que uma senóide truncada no tempo é um sinal de potência.	Associa-se a natureza senoidal ideal (que é um sinal de potência e infinito) ao sinal real medido ou gravado durante uma janela finita.	Critério de Duração: Toda senóide limitada por uma janela de duração T_0 possui integral do quadrado finita (E_x < \infty) e potência média nula no infinito (P_x = 0). É rigorosamente um sinal de energia.	Cálculo incorreto da densidade espectral de energia/potência e falha de dimensionamento de ganho do sistema.
3. Confundir convolução x(t) * h(t) com multiplicação x(t) \cdot h(t).	Supor que o operador asterisco (*) é apenas um símbolo alternativo para a multiplicação ponto a ponto de sinais.	Regra do Mapeamento Operacional: x(t) \cdot h(t) é a modulação direta. x(t) * h(t) é a integral/somatório de superposição com deslocamento temporal \int x(\tau)h(t-\tau)d\tau.	Erro total na resposta temporal do sistema; projeção errônea de filtros e perda de dinâmica do sistema.
4. Dimensionar o buffer de memória com tamanho N_1 em vez de N_1 + N_2 - 1.	Ignora-se a expansão temporal causada pelo espalhamento (memória) da resposta ao impulso h[n] sobre a entrada.	Regra do Suporte Temporal: O comprimento completo do vetor de saída da convolução linear discreta de dois sinais finitos é rigorosamente N_{out} = N_1 + N_2 - 1.	Estouro de memória (buffer overflow), truncamento abrupto do sinal e perda dos dados transitórios de saída.
5. Tentar remover aliasing em DSP pós-amostragem sub-Nyquist.	Acreditar que filtros digitais aplicados por software conseguem discriminar frequências originais de frequências rebatidas.	Teorema de Nyquist: O aliasing realiza uma sobreposição espectral irreversível na conversão A/D. O combate ao aliasing deve ser feito no domínio analógico via filtro Anti-Aliasing antes da amostragem.	Sinal digital corrompido permanentemente; imprecisão em sistemas de diagnóstico (ex.: falso espectro em EEG/ECG).
6. Escolher o filtro ideal ("brick-wall") ignorando o Efeito Gibbs e ringing.	Buscar a resposta de magnitude perfeita no domínio da frequência sem avaliar a resposta do filtro no domínio do tempo.	Limitação de Causalidade e Gibbs: O corte abrupto na frequência gera uma resposta ao impulso \text{sinc}(t) não causal e infinitamente oscilatória, provocando ringing severo no tempo.	Distorção transitória intensa em bordas de sinais quadrados ou de pulso, comprometendo a temporização do circuito.

A consolidação dessas correções pode ser verificada de forma prática através da resolução analítica do questionário estruturado a seguir.

# 3. DEZ QUESTÕES DE REVISÃO ORDENADAS POR DIFICULDADE (COM GABARITO COMENTADO)

A sequência de questões apresentada a seguir foi projetada para promover uma progressão cognitiva contínua. Inicia-se com a fixação operacional de notações e propriedades formais, avança pelo cálculo e análise analítica de sistemas no tempo e frequência, e culmina em diagnósticos complexos de engenharia.

3.1 Nível Básico (Fixação de Conceitos e Notação)

Questão 1 (Notação e Manipulação de Sinais)

Dado o sinal sintético contínuo x(t) = u(t+1) - u(t), expresse matematicamente o sinal y(t) = x(t) + r(t/2), onde u(t) é o degrau unitário e r(t) é a função rampa. Em seguida, determine analiticamente o valor pontual da função f(x) = \delta(-x-2) + 2\delta(x-4) nos pontos x = -2, x = 4 e x = 6, utilizando as propriedades do impulso unitário \delta(x) conforme explicitado no Exemplo 1.3 da fonte principal.

Gabarito Detalhado

1. Expressão do Sinal y(t): O termo x(t) = u(t+1) - u(t) representa um pulso retangular de amplitude 1 que se inicia em t = -1 e finaliza em t = 0. A função rampa escalada no argumento é r(t/2), a qual possui inclinação 1/2 para t \ge 0. Assim, a expressão matemática completa consolidada do sinal é: y(t) = r(t/2) + u(t+1) - u(t)
2. Avaliação da Função f(x) com Impulso Unitário: A função impulso unitário sob amostragem pontual satisfaz: \delta(x - x_0) = \begin{cases} 1, & \text{se } x = x_0 \\ 0, & \text{se } x \neq x_0 \end{cases}
  * Para x = -2: f(-2) = \delta(-(-2) - 2) + 2\delta(-2 - 4) = \delta(2 - 2) + 2\delta(-6) Como \delta(0) = 1 e \delta(-6) = 0: f(-2) = 1 + 2(0) = 1
  * Para x = 4: f(4) = \delta(-(4) - 2) + 2\delta(4 - 4) = \delta(-6) + 2\delta(0) Como \delta(-6) = 0 e \delta(0) = 1: f(4) = 0 + 2(1) = 2
  * Para x = 6: f(6) = \delta(-(6) - 2) + 2\delta(6 - 4) = \delta(-8) + 2\delta(2) Como \delta(-8) = 0 e \delta(2) = 0: f(6) = 0 + 2(0) = 0

Questão 2 (Classificação e Periodicidade de Sinais)

Considere o sinal contínuo dado pela soma de cossenos: x(t) = \cos(2t + 1) + \cos(10t). Prove que x(t) é um sinal periódico e determine o seu período fundamental T.

Gabarito Detalhado

1. Determinação dos Períodos Individuais: Um sinal senoidal na forma \cos(\omega t + \phi) possui período T = \frac{2\pi}{\omega}.
  * Para a primeira parcela, x_1(t) = \cos(2t + 1): Frequência angular \omega_1 = 2 \text{ rad/s} \implies T_1 = \frac{2\pi}{2} = \pi \text{ s}
  * Para a segunda parcela, x_2(t) = \cos(10t): Frequência angular \omega_2 = 10 \text{ rad/s} \implies T_2 = \frac{2\pi}{10} = \frac{\pi}{5} \text{ s}
2. Cálculo do Mínimo Múltiplo Comum (MMC): O período fundamental T da soma é o mínimo múltiplo comum entre os períodos T_1 e T_2: \text{MMC}\left(\pi, \frac{\pi}{5}\right) = \pi Como a razão entre os períodos é um número racional (\frac{T_1}{T_2} = \frac{\pi}{\pi/5} = 5 \in \mathbb{Q}), a soma é estritamente periódica, com período fundamental T = \pi \text{ s}.

Questão 3 (Propriedades Básicas de Sistemas: Causalidade e Memória)

Analise o sistema discreto no tempo com relação de entrada e saída dada por y[n] = x[-n]. Classifique o sistema fundamentadamente quanto à causalidade e à memória (estático ou dinâmico).

Gabarito Detalhado

1. Teste de Causalidade: Um sistema é causal se a saída no instante n_0 depende exclusivamente de instantes n \le n_0. Avaliando o sistema para um instante temporal negativo, por exemplo n_0 = -1: y[-1] = x[-(-1)] = x[1] Para determinar a saída no instante passado n = -1, o sistema requer o valor da entrada no instante futuro n = 1. Portanto, o sistema é não causal.
2. Teste de Memória: Um sistema é estático (sem memória) se a saída no instante n depende estritamente da entrada no mesmo instante n. Como observado no teste de causalidade (y[-1] = x[1]), a saída depende de instantes distintos do atual. Logo, o sistema é dinâmico (possui memória).

3.2 Nível Intermediário (Aplicação e Testes Formais)

Questão 4 (Teste Formal de Linearidade)

Demonstre formalmente, através dos critérios de Aditividade e Homogeneidade, se os seguintes sistemas são Lineares ou Não Lineares: a) Sistema Discreto A: y[n] = n \cdot x[n] b) Sistema Contínuo B: y(t) = a \cdot x(t) + b, com b \neq 0

Gabarito Detalhado

* a) Análise do Sistema Discreto A (y[n] = n \cdot x[n]):
  1. Aditividade: Sejam entradas arbitrárias x_1[n] e x_2[n], cujas saídas individuais são y_1[n] = n x_1[n] e y_2[n] = n x_2[n]. Para uma entrada x_3[n] = x_1[n] + x_2[n], a resposta do sistema é: y_3[n] = n \cdot (x_1[n] + x_2[n]) = n x_1[n] + n x_2[n] = y_1[n] + y_2[n] (Aditividade satisfeita).
  2. Homogeneidade: Multiplicando a entrada por uma constante escalar c: H\{c \cdot x_1[n]\} = n \cdot (c \cdot x_1[n]) = c \cdot (n \cdot x_1[n]) = c \cdot y_1[n] (Homogeneidade satisfeita). Conclusão: O sistema A é estritamente Linear.
* b) Análise do Sistema Contínuo B (y(t) = a \cdot x(t) + b, com b \neq 0):
  1. Teste da Entrada Nula: Aplicando uma entrada estritamente nula x(t) = 0: y(t) = a \cdot (0) + b = b Como b \neq 0, temos H\{0\} = b \neq 0. Conclusão: O sistema B viola o teste da entrada nula e, portanto, é Não Linear (é um sistema afim).

Questão 5 (Energia e Potência de Sinais Truncados)

Calcule a Energia total (E_x) e a Potência média (P_x) do sinal contínuo x(t) = \cos(t). Em seguida, analise o impacto na classificação do sinal se ele for truncado por uma janela retangular no intervalo t \in [0, 2\pi].

Gabarito Detalhado

1. Sinal Senoidal Ideal x(t) = \cos(t) (Duração Infinita):
  * Cálculo da Energia E_x: E_x = \int_{-\infty}^{\infty} |\cos(t)|^2 dt = \int_{-\infty}^{\infty} \frac{1 + \cos(2t)}{2} dt = \left[ \frac{t}{2} + \frac{\sin(2t)}{4} \right]_{-\infty}^{\infty} \to \infty
  * Cálculo da Potência Média P_x (Período T = 2\pi): P_x = \frac{1}{2\pi} \int_{0}^{2\pi} \cos^2(t) dt = \frac{1}{2\pi} \int_{0}^{2\pi} \frac{1 + \cos(2t)}{2} dt = \frac{1}{2\pi} \left[ \frac{t}{2} + \frac{\sin(2t)}{4} \right]_{0}^{2\pi} = \frac{1}{2\pi} \left( \pi + 0 \right) = \frac{1}{2}
  * Classificação: E_x = \infty e P_x = 1/2. Trata-se de um sinal de potência.
2. Sinal Senoidal Truncado no Intervalo t \in [0, 2\pi]:
  * Cálculo da Energia E_{\text{trunc}}: E_{\text{trunc}} = \int_{0}^{2\pi} \cos^2(t) dt = \int_{0}^{2\pi} \frac{1 + \cos(2t)}{2} dt = \left[ \frac{t}{2} + \frac{\sin(2t)}{4} \right]_{0}^{2\pi} = \pi \text{ Joules} < \infty
  * Cálculo da Potência Média P_{\text{trunc}} (Demonstração da Passagem Intermediária): A definição formal da potência média para um sinal observado em um intervalo de tempo T_0 à medida que T_0 \to \infty é: P_{\text{trunc}} = \lim_{T_0 \to \infty} \frac{1}{T_0} \int_{-T_0/2}^{T_0/2} |x_{\text{trunc}}(t)|^2 dt Como x_{\text{trunc}}(t) é nulo fora da janela [0, 2\pi], a integral no numerador simplifica-se para a energia finita calculada no passo anterior (E_{\text{trunc}} = \pi), independente do valor de T_0 (desde que T_0 \ge 2\pi): P_{\text{trunc}} = \lim_{T_0 \to \infty} \frac{1}{T_0} \left( \int_{0}^{2\pi} \cos^2(t) dt \right) = \lim_{T_0 \to \infty} \frac{\pi}{T_0} = 0
  * Classificação: Como a energia total E_{\text{trunc}} = \pi é finita e a potência média P_{\text{trunc}} = 0, o truncamento converte o sinal originalmente de potência em um sinal de energia.

Questão 6 (Dimensionamento de Buffer de Convolução)

Em um sistema de processamento de áudio digital, uma sequência de entrada x[n] com N_1 = 1024 amostras deve ser processada por um filtro digital cuja resposta ao impulso h[n] possui N_2 = 128 amostras. Determine o tamanho mínimo do buffer de memória necessário para armazenar o sinal de saída completo sem truncamento ou perda de dados.

Gabarito Detalhado

1. Aplicação da Regra do Suporte Temporal: O comprimento total do sinal de saída y[n] = x[n] * h[n] resultante da convolução de duas sequências discretas de durações finitas N_1 e N_2 é dado analiticamente por: N_{out} = N_1 + N_2 - 1
2. Cálculo Numérico: N_{out} = 1024 + 128 - 1 = 1151 \text{ amostras} Conclusão: O buffer de memória deve ser dimensionado para alocar no mínimo 1151 amostras.

3.3 Nível Avançado (Cálculo e Análise de Sistemas)

Questão 7 (Cálculo Explícito de Convolução Discreta)

Calcule passo a passo a resposta do sistema y[n] = x[n] * h[n] para os vetores de tempo discreto: x[n] = [3, 2] \quad \text{definido para } n = [0, 1] h[n] = [1, 1, 1] \quad \text{definido para } n = [0, 1, 2]

Gabarito Detalhado

1. Análise do Suporte Temporal e Limites Geométricos:
  * x[n] possui N_1 = 2 amostras, com suporte em n \in [n_{x,\min}, n_{x,\max}] = [0, 1].
  * h[n] possui N_2 = 3 amostras, com suporte em n \in [n_{h,\min}, n_{h,\max}] = [0, 2].
  * Os instantes limítrofes do suporte do sinal de saída y[n] são determinados geometricamente por: n_{\min} = n_{x,\min} + n_{h,\min} = 0 + 0 = 0 n_{\max} = n_{x,\max} + n_{h,\max} = 1 + 2 = 3
  * O número total de amostras não nulas é N_{out} = N_1 + N_2 - 1 = 2 + 3 - 1 = 4, no suporte discreto n \in [0, 3].
2. Expansão do Somatório de Convolução: y[n] = \sum_{k=-\infty}^{\infty} x[k] h[n-k] = x[0] h[n] + x[1] h[n-1] = 3h[n] + 2h[n-1]
3. Cálculo Ponto a Ponto das Amostras de y[n]:
  * Para n = 0: y[0] = 3h[0] + 2h[-1] = 3(1) + 2(0) = 3
  * Para n = 1: y[1] = 3h[1] + 2h[0] = 3(1) + 2(1) = 5
  * Para n = 2: y[2] = 3h[2] + 2h[1] = 3(1) + 2(1) = 5
  * Para n = 3: y[3] = 3h[3] + 2h[2] = 3(0) + 2(1) = 2
4. Vetor Resultante: y[n] = [3, 5, 5, 2] \quad \text{para } n = [0, 1, 2, 3]

Questão 8 (Análise de Aliasing e Frequência Rebatida)

Um sinal analógico senoidal x(t) = \cos(2\pi \cdot 800 \cdot t) de frequência f_0 = 800\text{ Hz} é amostragem por um conversor A/D operando a uma taxa de amostragem f_s = 1000\text{ Hz}. a) O critério de Nyquist foi satisfeito? b) Calcule a frequência aparente rebatida (f_{\text{alias}}) percebida no sinal discreto.

Gabarito Detalhado

1. Avaliação do Critério de Nyquist: A taxa de Nyquist exige f_s \ge 2 f_0 = 2(800) = 1600\text{ Hz}. Como a taxa utilizada é f_s = 1000\text{ Hz} < 1600\text{ Hz}, o critério foi violado, ocorrendo aliasing.
2. Cálculo da Frequência Rebatida (f_{\text{alias}}): Ao amostrar x(t) em t = n T_s = \frac{n}{f_s}: x[n] = \cos\left(2\pi \frac{f_0}{f_s} n\right) = \cos\left(2\pi \frac{800}{1000} n\right) = \cos(2\pi \cdot 0,8 \cdot n) Utilizando a periodicidade e simetria do cosseno em torno de 2\pi: \cos(2\pi \cdot 0,8 \cdot n) = \cos((2\pi - 2\pi \cdot 0,2) n) = \cos(-2\pi \cdot 0,2 \cdot n) = \cos(2\pi \cdot 0,2 \cdot n) A frequência discreta equivalente é f_d = 0,2\text{ ciclos/amostra}. A frequência analógica aparente rebatida na reconstrução é: f_{\text{alias}} = f_d \cdot f_s = 0,2 \times 1000 = 200\text{ Hz}

Questão 9 (Seleção e Trade-off de Estilos de Filtros)

Um engenheiro biomédico precisa projetar um filtro passa-baixas para o pré-processamento de sinais de Eletroencefalograma (EEG) visando à análise precisa das componentes morfológicas das ondas no tempo e à remoção de ruídos de alta frequência acima de 30\text{ Hz}. Compare os filtros Butterworth, Chebyshev e Bessel e indique a escolha mais adequada para esta aplicação.

Gabarito Detalhado

1. Comparativo dos Estilos de Filtros:
  * Butterworth: Possui resposta de magnitude com máxima planicidade na faixa de passagem, sem ripple. Todavia, sua resposta de fase é não linear, introduzindo pequenas distorções de forma no tempo.
  * Chebyshev: Apresenta taxa de transição muito abrupta entre a faixa de passagem e rejeição, mas introduz ripples (oscilações de amplitude). Sua fase é altamente não linear.
  * Bessel: Apresenta resposta de fase estritamente linear na faixa de passagem (atraso de grupo constante).
2. Seleção Justificada: Em análises de sinais de EEG, a preservação da forma de onda temporal (morfologia dos picos clínicos de ERP/EEG) é prioritária. Filtros com fase não linear (como Butterworth e Chebyshev) alteram o alinhamento temporal das componentes espectrais, distorcendo os eventos transitórios cerebrais. Escolha: O Filtro Bessel é o mais adequado por garantir distorção de fase nula no domínio do tempo, preservando com máxima fidelidade a morfologia do sinal de EEG.

3.4 Nível Mestre / Desafio (Síntese e Diagnóstico de Engenharia)

Questão 10 (Diagnóstico de Efeito Gibbs e Convolução Circular vs. Linear)

Em uma plataforma de processamento digital de sinais, um algoritmo calcula a convolução no domínio da frequência multiplicando as Transformadas Rápidas de Fourier (FFT) de duas sequências finitas x[n] (tamanho N_1 = 64) e h[n] (tamanho N_2 = 64). No entanto, os engenheiros observaram dois problemas graves:

1. Aparecimento de oscilações indesejadas (ringing) ao sintetizar o sinal truncando a série de Fourier.
2. Contaminação/corrupção de borda entre o final e o início do sinal filtrado.

Diagnostique analiticamente a causa raiz de ambos os fenômenos e apresente as soluções corretivas necessárias.

Gabarito Detalhado

1. Diagnóstico do Problema 1 (Oscilações e Ringing):
  * Causa Raiz: Trata-se do Efeito Gibbs. O truncamento abrupto de uma série de Fourier infinita equivale a multiplicar o espectro por uma janela retangular, gerando uma convolução no domínio da frequência com uma função \text{sinc}. Isso produz oscilações e sobressinais nas proximidades de descontinuidades no tempo.
  * Solução: Aplicar janelamento suave (suavização de bordas) no domínio do tempo para reduzir as oscilações transitórias.
2. Diagnóstico do Problema 2 (Corrupção de Borda por Convolução Circular):
  * Causa Raiz: A multiplicação de Transformadas de Fourier Discretas (FFT) realiza inerentemente uma convolução circular (periódica) e não a convolução linear desejada. Como o tamanho da FFT utilizada foi de apenas N = 64 e o suporte da convolução linear exige N_{out} = N_1 + N_2 - 1 = 64 + 64 - 1 = 127 amostras, ocorreu aliasing espacial/temporal, sobrepondo o final da sequência ao seu início.
  * Solução: Aplicar Preenchimento com Zeros (Zero-Padding) em ambos os vetores de entrada x[n] e h[n], expandindo seus tamanhos individuais com zeros até no mínimo N_{\text{FFT}} \ge N_1 + N_2 - 1 = 127 pontos (na prática, ajustando para N_{\text{FFT}} = 128, a potência de 2 subsequente) antes de calcular a FFT.

Com a consolidação das resoluções analíticas, o plano estruturado a seguir direciona a rotina de estudos de forma espaçada.

# 4. PLANO DE REVISÃO DE 7 DIAS

A metodologia de estudo distribuído e espaçado garante a retenção conceitual de longo prazo e consolida a capacidade de resolução de problemas complexos. O cronograma abaixo organiza as sessões ativas ao longo de uma semana.

  DIA 1          DIA 2          DIA 3          DIA 4          DIA 5          DIA 6          DIA 7
┌──────────────┐┌──────────────┐┌──────────────┐┌──────────────┐┌──────────────┐┌──────────────┐┌──────────────┐
│Classificação ││Propriedades  ││Decomposição  ││Mecânica da   ││Transformada  ││Cadeia de     ││Simulação     │
│de Sinais e   ││de Sistemas e ││por Impulsos e││Convolução    ││de Fourier e  ││Filtragem e   ││Global e      │
│Amostragem    ││Linearidade   ││Resposta h[n] ││Discreta/Cont.││Análise EEG   ││Estilos Filtro││Diagnóstico   │
└──────────────┘└──────────────┘└──────────────┘└──────────────┘└──────────────┘└──────────────┘└──────────────┘


Cronograma Diário de Estudo Ativo

Dia 1: Classificação de Sinais e Amostragem

* Atividades: Revisar a distinção entre x(t) e x[n]. Praticar equações de sinais determinísticos (exponenciais complexas, degrau u(t), rampa r(t) e delta de Dirac \delta(t)).
* Exercício Chave: Calcular a energia E_x e potência P_x de sinais contínuos e analisar os impactos do Teorema da Amostragem de Nyquist e aliasing.
* Autoavaliação: Resolver as Questões 1, 2 e 5 do Kit de Revisão.

Dia 2: Propriedades de Sistemas e Teste de Linearidade/Invariância

* Atividades: Estudar as abstrações formais de sistemas LIT. Aplicar sistematicamente os testes formais de aditividade e homogeneidade.
* Exercício Chave: Executar o Teste da Entrada Nula (H\{0\} = 0) em variadas relações entrada-saída e verificar causalidade e memória.
* Autoavaliação: Resolver as Questões 3 e 4 do Kit de Revisão.

Dia 3: Decomposição por Impulsos e Resposta ao Impulso

* Atividades: Compreender a representação de sinais discretos como somas de impulsos unitários deslocados e escalados.
* Exercício Chave: Interpretar o significado físico e matemático da resposta ao impulso h[n] e h(t) na caracterização de sistemas estáticos, dinâmicos e causais.
* Autoavaliação: Estudar o Exemplo 3.1 da apostila e revisar as propriedades da convolução com o impulso \delta[n-k].

Dia 4: Mecânica da Convolução Discreta e Contínua

* Atividades: Dominar o somatório e a integral de convolução. Praticar a técnica mecânica de inversão e deslocamento da função no tempo.
* Exercício Chave: Deduzir o suporte temporal de saída (N_{out} = N_1 + N_2 - 1) e calcular convoluções contínuas envolvendo funções degrau e exponenciais.
* Autoavaliação: Resolver as Questões 6 e 7 do Kit de Revisão.

Dia 5: Transformada de Fourier e Domínio da Frequência

* Atividades: Estudar a decomposição espectral em exponenciais complexas e senoides. Compreender o Teorema da Convolução no tempo e frequência.
* Exercício Chave: Analisar o Efeito Gibbs em descontinuidades e estudar a aplicação prática da Transformada de Fourier na extração das bandas do EEG (Delta, Theta, Alfa, Beta, Gama).
* Autoavaliação: Resolver a Questão 8 e revisar a Seção 4.2 da apostila.

Dia 6: Cadeia de Filtragem e Estilos de Filtros

* Atividades: Estudar a topologia dos filtros digitais e analógicos (Passa-Baixas, Passa-Alta, Passa-Faixa, Rejeita-Faixa).
* Exercício Chave: Comparar rigorosamente os trade-offs de magnitude e fase dos filtros Butterworth (máxima planicidade), Chebyshev (transição rápida com ripple) e Bessel (fase linear).
* Autoavaliação: Resolver a Questão 9 do Kit de Revisão.

Dia 7: Simulação Global de Prova e Diagnóstico Metacognitivo

* Atividades: Realizar a resolução cega (sem consulta) da Questão 10 e reavaliar o questionário completo sob limitação de tempo.
* Exercício Chave: Auditar os erros cometidos utilizando a Tabela de Erros Comuns (Seção 2) para identificar lacunas remanescentes e realizar correções pontuais.

Para otimizar o tempo durante as sessões do plano de estudos, utilize o guia de localização rápida de conteúdos a seguir.

# 5. GUIA DE FONTES ESPECÍFICAS PARA CONSULTA RÁPIDA

O mapeamento a seguir indexa os tópicos teóricos e práticos diretamente aos capítulos do material didático e aos artefatos interativos disponíveis, otimizando o fluxo de consulta durante as revisões.

- Mapeamento da Apostila Principal ('Apostila ELT 576 Atualizada.pdf')

* Capítulo 1 (Sinais): Páginas 3 a 20
  * Seções 1.1 a 1.3 (Páginas 4 a 8): Características de sinais (contínuo vs. discreto), discretização e amostragem; Seção 1.2 — Sinais Bidimensionais (representação matricial de imagens em escala de cinza, pág. 6); Seção 1.3 — Sinais Determinísticos vs. Aleatórios (ruído gaussiano, PDF e histogramas, págs. 7-8).
  * Seção 1.4 (Páginas 9 a 16): Descrição matemática de sinais — Equação exponencial complexa e relação de Euler (1.4.1); Funções Degrau e Rampa (1.4.2, Exemplos 1.1 e 1.2); Função Delta de Dirac e Impulso Unitário (1.4.3, Exemplo 1.3).
  * Seções 1.5 a 1.7 (Páginas 17 a 20): Sinais periódicos e cálculo do período por MMC (Exemplo 1.4); Energia e Potência de Sinais (Integrais formais 1.3 e 1.4, Exemplo de cálculo para \cos(t)); Seção 1.7 — Exercícios de fixação do Capítulo 1 (Página 20).
* Capítulo 2 (Sistemas): Páginas 21 a 28
  * Introdução e Seção 2.1 (Páginas 21 a 25): Conceito geral de sistemas e representação por blocos (pág. 21); Classificação de sistemas — Invariância no tempo e contra-exemplos (2.1.1, Exemplo 2.1); Sistemas Lineares, propriedades de aditividade, homogeneidade e teorema da superposição (2.1.2, Exemplo 2.2).
  * Seções 2.2 e 2.3 (Páginas 25 a 28): Memória de Sistemas — Sistemas Estáticos sem memória (2.2.1) e Dinâmicos com memória (2.2.2); Sistemas Causais e Não Causais (2.1.3, Exemplo 2.3); Seção 2.3 — Exercícios de fixação do Capítulo 2 (Página 28).
* Capítulo 3 (Convolução): Páginas 29 a 37
  * Introdução e Seção 3.1 (Páginas 29 a 34): Apresentação da convolução como resposta no tempo (pág. 29); Somatório de Convolução em Tempo Discreto — Decomposição por impulsos (3.1.1); Resposta ao impulso e fórmula da convolução discreta (3.1.2); Tabela de Propriedades da Convolução (Tabela 3.1.1); Aplicações em Redes Neurais Convolucionais - CNN (Figura 3.1); Exemplo prático de convolução discreta passo a passo (Exemplo 3.1).
  * Seções 3.2 e 3.3 (Páginas 34 a 37): Integral de Convolução em Tempo Contínuo — Formulação matemática integral (3.2.1 e 3.2.2); Tabela de Propriedades Contínuas (Tabela 3.2.1); Exemplo prático contínuo entre e^{-at}u(t) e u(t) (Exemplo 3.2); Seção 3.3 — Exercícios de fixação do Capítulo 3 (Página 37).
* Capítulo 4 (Transformada de Fourier): Páginas 38 a 45
  * Seção 4.1 (Páginas 38 a 41): Decomposição integral em senoides e exponenciais complexas (Equação 4.1.1); Fenômeno do Efeito Gibbs por truncamento da série de Fourier (Figura 4.3).
  * Seção 4.2 (Páginas 40 a 42): Aplicação clínica em sinais de EEG e mapeamento espectral das bandas de frequência (Delta, Theta, Alfa, Beta, Gama - Figura 4.5).
  * Seções 4.3 e 4.4 (Páginas 42 a 45): Propriedades da Transformada de Fourier (Linearidade, Convolução no tempo como multiplicação na frequência, Exemplos 4.1 e 4.2); Seção 4.4 — Exercícios de fixação do Capítulo 4 (Página 45).
* Capítulo 5 (Filtragem Digital): Páginas 45 a 63
  * Seção 5.1 (Páginas 48 a 52): Tipos fundamentais de filtros — Passa-Baixas (5.1.1), Passa-Alta (5.1.2), Passa-Faixa (5.1.3) e Rejeita-Faixa (5.1.4).
  * Seção 5.2 (Páginas 53 a 60): Estilos de Filtros — Filtro Chebyshev (5.2.1), Filtro Bessel (5.2.2) e Filtro Butterworth (5.2.3); Exemplos 5.1 e 5.2; Análise comparativa e conclusão dos trade-offs de projeto (5.2.4).
  * Seções 5.3 e 5.4 (Páginas 61 a 63): Seção 5.3 — Aplicações de Filtragem Digital (Páginas 61-62); Seção 5.4 — Exercícios de fixação do Capítulo 5 (Página 63).