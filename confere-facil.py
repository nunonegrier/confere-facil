import os
import google.generativeai as genai
from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools import google_search
from google.genai import types
from datetime import date
import warnings
import re

warnings.filterwarnings("ignore")

api_key = os.environ.get("GOOGLE_API_KEY")

genai.configure(api_key=api_key)

# Função auxiliar que envia uma mensagem para um agente via Runner e retorna a resposta final
def call_agent(agent: Agent, message_text: str) -> str:
    # Cria um serviço de sessão em memória
    session_service = InMemorySessionService()
    # Cria uma nova sessão (você pode personalizar os IDs conforme necessário)
    session = session_service.create_session(app_name=agent.name, user_id="user1", session_id="session1")
    # Cria um Runner para o agente
    runner = Runner(agent=agent, app_name=agent.name, session_service=session_service)
    # Cria o conteúdo da mensagem de entrada
    content = types.Content(role="user", parts=[types.Part(text=message_text)])

    final_response = ""
    # Itera assincronamente pelos eventos retornados durante a execução do agente
    for event in runner.run(user_id="user1", session_id="session1", new_message=content):
        if event.is_final_response():
          for part in event.content.parts:
            if part.text is not None:
              final_response += part.text
              final_response += "\n"
    return final_response


############################################
# --- Agente 1: Pesquisador de fraudes --- #
############################################
def agente_buscador(descricao_ocorrencia):
  buscador = Agent(
      name="agente_buscador",
      model="gemini-2.0-flash",
      description="Agente que busca informações sobre a ocorrência",
      tools=[google_search],
      instruction="""
      Você é um pesquisador de segurança digital.
      Possui vastos conhecimentos nos mais diversos tipos de fraudes digitais sendo feitas atualmente.
      A sua tarefa é a de analisar a descrição da ocorrência abaixo, e, para complementar a análise, deve também utilizar
      a ferramenta de busca do google (google_search) para ter acesso às informações mais recentes sobre o tema.
      A análise deve calcular a probabilidade de ser uma tentativa de fraude em curso assim como identificar o possível tipo de fraude.
      De preferência, deverá fazer uma identificação única e acertiva do tipo de fraude em andamento, mas, não sendo possível, deverá listar
      uma segunda possível identificação do tipo de fraude.
      Faça apenas a análise sem apresentar recomendações.
      Dê uma resposta suscinta, mas que não deixe nenhuma informação importante de fora.
      """
  )

  entrada_do_agente_de_pesquisa_inicial = f"Ocorrência: {descricao_ocorrencia}"

  # Executa o agente
  pesquisa_inicial = call_agent(buscador, entrada_do_agente_de_pesquisa_inicial)
  return pesquisa_inicial


################################################
#     --- Agente 2: Analista de fraudes ---    #
################################################
def agente_analista(descricao_ocorrencia, pesquisa_ocorrencia, respostas_usuario=None):
    analista = Agent(
        name="agente_analista",
        model="gemini-2.0-flash",
        instruction="""
        Você é um especialista em análise de fraudes.
        Com base na pesquisa inicial sobre a descrição da fraude:
        Crie entre 1 a 3 perguntas a serem feitas ao usuário e baseadas na pesquisa inicial, que auxiliem na análise da pesquisa inicial
        e retorne APENAS as perguntas numeradas.
        Se respostas do usuário forem fornecidas, utilize a pesquisa inicial e as respostas fornecidas para refinar a análise inicial,
        NÃO faça novas perguntas, use a ferramenta de busca do google (google_search) para buscar informações mais recentes se forem necessárias
        e apresente a análise final suscinta, mas que não deixe nenhuma informação importante de fora.
        """,
        description="Agente que analisa fraudes",
        tools=[google_search]
    )

    entrada_do_agente_analista = f"Descrição:{descricao_ocorrencia}\nPesquisa: {pesquisa_ocorrencia}"
    if respostas_usuario:
        entrada_do_agente_analista += f"\nRespostas do usuário: {respostas_usuario}"

    # Executa o agente
    analise_da_fraude = call_agent(analista, entrada_do_agente_analista)
    return analise_da_fraude


####################################################
# --- Agente 3: Especialista em Cibersegurança --- #
####################################################
def agente_especialista(descricao_ocorrencia, analise_da_fraude):
    especialista = Agent(
        name="agente_especialista",
        model="gemini-2.0-flash",
        instruction="""
            Você é um especialista em cibersegurança.
            Com base na análise da fraude você deve:
            Fornecer instruções claras para que o usuário evite a fraude.
            Fornecer os contados dos canais de atendimento da empresa ou serviço, públicos ou privados, ou qualquer
            outro tipo de negócio que tenham sido mencionados na descrição da ocorrência para que o usuário possa entrar
            em contato para esclarecer a situação.
            Terminar listando exatamanete e de forma clara e estruturada com as indicações do que o usuário não deve fazer no presente caso.
            """,
        description="Agente especialista em ciberseguranca",
        tools=[google_search]
    )
    entrada_do_agente_especialista = f"Descrição: {descricao_ocorrencia}\nAnálise: {analise_da_fraude}"

    # Executa o agente
    recomendacoes_finais = call_agent(especialista, entrada_do_agente_especialista)
    return recomendacoes_finais


print("🚀 Iniciando o Sistema de Análise e Prevenção de Fraudes 🚀")

# --- Obter a Descrição do Usuário ---
print("❓ Por favor, faça uma descrição da possível fraude:")
descricao_ocorrencia = input("")


if not descricao_ocorrencia:
  print("você esqueceu de digitar a descrição!")
else:
  print(f"Obrigado! Vamos analisar a ocorrência como foi descrita: {descricao_ocorrencia}")

  # 1o Agente
  pesquisa_ocorrencia = agente_buscador(descricao_ocorrencia)
  print("\n--- Resultado do Agente 1 (Buscador) ---\n")
  print(pesquisa_ocorrencia)
#   display(to_markdown(pesquisa_ocorrencia))
  print("-------------------------------------------------------------------")

  # 2o Agente
  # Primeira chamada do agente analista para obter as perguntas
  perguntas_texto = agente_analista(descricao_ocorrencia, pesquisa_ocorrencia)
  print("\n--- Perguntas do Agente 2 (Analista) ---\n")
  print(perguntas_texto)
#   display(to_markdown(perguntas_texto))
  print("-------------------------------------------------------------------")

  # Extrair as perguntas numeradas do texto
  perguntas_lista = re.findall(r'\d+\.\s+(.*)', perguntas_texto)

  respostas_usuario = {} # Dicionário para armazenar as respostas {numero_pergunta: resposta}

  if perguntas_lista:
      print("\n❓ Por favor, responda às perguntas acima para ajudar na análise:")
      for i, pergunta in enumerate(perguntas_lista):
          print(f"Resposta para a pergunta {i + 1}:")
          print(f"'{pergunta.strip()}'")
          resposta = input("")
          respostas_usuario[f"Pergunta {i + 1}"] = resposta # Armazena a resposta associada ao número da pergunta
  else:
      print("Nenhuma pergunta foi gerada pelo agente analista.")

  # Preparar as respostas para enviar ao agente na segunda chamada
  respostas_formatadas = "\n".join([f"{chave}: {valor}" for chave, valor in respostas_usuario.items()])

  # Segunda chamada do agente analista com as respostas do usuário
  analise_da_fraude = agente_analista(descricao_ocorrencia, pesquisa_ocorrencia, respostas_usuario=respostas_usuario)
  print("\n--- Análise final do Agente 2 (Analista) ---\n")
  print(analise_da_fraude)
#   display(to_markdown(analise_da_fraude))
  print("-------------------------------------------------------------------")

  # 3o Agente
  recomendacoes_finais = agente_especialista(descricao_ocorrencia, analise_da_fraude)
  print("\n--- Resultado do Agente 3 (Especialista) ---\n")
  print(recomendacoes_finais)
#   display(to_markdown(recomendacoes_finais))
  print("-------------------------------------------------------------------")