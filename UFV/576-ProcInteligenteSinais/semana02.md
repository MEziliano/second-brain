# Semana 02 - Convolução

## Análise de sistemas no domínio do tempo
- **Convolução**
    Uma convulução é a combinação de duas funções para a geração de uma terceira, integrando dois conjuntos de informações.
    Transformar a entrada em sinais mais simples. 

$x[n]= \displaystyle\sum^{\infin}_{k=-\infin} x[k]\delta[n-k]$

### Convolução Discreta
- Operação que combina duas sequências (ex.: x[n] e sistema h[n]) para gerar uma terceira (saída y[n]). É uma forma de misturar duas sequências de dados. Pense nela como uma **média móvel ponderada**, onde os pesos são definidos pelo kernel (resposta ao impulso).

$$

y[n] = (x*h)[n] =  \displaystyle\sum^{\infin}_{k=-\infin} x[k]\delta[n-k]
$$