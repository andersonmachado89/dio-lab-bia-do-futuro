# Passo a passo:
# 1 - Título
# 2 - Input do chat
# 3 - A cada mensagem enviada:
    # Mostrar a mensagem do usuario enviou no chat
    # Enviar essa mensagem para a IA responder
    # Aparece na tela a resposta da IA
# Streamlit - Frontend e Backend

import streamlit as st
from openai import OpenAI     
import os
from dotenv import load_dotenv
import pandas as pd
import json

#Função para carregar os arquivos csv
def carregar_csv(caminho):
    df = pd.read_csv(caminho)
    return df.to_string(index=False)

#Função para carregar os aquivos json
def carregar_json(caminho_json):
    with open(caminho_json, "r", encoding="utf-8") as f:
        dados = json.load(f)

    return json.dumps(dados, ensure_ascii=False, indent=2)

#Criação da base de conhecimento a partir dos aquivos carregados
base_conhecimento = ""

base_conhecimento += carregar_csv('/home/anderson/Documentos/python/dio-lab-bia-do-futuro/data/transacoes.csv')
base_conhecimento += "\n\n"
base_conhecimento += carregar_csv('/home/anderson/Documentos/python/dio-lab-bia-do-futuro/data/historico_atendimento.csv')
base_conhecimento += "\n\n"
base_conhecimento += carregar_json('/home/anderson/Documentos/python/dio-lab-bia-do-futuro/data/produtos_financeiros.json')
base_conhecimento += "\n\n"
base_conhecimento += carregar_json('/home/anderson/Documentos/python/dio-lab-bia-do-futuro/data/perfil_investidor.json')

#Prompt de restrição do agente
prompt_sistema = f"""
Você é Duda, uma assistente virtual.

REGRAS IMPORTANTES:

1. Responda SOMENTE utilizando informações da base de conhecimento abaixo.
2. Nunca invente informações.
3. Nunca utilize conhecimento próprio.
4. Nunca peça e nem forneça dados sensíveis, como: senha, cpf.
5. Se a resposta não estiver na base, responda exatamente:

"Desculpe, não encontrei essa informação em minha base de conhecimento."

BASE DE CONHECIMENTO:

{base_conhecimento}
"""
print(base_conhecimento)
# Oculte a barra de código
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    #fileMenu {visibility: hidden;}
    #sidebarContainer {visibility: hidden;}
    .sidebar {visibility: hidden;}
    .viewerBadge_link__1S137 {display: none;}
    </style>
""", unsafe_allow_html=True)

load_dotenv()
API_KEY = os.getenv("OPENAI_KEY")  

modelo = OpenAI(api_key=API_KEY)

st.subheader("Bem vindo(a) à Duda, sua consultora financeira!")

if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = [
        {
            "role": "assistant",
            "content": "Olá! 😊 Eu sou a Duda, sua assistente virtual. Como posso ajudar você hoje?"
        }
    ]

#Exibir o histórico de mensagens
for msg in st.session_state["lista_mensagens"]:
    chave = msg["role"]
    texto = msg["content"] 
    st.chat_message(chave).write(texto)

mensagem_usuario = st.chat_input("Escreva sua mensagem aqui")

if mensagem_usuario:
    # user -> Ser humano
    # assistant -> Inteligência Artificial
    st.chat_message("user").write(mensagem_usuario)
    mensagem = {"role":"user", "content":mensagem_usuario}
    st.session_state["lista_mensagens"].append(mensagem)
    
    #Resposta da IA
    mensagens = [
        {
            "role": "system",
            "content": prompt_sistema
        }
    ]

    mensagens.extend(st.session_state["lista_mensagens"])

    resposta_modelo = modelo.chat.completions.create(
        model="gpt-4o",
        messages=mensagens,
        temperature=0
    )
    
    resposta_ia = resposta_modelo.choices[0].message.content
    
    #Exibir a IA na tela
    st.chat_message("assistant").write(resposta_ia)    
    mensagem_ia = {"role":"assistant", "content":resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)
    