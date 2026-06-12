

# Análise de Risco Financeiro com Arquitetura Multiagente e Modelos Locais

## Integrantes da Equipe

* Matheus Soares Oliveira da Silva (191045)
* Vitória ... ()



# 1. Descrição do Problema

Empresas precisam analisar constantemente sua carteira de clientes para identificar inadimplência, riscos financeiros, necessidade de cobrança, concessão de crédito e oportunidades de renegociação.

Realizar essas análises manualmente demanda tempo e aumenta a possibilidade de erros.

Este projeto propõe uma solução baseada em Inteligência Artificial Multiagente para auxiliar a análise financeira e a tomada de decisão.



# 2. Objetivo da Solução

Desenvolver uma aplicação baseada em múltiplos agentes inteligentes capazes de cooperar para analisar informações financeiras, consultar documentos corporativos e responder perguntas em linguagem natural.

A solução utiliza modelos locais de linguagem executados via Ollama, além de uma arquitetura RAG para consulta de documentos financeiros.



# 3. Arquitetura da Solução

A arquitetura é composta por um coordenador central responsável por encaminhar as solicitações do usuário para agentes especializados.

Fluxo simplificado:

Usuário
↓
Coordenador
↓
Agentes Especializados
↓
Dados Excel / Base Vetorial
↓
LLM (Qwen)
↓
Resposta



# 4. Agentes do Sistema

## 4.1 Coordenador

Responsável por identificar o tipo de pergunta realizada pelo usuário e encaminhá-la ao agente mais adequado.

Funções:

* Receber perguntas.
* Realizar roteamento.
* Consolidar o fluxo de execução.



## 4.2 Agente Financeiro

Responsável por consultas financeiras gerais.

Exemplos:

* Consultar saldo de clientes.
* Consultar informações financeiras.



## 4.3 Agente de Cobrança

Responsável por identificar clientes com atrasos e inadimplência.

Exemplos:

* Clientes em atraso.
* Clientes inadimplentes.
* Necessidade de cobrança.



## 4.4 Agente de Crédito

Responsável pela análise de utilização de limite de crédito.

Exemplos:

* Clientes próximos do limite.
* Clientes acima do limite.



## 4.5 Agente de Risco

Responsável pela classificação e análise de risco financeiro.

Exemplos:

* Baixo risco.
* Médio risco.
* Alto risco.



## 4.6 Agente Analista de Carteira

Responsável por fornecer visão consolidada da carteira financeira.

Exemplos:

* Situação geral da carteira.
* Resumo executivo.
* Saúde financeira da carteira.



## 4.7 Agente de Regras (RAG)

Responsável pela consulta de documentos corporativos.

Utiliza:

* PDF de políticas financeiras.
* Embeddings.
* Banco vetorial ChromaDB.

Exemplos:

* Regras de crédito.
* Regras de renegociação.
* Políticas financeiras.
* Procedimentos corporativos.



# 5. Ferramentas (Tools)

Os agentes utilizam diferentes ferramentas para executar suas tarefas.

## Consulta Excel

Responsável por recuperar informações financeiras dos clientes.

## Consulta PDF

Responsável pela leitura da documentação corporativa.

## Busca Vetorial

Responsável pela recuperação semântica de informações relevantes.

## Geração de Embeddings

Responsável pela indexação do conteúdo documental.

## LLM Local

Responsável pela interpretação dos dados e geração das respostas.



# 6. MCP (Model Context Protocol)

A arquitetura foi organizada utilizando uma camada de coordenação responsável por padronizar o acesso dos agentes às ferramentas disponíveis.

O coordenador atua como intermediador entre os agentes e os recursos utilizados pelo sistema, garantindo a separação de responsabilidades e a comunicação estruturada entre os componentes da aplicação.

Essa abordagem permite que diferentes agentes utilizem recursos especializados de forma organizada e controlada.



# 7. Estratégia de RAG

O sistema implementa Retrieval-Augmented Generation (RAG) para consulta de documentos financeiros.

Fluxo:

1. O documento PDF é carregado.
2. O conteúdo é dividido em trechos.
3. São gerados embeddings para cada trecho.
4. Os embeddings são armazenados no banco vetorial ChromaDB.
5. Quando o usuário faz uma pergunta, um embedding da pergunta é gerado.
6. O ChromaDB recupera os trechos mais relevantes.
7. Os trechos recuperados são enviados ao modelo Qwen.
8. O modelo gera a resposta utilizando o contexto recuperado.



# 8. Base de Conhecimento

A base de conhecimento utilizada é composta por:

## Dados Estruturados

Arquivo Excel contendo:

* Clientes
* Saldos
* Limites de crédito
* Informações financeiras

## Dados Não Estruturados

Documento PDF:

Politica_Financeira_Empresa.pdf

Contendo:

* Políticas de crédito
* Regras de cobrança
* Regras de renegociação
* Critérios de risco



# 9. Embeddings e Banco Vetorial

## Embeddings

Biblioteca utilizada:

sentence-transformers

Modelo utilizado:

all-MiniLM-L6-v2

Função:

Converter textos em vetores numéricos para busca semântica.



## Banco Vetorial

Tecnologia utilizada:

ChromaDB

Funções:

* Armazenamento de embeddings.
* Busca semântica.
* Recuperação de contexto para RAG.



# 10. Modelo Local Utilizado

Modelo:

Qwen 3 1.7B

Execução:

Ollama Local

Motivação da escolha:

* Baixo consumo de recursos.
* Boa qualidade para tarefas de análise textual.
* Facilidade de execução local sem dependência de APIs pagas.



# 11. Tecnologias Utilizadas

* Python
* Ollama
* Qwen 3 1.7B
* ChromaDB
* Sentence Transformers
* PyPDF
* Pandas
* OpenPyXL



# 12. Dependências

Instalação:

pip install ollama
pip install pandas
pip install openpyxl
pip install pypdf
pip install chromadb
pip install sentence-transformers



# 13. Estrutura do Projeto

MultiAgente/

├── chat.py

├── indexar_documento.py

├── Politica_Financeira_Empresa.pdf

├── dados_financeiros.xlsx

├── chroma_db/

└── agentes/

├── coordenador.py

├── agente_financeiro.py

├── cobranca.py

├── credito.py

├── risco.py

├── analista_ia.py

└── agente_regras.py



# 14. Como Executar

## Passo 1

Iniciar o Ollama.

## Passo 2

Verificar se o modelo está instalado.

ollama list



## Passo 3

Indexar o documento PDF.

python indexar_documento.py



## Passo 4

Executar o sistema.

python chat.py



# 15. Exemplos de Uso

Pergunta:

Quem está inadimplente?

Pergunta:

Quem possui maior saldo devedor?

Pergunta:

Qual a situação geral da carteira?

Pergunta:

Consultar documento: quando oferecer renegociação?

Pergunta:

Qual a política para clientes de alto risco?

Pergunta:

Quando o crédito deve ser bloqueado?



# 16. Conclusão

O projeto demonstrou a construção de uma solução baseada em Inteligência Artificial Multiagente utilizando modelos locais, recuperação de conhecimento por RAG, embeddings, banco vetorial e ferramentas especializadas para análise financeira.

A arquitetura proposta permitiu separar responsabilidades entre agentes especializados, melhorando a organização da solução e facilitando a tomada de decisão baseada em dados financeiros e documentos corporativos.
