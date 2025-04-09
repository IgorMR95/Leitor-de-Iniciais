# Home.py

import streamlit as st

# Título da página
st.set_page_config(page_title="Leitor de Iniciais", layout="centered")

# Cabeçalho
st.title("📄 Leitor de Iniciais")
st.subheader("Um projeto simples para leitura e resumo de petições iniciais.")

# Mensagem de boas-vindas
st.markdown("""
Bem-vindo ao **Leitor de Iniciais**!  
Aqui você pode fazer upload de documentos jurídicos e obter um resumo automático usando inteligência artificial.

Para começar, faça o upload de um arquivo PDF no menu à esquerda ou clique no botão abaixo.
""")


# Rodapé
st.markdown("---")
