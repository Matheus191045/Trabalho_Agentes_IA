

import pandas as pd

df = pd.read_excel("BaseFinanceiroAnalise.xlsx")

def responder(pergunta):

    pergunta = pergunta.lower()

    if "saldo" in pergunta:

        saldo = df["Saldo_Aberto"].sum()

        return f"Saldo pendente total: R$ {saldo:,.2f}"

    elif "atrasado" in pergunta:

        atrasados = df[df["Situacao"] == "Atrasada"]

        return f"Existem {len(atrasados)} registros em atraso."

    return "Não entendi a pergunta."



