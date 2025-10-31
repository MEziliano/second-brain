NIAS/  
│  
├── data/                  # Dados brutos e processados  
│   ├── raw/               # Dados originais (imutáveis)  
│   ├── processed/         # Dados limpos/transformados  
│   └── external/          # Dados de fontes externas (ex: APIs)  
│  
├── notebooks/             # Jupyter/Colab notebooks (exploração)  
│  
├── pages/                 # Páginas do dashboard (streamlit) 
│  
├── src/                   # Código-fonte  
│   ├── preprocessing/     # Scripts de limpeza e feature engineering  
│   ├── models/            # Treino, validação e arquiteturas  
│   └── utils/             # Funções auxiliares (logs, helpers)  
│  
├── models/                # Modelos treinados (binários/pickle)  
│   ├── trained/           # Versões finais  
│   └── experiments/       # Testes durante desenvolvimento  
│  
├── evaluations/           # Métricas, plots e relatórios  
│   ├── metrics/           # Arquivos JSON/CSV com resultados  
│   └── visualizations/    # Gráficos e análises  
│  
├── config/                # Arquivos de configuração (YAML/JSON)  
│  
├── docs/                  # Documentação (markdown, relatórios)  
│  
├── pyproject.toml         # Dependências do Python  
├── README.md              # Guia do projeto  
└── .gitignore             # Ignorar arquivos desnecessários (ex: dados, .pyc)  