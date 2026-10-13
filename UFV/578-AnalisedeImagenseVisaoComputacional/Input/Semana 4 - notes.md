# Semana 04 - Análise de Imagens via RNC    
- **AULA 10:** Classificação de Imagens
- **AULA 11:** Detecção de Objetos
- **AULA 12:** Redes Adversárias Generativas
    - **AULA PRÁTICA 8:** Classificação de Imagens
    - **AULA PRÁTICA 9:** Detecção de objetos
    - **AULA PRÁTICA 10:** Redes Adversárias Generativas

## Aula 10 - Classificação de Imagens via Redes Neurais Convolucionais 
[VIDEO](https://youtu.be/KSVdOn5KXXA)


Os modelos são gerados e aprimorados a cada ano. Os modelos já foram treinados com vastos conjuntos de dados, seus parâmetros já foram definidos e repassados ao grande público.

*  Classificação de imagens: a partir de um conjunto de dados de imagens categorizar os tipos determinados através da convulação.


Antes de tudo: **não recebi o vídeo nem o anexo do "caderno"** nesta conversa 📭 — então vou mapear as **fontes canônicas do campo** (papers + docs oficiais do GCP). Se você me passar os nomes/links do material, eu re-monto as citações no seu caderno.

Também sei que você **já domina supervisionado**, então vou pular a base de ML e atacar as ideias *não óbvias*.

---

# 🧠 Mapa Mental — 5 Pilares da Classificação por CNN

```
                        CLASSIFICAR IMAGEM
                              │
   ┌──────────────┬───────────┴───────────┬──────────────┐
   │              │                       │              │
 [C1] COMO LÊ   [C2] O QUE CONSTRÓI   [C3] POR QUE    [C4] COMO
  pixels→       ABSTRAÇÃO             NÃO TRAM      APROVEITAR
  filtros      (profundidade)         (regulariz.)  (transfer)
   │              │                       │              │
   └──────┬───────┴───────────┬───────────┘              │
          │                   │                          │
          └──── [C5] ONDE TUDO QUEBRA ───────────────────┘
                 (dados, métrica, atalhos, produção)
```

---

## C1 — 🔄 "A rede não vê a imagem: ela desliza o mesmo mini-detector por toda ela"

1. **Nome:** Equivalência translacional nasce do **compartilhamento de pesos**, não do pooling.
2. **Por que importa:** é a *única* diferença conceitual entre CNN e MLP. Quem não vê isso acha que convolução é "filtro de Photoshop". É isso que faz uma CNN treinar com 10³ imagens onde uma MLP precisaria de 10⁷.
3. **Exemplo prático:** ao aprender uma nova arquitetura (ResNet, EfficientNet), leia primeiro o tamanho de kernel e o stride — não o número de parâmetros. No trabalho: se o seu objeto **só aparece no canto inferior direito** (ex.: logotipo em nota fiscal), o compartilhamento de pesos está te *prejudicando* → você precisa de crop/tile antes.
4. **Relaciona-se com:** C2 (o campo receptivo define o "alcance" desse detector), C3 (menos parâmetros = regularização implícita), C5 (domínio e atalhos).
5. **Explicação Feynman**
   - **Básico (12 anos):** é um carimbo. Você molha o carimbo no papel e bate, bate, bate, da esquerda pra direita. Não importa onde bate — o desenho do carimbo é o mesmo. Por isso um cachorro no canto é reconhecido igual ao do centro. 🐶
   - **Intermediário:** um filtro $k\times k$ produz um *feature map* por *sliding window*; os pesos do filtro são compartilhados em todas as posições espaciais. Isso é **equivariância** (mover a entrada move a saída). O **pooling** (max/average) transforma equivariância em **invariância** aproximada.
   - **Avançado:** trade-off real — compartilhamento de pesos reduz parâmetros de $O(HWC \cdot O)$ para $O(k^2 C \cdot O)$, mas impõe um *prior* rígido. Se a tarefa não é translation-equivariant (muitas imagens médicas, satélite, OCR com layout), o prior vira **viés indutivo errado**. Alternativas: attention (ViT), deformable convs, ou coordenadas como feature extra.
   - **Mestre:** ⚠️ edge cases — invariância excessiva destrói informação espacial ("duas janelas" vs "uma janela grande"); padding cria *boundary artifacts*; stride >1 quebra equivariância (aliasing — ver Zhang 2019, "Making Convolutional Networks Shift-Invariant Again"); e CNNs treinadas em ImageNet têm *prior de textura* que ignora a relação espacial global.
6. **Erro típico:** achar que "conv3x3 + pooling = a rede é invariante a translação, rotação e escala". **Invariância a rotação/escala não é gratuita** — CNNs são notoriamente *fracas* nisso sem augmentation.
7. **Fontes:** IBM — *What are CNNs* [[7]]; Yamashita et al., *CNNs: an overview and applications in radiology* [[13]]; Vision Book MIT, cap. 24 [[12]].

> 🎯 **No PMLE:** quando o enunciado descreve "mesmo objeto em posições variadas" e dataset pequeno → a resposta certa costuma ser *model customizado com CNN/backbone pré-treinado*, não AutoML tabular.

---

## C2 — 🪜 "Profundidade não é potência de fogo: é uma escada de abstrações"

1. **Nome:** Hierarquia de features + crescimento **multiplicativo** do campo receptivo.
2. **Por que importa:** é a ponte entre " pixels" e "conceito". É também o motivo pelo qual **camadas baixas são transferíveis e camadas altas não** (a chave do C4).
3. **Exemplo prático:** ao depurar um modelo ruim, visualize as ativações das camadas intermediárias: se as primeiras respondem a bordas mas as últimas ficam saturadas, seu problema é profundidade/receptive field, não learning rate. Estudar: aprenda arquiteturas como **escada**, não como lista de nomes.
4. **Relaciona-se com:** C1 (cada camada amplia o "carimbo"), C3 (mais profundidade exige mais regularização), C4 (o que congelar).
5. **Explicação Feynman**
   - **Básico:** é como ler. Você junta letras → palavras → frases → sentido. Um caco de vidro sozinho não diz nada; a frase diz. 🔤
   - **Intermediário:** camadas 1–3 aprendem bordas/gradientes de cor; intermediárias, texturas e partes; profundas, objetos e *todo*. O campo receptivo cresce com $\approx$ soma/Produto de $(k-1)$ por camada + efeitos do stride, então **profundidade compra contexto mais barato que largura**.
   - **Avançado:** por isso o estado da arte migrou de 3×3 empilhadas (VGG→ResNet): 2 camadas 3×3 têm campo receptivo de 5×5 com **menos parâmetros e mais não-linearidade**. O gargalo passa a ser *otimização* (vanishing gradient, degradação) → **residual connections** são a resposta real, não a convolução.
   - **Mestre:** ⚠️ profundidade tem retornos decrescentes em datasets pequenos; campos receptivos gigantes podem **diluir** o objeto de interesse (crucial em *whole-slide pathology* e detecção de lesão pequena — precisa de FPN/pyramid). Há debate ativo na literatura se a "hierarquia semântica" é garantida ou emergente/context-dependente.
6. **Erro típico:** "mais camadas = melhor". Sem normalização/resíduos, o modelo **piora com profundidade** (degradation problem), e você culpa o dataset.
7. **Fontes:** Krizhevsky/Sutskever/Hinton, *ImageNet Classification with Deep CNNs* (NeurIPS 2012) [[16]][[17]]; Aman's AI Journal CS230 — CNN [[39]]; revisão de arquiteturas 2026 [[37]].

> 🎯 **No PMLE:** arquitetura é *meio* da solução. A pergunta de prova costuma testar se você escolhe **depth vs latency vs cost** no serving, não SOTA em ImageNet.

---

## C3 — 🛡️ "A CNN já é regularização; o resto é só ajuste fino de viés-variância"

1. **Nome:** O ganho de performance em visão vem de **restrição estrutural da hipótese**, não de memorização.
2. **Por que importa:** como você vem de tabular, o instinto é "mais features + capacity + ensemble". Em visão, isso te leva a overfit instantâneo. Aqui **menos liberdade = mais generalização**.
3. **Exemplo prático:** dataset com 2.000 imagens? Antes de trocar de arquitetura, aplique **augmentation + weight decay + early stopping**. No trabalho real, um `RandomResizedCrop` + `flip` bem escolhido costuma valer mais que qualquer troca de backbone.
4. **Relaciona-se com:** C1 (o prior estrutural), C2 (profundidade aumenta variância), C4 (congelar backbone = congelar prior), C5 (augmentation precisa respeitar o domínio).
5. **Explicação Feynman**
   - **Básico:** é ensinar alguém a reconhecer gatos só com fotos de gato na grama, no escuro, de lado e de cabeça pra baixo. Assim, ele aprende "gato", não "grama". 🌱
   - **Intermediário:** duas fontes de regularização — **(a) implícita**: weight sharing + local connectivity podam o espaço de hipóteses; **(b) explícita**: augmentation, dropout, BatchNorm (que também estabiliza gradientes e permite LR maior), weight decay, early stopping, label smoothing.
   - **Avançado:** augmentation cara no CPU pode **subutilizar a GPU** → use augmentation na GPU/TPU (TF `data_service`) ou no input pipeline (TFDS). Em fine-tuning, augmentation agressiva **destrói** o prior pré-treinado; BatchNorm + freeze exige `training=False` para não corromper running stats. Trade-off: capacity ↑ → precisa regularization ↑, mas regularization excessiva → underfit e *miscalibration*.
   - **Mestre:** ⚠️ **BatchNorm memoriza exemplos** (ataques de membership inference; vazamento entre train/test se stats forem recalculadas sobre o test set). Augmentation fora de distribuição (ex.: rotação 180° em imagem de raio-X ou em *digitalis* de plantas) **inverte o rótulo semanticamente**. Debate atual: parte do ganho do augmentation vem de *implicit curriculum*, e MixUp/CutMix produzem `soft labels` que quebram a suposição de one-hot da cross-entropy [[51]].
6. **Erro típico:** usar augmentation como checklist aleatório ("flip, rotaciona, ajusta cor") sem perguntar **"isso ainda é a mesma classe no mundo real?"**.
7. **Fontes:** Zhang et al., *mixup: Beyond Empirical Risk Minimization* [[51]]; Smucny et al., *Data augmentation with Mixup* [[57]]; Yamashita et al. [[13]].

> 🎯 **No PMLE:** perguntas de "dataset pequeno/desequilibrado" têm resposta quase sempre em **augmentation + re-weighting + transfer**, nunca "trocar a loss por uma mais exótica".

---

## C4 — 🎁 "Nunca comece do zero: features baixas são universais, as altas são suas"

1. **Nome:** Transfer learning = **reuso da hierarquia** (C2), decide-se por **distância de domínio**.
2. **Por que importa:** é a decisão com maior ROI em CV aplicado. É também o maior peso do seu objetivo (exame): Vertex AI tem **AutoML, Model Garden, Feature Store, batch/online prediction** — quase tudo em torno dessa ideia.
3. **Exemplo prático:** rotina de trabalho — (1) tire baseline com backbone pré-treinado congelado + sua cabeça; (2) só descongele camadas altas se houver ≥ 5–10k imagens/domínio parecido. Para estudar: faça **um** pipeline de fine-tuning e repita com 3 backbones, em vez de ler 10 artigos.
4. **Relaciona-se com:** C2 (é a hierarquia que autoriza o congelamento), C3 (LR discriminativo + augmentation leve), C1 (se o domínio de origem é muito diferente, a equivariância aprendida pode não valer).
5. **Explicação Feynman**
   - **Básico:** você não aprende o alfabeto de novo pra ler um livro diferente — só aprende o vocabulário novo. 📖
   - **Intermediário:** **feature extraction** = congela o `convolutional base`, treina só a cabeça [[42]]; **fine-tuning** = descongela parcialmente com **learning rate menor que o do scratch** (LR discriminativo) [[48]]. Heurística de congelamento: congele as camadas cedo (bordas/texturas transferem bem) e solte as tarde [[46]].
   - **Avançado:** decida por **similaridade de domínio + tamanho de dados**. Regra 2×2: domínio próximo + dados muitos → full FT; domínio distante + dados poucos → frozen features + nova cabeça (ou *self-supervised* pré-treino). Eficiência real: **mixed precision (FP16/BF16)**, `tf.data` pipeline, `XLA`, e escolha de backbone por Pareto accuracy × latency × custo no endpoint.
   - **Mestre:** ⚠️ **catastrophic forgetting** ao descongelar sem memória; **catastrophic *neglect*** — FT em dataset enviesado pode *piorar* o prior; **pretrained weights podem herdar vazamento de ImageNet/CLIP** (memorização de imagens com conteúdo pessoal — sério em medical/satellite); há literatura mostrando que **random initialization + mais steps** supera fine-tuning quando domínio é muito diferente — mito do "pretrain sempre vence".
6. **Erro típico:** descongelar tudo com o *mesmo* learning rate → destrói o backbone em 3 épocas e o modelo "de repente" vira um treino do zero com 500 imagens.
7. **Fontes:** TensorFlow — *Transfer learning and fine-tuning* [[42]]; Lightly — *Introduction to Transfer Learning* [[43]]; Vertex AI Model Garden [[31]].

> 🎯 **No PMLE:** a pergunta-chave é **selecionar a ferramenta certa**: AutoML Image (baseline rápido, dados medianos, zero código) vs **custom trained model em Vertex AI + Model Garden** (precisa de arquitetura específica, augmentation custom, controle de serving) vs batch prediction para milhões de imagens via GCS/BigQuery [[25]][[27]].

---

## C5 — 🕳️ "A rede não entende o mundo: ela acha o atalho estatístico mais barato"

1. **Nome:** *Shortcut learning* / viés de textura + o gargalo real está em **taxonomia, labels, leakage e métrica**.
2. **Por que importa:** é a diferença entre "97% na validação" e modelo inútil em produção. Especialista não questiona a arquitetura primeiro — questiona **o que a métrica está te deixando esconder**.
3. **Exemplo prático:** antes de treinar, rode um **"baseline estúpido"**: classificador só pelo *tamanho do arquivo* ou pela marca d'água do fundo. Se ele bate 80%, seu dataset vazou. Ao aprender algo novo, sempre pergunte: "qual é o baseline trivial desta tarefa?".
4. **Relaciona-se com:** todos — C1 (atalhos aparecem por invariância espacial), C2 (camadas altas pegam o atalho mais fácil), C3 (augmentation precisa quebrar o atalho, não alimentá-lo), C4 (o prior do ImageNet traz *texture bias*).
5. **Explicação Feynman**
   - **Básico:** é o aluno que decora "a resposta certa é sempre C". Passa na prova, mas não sabe nada. 🎓
   - **Intermediário:** CNNs são **otimizadores de atalho**: textura > forma (Geirhos et al. 2019), fundo > objeto, cor > estrutura. Em classificação, a escolha da métrica segue o problema: accuracy só com classes balanceadas; **AUC-PR** para desbalanceadas; top-k accuracy para multi-classe ambígua; e threshold de decisão é escolha de *custo de negócio*, não técnica.
   - **Avançado:** leakage específico de imagem é sutil — **mesma fonte/fotograma/paciente** em treino e teste (médico: split por paciente; satélite: split geográfico/temporal). Produção: drift de câmera/iluminação, custo por chamada de *online prediction*, necessidade de **batch prediction** para milhões de imagens em GCS [[29]][[30]], e explicabilidade (Grad-CAM/feature attribution) para auditoria.
   - **Mestre:** ⚠️ CNNs perdem para um *patch* adversarial minúsculo; **calibração** (ECE) importa mais que AUC quando você decide em threshold; modelo com 99% de accuracy pode estar aprendendo *apenas* o fundo (contexto espúrio) — e o debate atual (shortcut learning, *spurious correlations*, avaliação out-of-distribution com benchmarks tipo WILDS/DiagNets) é sobre **generalização real, não acurácia**.
6. **Erro típico:** dividir o dataset com `shuffle=True` **por imagem** quando imagens provêm do mesmo grupo → métrica inflada e deploy fracassado. É o erro nº 1 em projetos reais de CV.
7. **Fontes:** Vertex AI — *Get inferences from an image classification model* (online vs batch) [[25]]; Heyer, *Vertex AI Batch Predictions* [[29]]; Reza et al., *A comprehensive review of CNNs* (2026) [[37]].

---

## 📝 Cornell Notes — versão de bolso

| Esquerda (pergunta) | Direita (resposta-âncora) |
|---|---|
| Por que conv ≠ MLP? | Peso compartilhado → equivariância translacional (C1) |
| Por que profundidade? | Campo receptivo ↑ multiplicativamente → hierarquia (C2) |
| Por que funciona com poucos dados? | Prior estrutural + augmentation = regularização (C3) |
| O que eu congelo? | Camadas baixas = universais; altas = específicas (C4) |
| Por que 97% não serve? | Atalhos + leakage por grupo, métrica errada (C5) |

---


## Aula 11 - Detecção de Objetos via CNN

