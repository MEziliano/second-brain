import json
import os
import re
from datetime import datetime
from typing import Any, Dict, List

import yaml
from openai import OpenAI
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    openai_api_key: SecretStr = SecretStr("Nao Coloque Sua Chave Aqui")
    openai_model: str = "gpt-4.1-mini"

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


class AnalisadorDePropostas:
    def __init__(self):
        settings = Settings()
        self.client = OpenAI(
            api_key=settings.openai_api_key.get_secret_value()
        )
        self.model_name = settings.openai_model

    def etapa_1_extracao_basica(self, proposta_texto: str) -> Dict[str, Any]:
        """Zero-Shot: Extração direta de informações estruturadas"""

        prompt = f"""Extraia as seguintes informações da proposta:
        - Título do projeto (chave: titulo)
        - Departamento (chave: departamento)
        - Orçamento solicitado (apenas números, chave: orcamento)
        - Prazo de execução (apenas número de meses, chave: prazo)

        Proposta: {proposta_texto}

        Retorne em formato JSON puro."""

        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}]
        )

        content = response.choices[0].message.content
        if not content:
            raise ValueError("A resposta da API veio vazia.")

        # Clean up markdown code blocks if present
        if content.startswith("```json"):
            content = content[7:]
        if content.endswith("```"):
            content = content[:-3]

        return json.loads(content.strip())

    def _avaliar_proposta(self, proposta_info: Dict[str, Any]) -> str:
        prompt = f"""Avalie a seguinte proposta de projeto:
        Título: {proposta_info.get("titulo")}
        Departamento: {proposta_info.get("departamento")}
        Orçamento: {proposta_info.get("orcamento")}
        Prazo: {proposta_info.get("prazo")}

        Forneça uma avaliação inicial sobre a clareza, relevância e
        viabilidade aparente."""

        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}]
        )
        content = response.choices[0].message.content
        return content if content else ""

    def _criticar_avaliacao(
        self, avaliacao: str, proposta_info: Dict[str, Any]
    ) -> str:
        prompt = f"""Atue como um crítico experiente. Analise a avaliação
        feita sobre a proposta abaixo e identifique pontos cegos, vieses
        ou riscos não considerados.

        Proposta: {proposta_info.get("titulo")}
        Avaliação Inicial: {avaliacao}

        Seja construtivo mas rigoroso."""

        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}]
        )
        content = response.choices[0].message.content
        return content if content else ""

    def _refinar_avaliacao(self, avaliacao: str, critica: str) -> str:
        prompt = f"""Com base na avaliação inicial e na crítica recebida,
        elabore uma avaliação final refinada e mais equilibrada.

        Avaliação Inicial: {avaliacao}
        Crítica: {critica}
        """

        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}]
        )
        content = response.choices[0].message.content
        return content if content else ""

    def etapa_2_avaliacao_com_reflexao(
        self, proposta_info: Dict[str, Any]
    ) -> Dict[str, str]:
        """Reflection: Avaliação inicial + crítica + versão melhorada"""

        # Passo 1: Avaliação inicial
        avaliacao_inicial = self._avaliar_proposta(proposta_info)

        # Passo 2: Reflexão crítica
        critica = self._criticar_avaliacao(avaliacao_inicial, proposta_info)

        # Passo 3: Avaliação refinada
        avaliacao_final = self._refinar_avaliacao(avaliacao_inicial, critica)

        return {
            "inicial": avaliacao_inicial,
            "critica": critica,
            "final": avaliacao_final,
        }

    def _processar_resposta_cot(self, response_content: str) -> Dict[str, str]:
        """Extrai o raciocínio e a decisão das tags XML."""
        raciocinio_match = re.search(
            r"<raciocinio>(.*?)</raciocinio>", response_content, re.DOTALL
        )
        decisao_match = re.search(
            r"<decisao>(.*?)</decisao>", response_content, re.DOTALL
        )

        raciocinio = (
            raciocinio_match.group(1).strip()
            if raciocinio_match
            else response_content
        )
        decisao = (
            decisao_match.group(1).strip()
            if decisao_match
            else "Decisão não encontrada."
        )

        return {"raciocinio": raciocinio, "decisao": decisao}

    def etapa_3_analise_viabilidade_cot(
        self, proposta_info: Dict[str, Any], orcamento_disponivel: float
    ) -> Dict[str, str]:
        """Chain-of-Thought: Análise multi-critério com raciocínio explícito"""

        # Tratamento seguro para orçamento caso venha como string ou número
        orcamento_solicitado = proposta_info["orcamento"]
        if isinstance(orcamento_solicitado, str):
            # Remove caracteres não numéricos se necessário
            orcamento_solicitado = "".join(
                filter(str.isdigit, orcamento_solicitado)
            )
            orcamento_solicitado = float(orcamento_solicitado)

        prompt = f"""Atue como um avaliador rigoroso de projetos de pesquisa.
Analise a viabilidade desta proposta.

Proposta:
- Título: {proposta_info["titulo"]}
- Departamento: {proposta_info["departamento"]}
- Orçamento solicitado: R$ {orcamento_solicitado:,.2f}
- Prazo: {proposta_info["prazo"]} meses

Orçamento disponível do departamento: R$ {orcamento_disponivel:,.2f}

Critérios Rígidos de Avaliação:
1. **Orçamento**:
   - Se o valor solicitado ultrapassar 100% do orçamento disponível e não
     houver menção explícita e garantida de verba externa: REJEITADO.
   - Se o valor ocupar mais de 50% do orçamento: Exige "APROVADO COM AJUSTES"
     (redução de custos).
2. **Cronograma e Ética**:
   - Prazos irrealistas para a natureza do projeto (ex: ensaio clínico em
     poucos meses): REJEITADO.
   - Infrações éticas graves (ex: iniciar pesquisa com seres humanos antes
     da aprovação do comitê de ética): REJEITADO IMEDIATAMENTE.
     ATENÇÃO: Começar recrutamento ANTES da aprovação ética é VIOLAÇÃO GRAVE.
3. **Viabilidade Técnica**:
   - Falta de infraestrutura crítica ou riscos não mitigados:
     "APROVADO COM AJUSTES" ou "REJEITADO" dependendo da gravidade.

Instrução de Tolerância Zero:
Se QUALQUER um dos critérios de REJEIÇÃO for atendido (especialmente ética
ou orçamento estourado), a decisão final DEVE ser "REJEITADO".
NÃO suavize para "APROVADO COM AJUSTES" se houver uma falha fatal.

Passos para o Raciocínio:
1. Analise a conformidade ética e legal (Busque ativamente por infrações).
2. Verifique a viabilidade do cronograma (considerando burocracia,
   recrutamento, importação, etc.).
3. Calcule o impacto orçamentário percentual.
4. Avalie riscos técnicos.
5. Defina a categoria final baseada nos critérios rígidos acima.

Formato de Saída Obrigatório:
Utilize as seguintes tags XML para estruturar sua resposta:
<raciocinio>
[Seu raciocínio detalhado passo a passo aqui, citando explicitamente as
violações ou riscos encontrados]
</raciocinio>
<decisao>
[Sua decisão final: APROVADO, APROVADO COM AJUSTES ou REJEITADO]
[Breve justificativa em uma frase]
</decisao>
"""

        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}]
        )

        content = response.choices[0].message.content
        if not content:
            return {"raciocinio": "", "decisao": ""}
        return self._processar_resposta_cot(content)

    def processar_proposta_completa(
        self, proposta_texto: str, orcamento_dept: float
    ) -> Dict[str, Any]:
        """Pipeline completo demonstrando as três técnicas"""
        print("=" * 60)
        print("ETAPA 1: Extração Básica (Zero-Shot)")
        print("=" * 60)
        info = self.etapa_1_extracao_basica(proposta_texto)
        print(json.dumps(info, indent=2, ensure_ascii=False))

        print("\n" + "=" * 60)
        print("ETAPA 2: Avaliação com Reflexão")
        print("=" * 60)
        avaliacao = self.etapa_2_avaliacao_com_reflexao(info)
        print(f"Avaliação Inicial: {avaliacao['inicial'][:200]}...")
        print(f"\nCrítica: {avaliacao['critica'][:200]}...")
        print(f"\nAvaliação Final: {avaliacao['final'][:200]}...")

        print("\n" + "=" * 60)
        print("ETAPA 3: Análise de Viabilidade (Chain-of-Thought)")
        print("=" * 60)
        viabilidade = self.etapa_3_analise_viabilidade_cot(
            info, orcamento_dept
        )
        print(f"Raciocínio: {viabilidade['raciocinio'][:200]}...")
        print(f"Decisão: {viabilidade['decisao']}")

        return {
            "info": info,
            "avaliacao": avaliacao,
            "viabilidade": viabilidade,
        }


def carregar_propostas_yaml(arquivo: str) -> List[Dict[str, Any]]:
    """Carrega propostas de um arquivo YAML"""
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            conteudo = yaml.safe_load(f)
            if not conteudo or "propostas" not in conteudo:
                print(f"Aviso: Arquivo {arquivo} vazio ou mal formatado.")
                return []
            return conteudo["propostas"]
    except FileNotFoundError:
        print(f"Erro: Arquivo {arquivo} não encontrado.")
        return []
    except yaml.YAMLError as exc:
        print(f"Erro ao ler YAML: {exc}")
        return []


# Uso demonstrativo
if __name__ == "__main__":
    arquivo_propostas = "propostas.yaml"
    propostas = carregar_propostas_yaml(arquivo_propostas)

    if propostas:
        # Cria diretório de saída com timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = os.path.join("outputs", timestamp)
        os.makedirs(output_dir, exist_ok=True)
        print(f"Diretório de saída: {output_dir}")

        analyzer = AnalisadorDePropostas()
        for i, proposta in enumerate(propostas, 1):
            print(f"\n\n{'#' * 80}")
            print(f"PROCESSANDO PROPOSTA {i}")
            print(f"{'#' * 80}\n")

            texto = proposta.get("texto", "")
            orcamento_dept = proposta.get("orcamento_dept", 0)

            if texto:
                resultado = analyzer.processar_proposta_completa(
                    proposta_texto=texto,
                    orcamento_dept=orcamento_dept
                )

                # Define nome do arquivo individual
                titulo_safe = resultado["info"].get("titulo", "sem_titulo")
                titulo_safe = "".join(
                    c for c in titulo_safe
                    if c.isalnum() or c in (' ', '-', '_')
                ).strip().replace(' ', '_')

                nome_arquivo = f"proposta_{i}_{titulo_safe[:50]}.md"
                caminho_arquivo = os.path.join(output_dir, nome_arquivo)

                # Salva no relatório markdown individual
                with open(caminho_arquivo, "w", encoding="utf-8") as f_md:
                    titulo = resultado["info"].get("titulo", f"Proposta {i}")
                    f_md.write(f"# {i}. {titulo}\n\n")

                    f_md.write("## 1. Extração de Dados\n")
                    f_md.write("```json\n")
                    f_md.write(
                        json.dumps(
                            resultado["info"], indent=2, ensure_ascii=False
                        )
                    )
                    f_md.write("\n```\n\n")

                    f_md.write("## 2. Avaliação com Reflexão\n")
                    f_md.write("**Avaliação Inicial:**\n")
                    f_md.write(f"{resultado['avaliacao']['inicial']}\n\n")

                    f_md.write("**Crítica:**\n")
                    f_md.write(f"{resultado['avaliacao']['critica']}\n\n")

                    f_md.write("**Avaliação Final:**\n")
                    f_md.write(f"{resultado['avaliacao']['final']}\n\n")

                    f_md.write("## 3. Análise de Viabilidade\n")
                    f_md.write("**Raciocínio (Chain-of-Thought):**\n")
                    f_md.write(f"{resultado['viabilidade']['raciocinio']}\n\n")
                    f_md.write("**Decisão Final:**\n")
                    f_md.write(f"{resultado['viabilidade']['decisao']}\n\n")

                print(f"Relatório salvo: {caminho_arquivo}")
            else:
                print(f"Aviso: Proposta {i} sem texto.")

    else:
        print("Nenhuma proposta encontrada para processar.")
