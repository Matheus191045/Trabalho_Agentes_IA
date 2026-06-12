import pandas as pd

df = pd.read_excel("BaseFinanceiroAnalise.xlsx")

def analisar():

    atrasados = df[df["Situacao"] == "Atrasada"]

    resultado = "Clientes em atraso:\n"

    for _, linha in atrasados.iterrows():
        resultado += (
            f"- {linha['Nome_Cliente']} "
            f"(Saldo: R$ {linha['Saldo_Aberto']:.2f})\n"
        )

    return resultado