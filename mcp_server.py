import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

from mcp.server.fastmcp import FastMCP
from agentes.agente_financeiro import responder as _financeiro
from agentes.cobranca import analisar as _cobranca
from agentes.credito import analisar as _credito
from agentes.risco import analisar as _risco
from agentes.analista_ia import analisar_carteira as _analisar_carteira
from agentes.agente_regras import consultar_regras as _consultar_regras
from agentes.concessao_credito import analisar_concessao as _concessao

mcp = FastMCP("Assistente Financeiro IA")


@mcp.tool()
def consultar_politica_financeira(pergunta: str) -> str:
    """Consulta a política financeira da empresa via RAG. Use para perguntas sobre regras, bloqueios, manuais e documentos internos."""
    return _consultar_regras(pergunta) 


@mcp.tool()
def resumo_carteira() -> str:
    """Retorna resumo executivo completo da carteira: saldo total em aberto, número de inadimplentes, clientes de alto risco e utilização de limite."""
    return _analisar_carteira()


@mcp.tool()
def consultar_saldo(pergunta: str) -> str:
    """Consulta o saldo em aberto e a situação financeira dos clientes."""
    return _financeiro(pergunta)


@mcp.tool()
def listar_inadimplentes() -> str:
    """Lista todos os clientes com pagamentos atrasados e seus saldos em aberto. Use para análise de cobrança e renegociação."""
    return _cobranca()


@mcp.tool()
def analisar_uso_credito() -> str:
    """Analisa a utilização do limite de crédito dos clientes. Identifica quem ultrapassou 80% do limite disponível."""
    return _credito()


@mcp.tool()
def classificar_risco_clientes() -> str:
    """Classifica todos os clientes em ALTO RISCO, MÉDIO RISCO ou BAIXO RISCO com base em score de crédito e situação de inadimplência."""
    return _risco()


@mcp.tool()
def analisar_concessao_credito(cliente: str) -> str:
    """Analisa se é seguro conceder crédito a um cliente específico. Avalia score, inadimplência e utilização do limite. Informe o nome do cliente."""
    return _concessao(cliente)


if __name__ == "__main__":
    mcp.run()
