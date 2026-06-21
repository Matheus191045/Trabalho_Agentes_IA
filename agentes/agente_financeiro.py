import pandas as pd

df = pd.read_excel("BaseFinanceiroAnalise.xlsx")

_clientes = df["Nome_Cliente"].unique().tolist()


def responder(pergunta):
    pergunta_lower = pergunta.lower()

    cliente = next(
        (c for c in _clientes if c.lower() in pergunta_lower),
        None
    )

    if cliente:
        registros = df[df["Nome_Cliente"] == cliente]
        saldo = registros["Saldo_Aberto"].sum()
        situacoes = registros["Situacao"].value_counts().to_dict()
        sit_str = ", ".join(f"{s}: {n}" for s, n in situacoes.items())
        return (
            f"Cliente: {cliente}\n"
            f"Saldo em aberto: R$ {saldo:,.2f}\n"
            f"Situações: {sit_str}"
        )

    if "saldo" in pergunta_lower:
        saldo = df["Saldo_Aberto"].sum()
        return f"Saldo pendente total: R$ {saldo:,.2f}"

    if "atrasado" in pergunta_lower or "inadimplente" in pergunta_lower:
        atrasados = df[df["Situacao"] == "Atrasada"]
        return f"Existem {len(atrasados)} registros em atraso."

    return "Não entendi a pergunta."



