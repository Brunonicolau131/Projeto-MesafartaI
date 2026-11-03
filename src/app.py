"""MESAFARTAI - AC4 Parte 1: interface Streamlit."""
from pathlib import Path
import sqlite3
import pandas as pd
import streamlit as st
from nlu import MotorNLU
from entities import ExtratorEntidades
from matchmaking import MotorMatchmaking

DB_PATH = Path(__file__).resolve().parent.parent / 'mesafartai.db'
st.set_page_config(page_title='MESAFARTAI - Combate à Fome', page_icon='🥫', layout='wide')

@st.cache_resource
def carregar_motores():
    return MotorNLU(limiar_threshold=0.60), ExtratorEntidades(), MotorMatchmaking(db_path=str(DB_PATH))

nlu, extrator, matchmaker = carregar_motores()
st.title('🥫 MESAFARTAI — Inteligência contra a Fome')
st.caption('Conectando doadores e ONGs com inteligência artificial | ODS 2')
aba_chat, aba_dashboard = st.tabs(['💬 Chatbot de Doações', '📊 Dashboard de Impacto Social'])

with aba_chat:
    st.subheader('Converse com o assistente de doações')
    st.caption('Demonstração acadêmica: as coordenadas do doador são ilustrativas e as doações não são persistidas.')
    if 'mensagens' not in st.session_state:
        st.session_state.mensagens = [{'role': 'assistant', 'content': 'Olá! Sou o assistente do MESAFARTAI. Você quer doar alimentos ou solicitar doações para uma ONG?'}]
    for mensagem in st.session_state.mensagens:
        with st.chat_message(mensagem['role']):
            st.markdown(mensagem['content'])
    if prompt := st.chat_input('Ex.: Tenho 20 kg de arroz para doar hoje'):
        st.session_state.mensagens.append({'role': 'user', 'content': prompt})
        with st.chat_message('user'):
            st.markdown(prompt)
        resultado = nlu.processar_mensagem(prompt)
        intencao = resultado['intencao']
        if intencao == 'cadastrar_doacao':
            entidades = extrator.processar_texto(prompt)
            match = matchmaker.encontrar_ong_mais_proxima(-23.615, -46.785)
            resposta = (f"**Doação identificada (simulação)**\n\n"
                        f"- **Alimento:** {entidades['alimento']}\n"
                        f"- **Quantidade extraída:** {entidades['quantidade_kg']} (verifique a unidade informada)\n"
                        f"- **Validade estimada pelo módulo:** {entidades['data_validade']}\n\n")
            if match:
                resposta += (f"**ONG sugerida pelo KNN:** {match['ong_nome']} "
                             f"(distância aproximada calculada: {match['distancia_estimada']} km).")
            else:
                resposta += 'Nenhuma ONG disponível no banco de dados.'
            resposta += '\n\n_Nenhuma doação foi gravada no banco de dados._'
        elif intencao == 'solicitar_alimentos':
            resposta = 'Entendi que você deseja solicitar alimentos. O cadastro de solicitações ainda não está implementado nesta etapa.'
        elif intencao == 'consultar_status':
            resposta = 'Entendi sua consulta. O acompanhamento de status ainda não está implementado nesta etapa.'
        else:
            resposta = resultado['resposta']
        st.session_state.mensagens.append({'role': 'assistant', 'content': resposta})
        with st.chat_message('assistant'):
            st.markdown(resposta)

with aba_dashboard:
    st.subheader('Indicadores Logísticos e Sociais')
    with sqlite3.connect(str(DB_PATH)) as conn:
        df_ongs = pd.read_sql_query("SELECT id, nome, latitude, longitude FROM usuarios WHERE tipo = 'ONG'", conn)
    col1, col2, col3 = st.columns(3)
    col1.metric('ONGs cadastradas', len(df_ongs))
    col2.metric('Doações registradas', 'Não disponível')
    col3.metric('Refeições proporcionadas', 'Não disponível')
    st.caption('Os indicadores de doações e refeições dependem de registros reais, ainda não implementados.')
    st.divider()
    st.subheader('Unidades de atendimento cadastradas')
    st.dataframe(df_ongs, use_container_width=True, hide_index=True)
    if not df_ongs.empty:
        st.map(df_ongs[['latitude', 'longitude']])
