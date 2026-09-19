# Semana 1 -  Sinais e Sistemas

[AULA GRAVADA](https://www.youtube.com/watch?v=s-NkI5mS6U0)

## Sinais 
* Sinal 
    - **Informação** sobre o comportamento ou natureza de algum fênomeno.
    * Sistema: Uma entidade, que pode ser física, digital, biológica ou mineral, etc. sua princial função é alterar sinais.

### Sinais contínuos e discretos no tempo
- Sinal contínuo é quando dentro de um sistema ao verificar um sinal existente **infinitas possibilidades**.
- Sinal discreto é quando há uma variação entre apenas **dois pontos**

### Sinais determinísticos e aleatórios
- Determinístico: Onde é possível calcular
- Aleatório: Onde é possível estimar apenas utilizando alguma distruição de probabilidade. 

#### Descrição matemática de sinais contínuos
$$
x(t)
$$

Exponencial complexa (Relação de Euler)
$$
g(t) = Ae^{(\delta+j \omega)t} = Ae^{\delta t} [cos(\omega t)+ jsen(\omega t)]

\\
A cos(\omega_0 t _\phi) = dfrac{A}{2} e^{j \phi} e^{j \omega} + \dfrac{A}{2}e^{j \phi} e^{j \omega}
$$

#### Descrição matemática de sinais contínuos

* Função degrau unitário
$$
u(t) = \begin{cases}
   1,t & > 0 \\
   0,t & <0
\end{cases}
$$

* Função rampa
$$
ramp(t) = \begin{cases}
   t,t & >0 \\
   0,t & <0
\end{cases} = \int u(t)=tu(t)
$$

* Função impulso (delta de Dirac)
$$
\sigma(t) = \begin{cases}
   1\epsilon, |t| <\epsilon /2 \\
   0,|t| >\epsilon/2, \text{ para } \epsilon \rarr0
\end{cases}

$$
* Sinal perióidico
$$
g(t)= g(t+nT), \forall n \isin N
$$


O intervalo **positivo mínimo** que a função se repete é chamado de período funamental $T_0= > f_01T_0 e w_0 = 2\pi f_0$

Período da soma de sinais: o período fundamental é obtido através do mínimo múltiplo comum (**MMC**) dos períodos individuais ou através do máximo denominador comum (**MDC**) das frequências. 
Se $T_1/T_2$ é irracional, então a soma é aperiódica.

- Energia e potência
Na maioria dos sistemas físicos, a energia é diretamente proporcional a esta constante

$$
P_x = \dfrac{1}{T} \int_r |x(t)²| dt

$$

#### Descrição matemática de sinais discretos
**Notação** $g[n]$ para *n* inteiro 
$$

x[n]= e^{i \Omega n}
$$

----

> No contexto da IA, o que se faz é controlar o fluxo da entrada para a saída do modelo. O que nada mais é um processamento de sinais. 

## Sistemas

Onde ocorre a transformação do sinal através das entradas, para assim, manipular suas saídas

### Invariância temporal
Sistema mantém suas características independentemente do instante em que a entrada for aplicada. 
$$
x(t) \xrightarrow{H} y(t) \\
x(t-t_0) \xrightarrow{over} y(t-t_0)

$$
### Homogeneidade
Um escalonamento na entrada causa um mesmo escalonamento na saída.  
### Aditividade
A saída para uma soma de entradas é a soma das saídas individuais. 

#### HOMOGENEIDADE + ADITIVIDADE = LINEARIDADE
**Princípio da Superposição**: A resposta para qualquer sinal de entrada pode ser determinada pela decomposição da entrada em partes mais simples e pela determinação de cada resposta individual

$ x_1[n] \xrightarrow{} y_1[n]$ e $x_2[n]\xrightarrow{} y_2[n]$, então para qualquer *k* complexo $k_1x_1[n]+k_2x_2[n] = k_1y_1[n]+k_2y_2[n]$

### Memória
$e[n] = R_i[n]$ - saída depende instantaneamente da entrada. **Sistema estático**

$i(t) = C \dfrac{dv(t)}{dt}$ - valor da saída depende também de outros instantes. **Sistemas dinâmicos**

### Causalidade
$y[n]=\dfrac{1}{3}(x[n]+x[n-1]+x[-2])$ **causal**: saída atual depende apenas dos instantes atual e passados da entrada

$y[n]=\dfrac{1}{3}(x[n+1]+x[n]+x[n-1])$ **não-causal** saída atual depende de instante(s) futuro(s)
> Sistemas práticos contínuos são causais
> Sistemas discretos não necessariamente.