import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Gerenciador de Produtos e Estoque")
st.title(" Gerenciador de Produtos e Estoque")

menu = st.sidebar.radio("Navegação", ["Catalogo", "Adicionar produto", "Atualizar produto"])

