import pandas as pd

df = pd.read_excel("BaseFinanceiroAnalise.xlsx")

def analisar():

    resultado = "ANÁLISE DE CRÉDITO\n\n"

    encontrou = False

    for _, linha in df.iterrows():

        saldo = linha["Saldo_Aberto"]
        limite = linha["Limite_Credito"]

        if limite > 0:

            percentual = (saldo / limite) * 100

            if percentual >= 80:

                encontrou = True

                resultado += (
                    f"- {linha['Nome_Cliente']} "
                    f"(Utilização: {percentual:.1f}% "
                    f"do limite de crédito)\n"
                )

    if not encontrou:

        resultado += "Nenhum cliente utilizando mais de 80% do limite."

    return resultado



