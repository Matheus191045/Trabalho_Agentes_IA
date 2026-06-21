import asyncio
import os
import re
import sys
from pathlib import Path
import ollama
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

SYSTEM_PROMPT = """Você é um analista financeiro corporativo com acesso a ferramentas especializadas.

Ao receber uma pergunta, use a ferramenta mais adequada para obter os dados e responda
com base EXCLUSIVAMENTE no que ela retornar.

REGRAS:
- Nunca invente números, clientes ou valores
- Nunca faça cálculos próprios
- Nunca use informações de perguntas anteriores
- Responda sempre em português
- Se a informação não estiver nos dados, informe que não é possível concluir

Formato da resposta:
RESUMO:
...

PONTOS DE ATENÇÃO:
- ...

RECOMENDAÇÃO:
...
"""


def strip_think(text: str) -> str:
    """Remove tags <think>...</think> geradas pelo Qwen 3."""
    return re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()


def mcp_tools_para_ollama(mcp_tools) -> list:
    """Converte a lista de tools do MCP para o formato esperado pelo Ollama."""
    resultado = []
    for tool in mcp_tools:
        schema = tool.inputSchema if tool.inputSchema else {
            "type": "object",
            "properties": {},
            "required": [],
        }
        resultado.append({
            "type": "function",
            "function": {
                "name": tool.name,
                "description": tool.description or "",
                "parameters": schema,
            },
        })
    return resultado


async def main():
    server_params = StdioServerParameters(
        command=sys.executable,
        args=["mcp_server.py"],
        env=dict(os.environ),
        cwd=str(Path(__file__).parent),
    )

    print("=" * 50)
    print("  ASSISTENTE FINANCEIRO IA")
    print("  Arquitetura: MCP + RAG + LLM Local")
    print("=" * 50)
    print("Inicializando servidor MCP...\n")

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools_result = await session.list_tools()
            ollama_tools = mcp_tools_para_ollama(tools_result.tools)
            nomes = [t["function"]["name"] for t in ollama_tools]
            print(f"[MCP] {len(ollama_tools)} ferramentas carregadas: {nomes}")

            print("\nExemplos de perguntas que você pode fazer:")
            print("  • Qual o saldo de Ricardo?")
            print("  • Quais clientes estão inadimplentes?")
            print("  • Qual o resumo geral da carteira?")
            print("  • Quem está acima de 80% do limite de crédito?")
            print("  • Posso conceder crédito ao cliente Ricardo?")
            print("  • Tem alguma regra de inadimplência?")
            print("  • Qual a política de bloqueio de clientes?")
            print("\nDigite 'sair' para encerrar.\n")

            while True:
                pergunta = input("Pergunta: ").strip()
                if not pergunta:
                    continue
                if pergunta.lower() == "sair":
                    break

                print("\nPensando...", flush=True)

                messages = [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": pergunta},
                ]

                resposta = ollama.chat(
                    model="qwen3:1.7b",
                    messages=messages,
                    tools=ollama_tools,
                )

                msg = resposta["message"]
                tool_calls = msg.get("tool_calls") or []

                if tool_calls:
                    messages.append({
                        "role": "assistant",
                        "content": msg.get("content", ""),
                        "tool_calls": tool_calls,
                    })

                    for tc in tool_calls:
                        nome = tc["function"]["name"]
                        args = tc["function"]["arguments"] or {}

                        print(f"\n[MCP] → Chamando ferramenta: {nome}")

                        resultado = await session.call_tool(nome, args)
                        dados = resultado.content[0].text if resultado.content else "Sem dados retornados."

                        print("\n=== DADOS DOS AGENTES ===")
                        print(dados)

                        print("\nAGUARDANDO RESPOSTA DA IA")

                        messages.append({
                            "role": "tool",
                            "content": dados,
                        })

                    resposta_final = ollama.chat(
                        model="qwen3:1.7b",
                        messages=messages,
                    )
                    conteudo = strip_think(resposta_final["message"]["content"])

                else:
                    conteudo = strip_think(msg.get("content", ""))

                print("\n=== RESPOSTA DA IA ===")
                print(conteudo)
                print()


if __name__ == "__main__":
    asyncio.run(main())
