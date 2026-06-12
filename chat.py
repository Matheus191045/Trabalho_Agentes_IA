import ollama
from agentes.coordenador import processar_pergunta

print("=" * 50)
print("ASSISTENTE FINANCEIRO IA")
print("=" * 50)

while True:

    pergunta = input("\nPergunta: ")

    if pergunta.lower() == "sair":
        break

    dados = processar_pergunta(pergunta)

    print("\n=== DADOS DOS AGENTES ===")
    print(dados)

    resposta = ollama.chat(
        model="qwen3:1.7b",
        messages=[
                    {
            "role": "system",
            "content": """
        Você é um analista financeiro corporativo.

        REGRAS:

        - Utilize somente os dados recebidos.
        - Nunca invente números.
        - Nunca invente clientes.
        - Nunca altere valores.
        - Nunca altere scores.
        - Nunca faça cálculos próprios.
        - Utilize exatamente as classificações de risco recebidas.
        - Não contradiga os agentes.
        - Seja objetivo.
        - Responda em português.
        - Utilize o termo "inadimplência" em vez de "default".

        - Não classifique clientes por conta própria.
        - Não interprete percentuais.
        - Não realize cálculos matemáticos.
        - Não deduza informações ausentes.
        - Se a informação não estiver nos dados, informe que não é possível concluir.
        - Clientes em atraso são candidatos prioritários para cobrança.
        - Clientes acima do limite de crédito devem ser monitorados.


        Quando houver RESUMO EXECUTIVO:
        utilize os números informados no resumo.

        Quando houver clientes classificados:
        respeite exatamente ALTO RISCO, MÉDIO RISCO e BAIXO RISCO.

        Formato:

        RESUMO:
        ...

        PONTOS DE ATENÇÃO:
        - ...

        RECOMENDAÇÃO:
        ...
        """
        },
            {
                "role": "user",
                "content": f"""
                            Pergunta do usuário:
                            {pergunta}

                            Dados dos agentes:
                            {dados}

                            IMPORTANTE:

                            - Utilize exclusivamente os dados apresentados.
                            - Não utilize conhecimento externo.
                            - Não utilize informações de perguntas anteriores.
                            - Considere apenas os dados recebidos na pergunta atual.
                            - Não faça suposições.
                            - Não invente informações.
                            

                            Responda somente com base nos dados acima.
                            """
            }
        ]
    )

    print("\n=== RESPOSTA IA ===")
    print(resposta["message"]["content"])

