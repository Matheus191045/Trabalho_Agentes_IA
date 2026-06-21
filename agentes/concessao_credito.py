import pandas as pd

df = pd.read_excel("BaseFinanceiroAnalise.xlsx")


def analisar_concessao(cliente_nome: str) -> str:
    nome_lower = cliente_nome.lower()
    clientes = df["Nome_Cliente"].unique()
    match = next((c for c in clientes if c.lower() == nome_lower), None)

    if match is None:
        match = next((c for c in clientes if nome_lower in c.lower()), None)

    if match is None:
        return f"Cliente '{cliente_nome}' não encontrado na base."

    registros = df[df["Nome_Cliente"] == match]

    saldo_aberto = registros["Saldo_Aberto"].sum()
    limite = registros["Limite_Credito"].iloc[0]
    score = registros["Score_Credito"].iloc[0]
    inadimplente = (registros["Situacao"] == "Atrasada").any()
    utilizacao = (saldo_aberto / limite * 100) if limite > 0 else 0

    motivos_negacao = []
    motivos_cautela = []

    if score < 300:
        motivos_negacao.append(f"score de crédito muito baixo ({score})")
    elif score < 500:
        motivos_cautela.append(f"score de crédito intermediário ({score})")

    if inadimplente:
        if saldo_aberto > 5000:
            motivos_negacao.append(f"inadimplente com saldo alto em aberto (R$ {saldo_aberto:,.2f})")
        else:
            motivos_cautela.append(f"possui parcela(s) em atraso (saldo R$ {saldo_aberto:,.2f})")

    if utilizacao >= 100:
        motivos_negacao.append(f"limite de crédito esgotado ({utilizacao:.1f}% utilizado)")
    elif utilizacao >= 80:
        motivos_cautela.append(f"utilização elevada do limite ({utilizacao:.1f}%)")

    if motivos_negacao:
        decisao = "NEGAR CRÉDITO"
    elif motivos_cautela:
        decisao = "AVALIAR COM CAUTELA"
    else:
        decisao = "CONCEDER CRÉDITO"

    linhas = [
        f"=== ANÁLISE DE CONCESSÃO DE CRÉDITO ===",
        f"Cliente        : {match}",
        f"Score          : {score}",
        f"Saldo em aberto: R$ {saldo_aberto:,.2f}",
        f"Limite         : R$ {limite:,.2f}",
        f"Utilização     : {utilizacao:.1f}%",
        f"Inadimplente   : {'Sim' if inadimplente else 'Não'}",
        f"",
        f"DECISÃO: {decisao}",
    ]

    if motivos_negacao:
        linhas.append("\nMotivos de negação:")
        linhas += [f"  - {m}" for m in motivos_negacao]

    if motivos_cautela:
        linhas.append("\nPontos de atenção:")
        linhas += [f"  - {m}" for m in motivos_cautela]

    return "\n".join(linhas)
