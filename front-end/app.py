import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Gerenciador de Produtos e Estoque")
st.title(" Gerenciador de Produtos e Estoque")

menu = st.sidebar.radio("Navegação", ["Catalogo", "Adicionar produto", "Atualizar produto"])

if menu == "Catalogo":
    st.subheader("Todos os produtos disponiveis")
    response = requests.get(f"{API_URL}/estoque")
    if response.status_code == 200:
        produto = response.json().get("produto", [])
        if produto:
            st.dataframe(produto)
    else:
        st.error("Erro ao tentar acessar a API")