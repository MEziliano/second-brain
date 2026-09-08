# Variável padrão (será sobrescrita se você passar SUBJECT=nome no terminal)
SUBJECT ?= nova_disciplina

# 1. Cria a estrutura de pastas
criar-estrutura:
	@echo "📂 Criando estrutura para: $(SUBJECT)"
	@mkdir -p $(SUBJECT)/Docs $(SUBJECT)/input $(SUBJECT)/Resolver $(SUBJECT)/Tests
	@echo "✅ Pastas criadas com sucesso!"

# 2. Cria o ambiente virtual com uv
setup-env:
	@echo "🐍 Configurando ambiente virtual com uv em $(SUBJECT)/.venv..."
	@uv venv $(SUBJECT)/.venv
	@echo "✅ Ambiente criado! Para ativar: source $(SUBJECT)/.venv/bin/activate"

# 3. Target "Mestre" que chama os dois de uma vez
init: criar-estrutura setup-env
	@echo "🎉 Disciplina $(SUBJECT) 100% pronta para estudar!"

# Informa ao Make que estes não são arquivos reais
.PHONY: criar-estrutura setup-env init

# Usando o nome padrão
# make criar-estrutura

# Passando o nome da disciplina como variável
# make criar-estrutura SUBJECT=Machine_Learning_Avancado