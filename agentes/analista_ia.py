import pandas as pd

from agentes.agente_financeiro import responder as financeiro
from agentes.cobranca import analisar as cobranca
from agentes.credito import analisar as credito
from agentes.risco import analisar as risco

df = pd.read_excel("BaseFinanceiroAnalise.xlsx")


def analisar_carteira():

    saldo_total = df["Saldo_Aberto"].sum()

    qtd_atrasados = len(
        df[df["Situacao"] == "Atrasada"]
    )

    qtd_limite = len(
        df[
            (df["Saldo_Aberto"] / df["Limite_Credito"]) >= 0.80
        ]
    )

    qtd_alto_risco = len(
        df[
            (df["Score_Credito"] < 300)
            |
            (
                (df["Situacao"] == "Atrasada")
                &
                (df["Saldo_Aberto"] > 8000)
            )
        ]
    )

    contexto = f"""
RESUMO EXECUTIVO

Saldo total pendente: R$ {saldo_total:,.2f}

Quantidade de clientes em atraso: {qtd_atrasados}

Quantidade de clientes de alto risco: {qtd_alto_risco}

Clientes acima de 80% do limite: {qtd_limite}

DETALHES

{financeiro('saldo')}

{cobranca()}

{credito()}

{risco()}
"""

    return contexto


