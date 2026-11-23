# Técnicas de Prompting com LLMs

Este projeto demonstra três técnicas fundamentais de **prompt engineering** usando a API da OpenAI. É projetado para fins educacionais, mostrando como diferentes estratégias de prompting podem melhorar a qualidade e confiabilidade das respostas de LLMs.

## 📋 O que são as Técnicas?

O projeto implementa três técnicas de prompting aplicadas à análise de propostas de pesquisa:

1. **Zero-Shot**: Extração direta de informações estruturadas sem exemplos prévios
2. **Reflection**: Melhoria iterativa através de auto-crítica (avaliação → crítica → refinamento)
3. **Chain-of-Thought (CoT)**: Raciocínio explícito passo a passo para decisões complexas

## 🚀 Configuração Inicial

### 1. Pré-requisitos

- Python 3.12 ou superior
- Conta OpenAI com API key ([obtenha aqui](https://platform.openai.com/api-keys))

### 2. Instalação

```bash
# Navegue até o diretório
cd exercicio_1_prompting

# Crie um ambiente virtual
python3.12 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Instale as dependências com Poetry
poetry install
```

### 3. Configurar a API Key

Crie um arquivo `.env` na raiz do projeto (copie do `.env.example`):

```bash
# .env
OPENAI_API_KEY=sua-chave-openai-aqui
```

⚠️ **IMPORTANTE**: Nunca commite o arquivo `.env`!

## 📚 Estrutura do Projeto

```
exercicio_1_prompting/
├── main.py              # Script principal com as técnicas de prompting
├── propostas.yaml       # Propostas de pesquisa para análise
├── .env                 # Configurações (API key) - NÃO COMMITADO
├── .env.example         # Exemplo de configuração
├── README.md            # Este arquivo
├── pyproject.toml       # Dependências do projeto
└── outputs/             # Relatórios gerados (criado automaticamente)
```

## 🎯 Como Usar

### Executar o Script

```bash
python main.py
```

O script irá:
1. Ler as propostas do arquivo `propostas.yaml`
2. Processar cada proposta através das 3 etapas
3. Gerar relatórios em markdown na pasta `outputs/`

### Estrutura do Processamento

Cada proposta passa por três etapas:

**ETAPA 1: Extração Básica (Zero-Shot)**
- Extrai título, departamento, orçamento e prazo
- Retorna JSON estruturado

**ETAPA 2: Avaliação com Reflexão**
- Gera avaliação inicial da proposta
- Critica a própria avaliação
- Refina a avaliação com base na crítica

**ETAPA 3: Análise de Viabilidade (Chain-of-Thought)**
- Analisa viabilidade com raciocínio explícito
- Verifica conformidade ética, orçamentária e técnica
- Decide: APROVADO, APROVADO COM AJUSTES ou REJEITADO

## 📖 Componentes Principais

### Settings (Pydantic Settings)
Gerencia configurações do ambiente:
- Lê a API key do arquivo `.env`
- Valida configurações automaticamente
- Usa `SecretStr` para proteger dados sensíveis

### AnalisadorDePropostas
Classe principal que implementa as três técnicas:
- `etapa_1_extracao_basica()`: Zero-shot prompting
- `etapa_2_avaliacao_com_reflexao()`: Reflection pattern
- `etapa_3_analise_viabilidade_cot()`: Chain-of-thought

### Arquivo YAML
Define as propostas a serem analisadas:
```yaml
propostas:
  - texto: |
      Título: Nome do Projeto
      Departamento: Nome
      Orçamento: R$ 50.000
      Prazo: 12 meses
      Descrição: ...
    orcamento_dept: 200000
```

## 🐛 Resolução de Problemas

### Erro: API key não encontrada
- Verifique se o arquivo `.env` existe na raiz do projeto
- Confirme que a variável `OPENAI_API_KEY` está definida
- Certifique-se de estar no diretório correto

### Erro: "propostas.yaml not found"
- O arquivo deve estar no mesmo diretório que `main.py`
- Verifique o nome do arquivo (case-sensitive)

### Problemas com a API OpenAI
- Confirme que sua chave é válida e tem créditos disponíveis
- Verifique os limites de rate da sua conta

### Diretório outputs/ não criado
- O script cria automaticamente, mas verifique permissões
- Cada execução cria um subdiretório com timestamp

## 📚 Recursos Adicionais

- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [OpenAI Best Practices](https://platform.openai.com/docs/guides/prompt-engineering)
- [Chain-of-Thought Prompting](https://arxiv.org/abs/2201.11903)
- [Pydantic Documentation](https://docs.pydantic.dev/)

## 📄 Licença

Este projeto é para fins educacionais. Use livremente para aprender e ensinar!

---

**Desenvolvido para o curso de IA Generativa - Universidade Federal de Viçosa**
