import pandas as pd

df = pd.read_excel("BaseFinanceiroAnalise.xlsx")

def analisar():

    resultado = "ANÁLISE DE RISCO\n\n"

    clientes = df[df["Saldo_Aberto"] > 0]

    if len(clientes) == 0:
        return "Nenhum cliente com risco identificado."

    for _, linha in clientes.iterrows():

        score = linha["Score_Credito"]
        saldo = linha["Saldo_Aberto"]
        situacao = linha["Situacao"]

        if score < 300 or (
            situacao == "Atrasada" and saldo > 8000
        ):

            classificacao = "ALTO RISCO"

        elif (
            (situacao == "Atrasada" and saldo > 3000)
            or
            (300 <= score < 500)
        ):

            classificacao = "MÉDIO RISCO"

        else:

            classificacao = "BAIXO RISCO"

        resultado += (
            f"- {linha['Nome_Cliente']} | "
            f"{classificacao} | "
            f"Score: {score} | "
            f"Saldo: R$ {saldo:.2f} | "
            f"Situação: {situacao}\n"
        )

    return resultado


