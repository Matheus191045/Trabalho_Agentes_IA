from agentes.agente_financeiro import responder as financeiro
from agentes.cobranca import analisar as cobranca
from agentes.credito import analisar as credito
from agentes.risco import analisar as risco
from agentes.analista_ia import analisar_carteira
from agentes.agente_regras import consultar_regras


def processar_pergunta(pergunta):

    pergunta = pergunta.lower()


    if "manual" in pergunta:
        return consultar_regras(pergunta)

    elif "regra" in pergunta:
        return consultar_regras(pergunta)

    elif "política" in pergunta:
        return consultar_regras(pergunta)

    elif "politica" in pergunta:
        return consultar_regras(pergunta)

    elif "documento" in pergunta:
        return consultar_regras(pergunta)


    elif "bloqueado" in pergunta:
        return consultar_regras(pergunta)

    elif "bloqueio" in pergunta:
        return consultar_regras(pergunta)





    # CONSULTA GERAL DA CARTEIRA
    elif "carteira" in pergunta:
        return analisar_carteira()

    elif "saudável" in pergunta:
        return analisar_carteira()

    elif "saudavel" in pergunta:
        return analisar_carteira()

    elif "situação geral" in pergunta:
        return analisar_carteira()

    elif "situacao geral" in pergunta:
        return analisar_carteira()

    elif "resumo" in pergunta:
        return analisar_carteira()

    # FINANCEIRO
    elif "saldo" in pergunta:
        return financeiro(pergunta)

    # COBRANÇA
    elif "atrasad" in pergunta:
        return cobranca()

    elif "pagou" in pergunta:
        return cobranca()

    elif "inadimplente" in pergunta:
        return cobranca()
    

    elif "renegociação" in pergunta:
        return cobranca()

    elif "renegociacao" in pergunta:
        return cobranca()


    # CRÉDITO
    elif "limite" in pergunta:
        return credito()

    elif "crédito" in pergunta:
        return credito()

    # RISCO
    elif "risco" in pergunta:
        return risco()



    





    return "Não encontrei um agente adequado para responder."


