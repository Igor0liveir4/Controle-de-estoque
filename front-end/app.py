import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Gerenciador de Produtos e Estoque")
st.title(" Gerenciador de Produtos e Estoque")

menu = st.sidebar.radio("Navegação", ["Catalogo", "Adicionar produto", "Atualizar produto"])

if menu == "Catalogo":
    st.subheader("Todos os produtos disponiveis")
    response = requests.get(f"{API_URL}/produtos")
    if response.status_code == 200:
        produtos = response.json().get("produtos", [])
        if produtos:
            st.dataframe(produtos)
        else:
            st.info('Nenhum produto encontrado no catálogo.')
    else:
        st.error("Erro ao tentar acessar a API")

elif menu == "Adicionar produto":
    st.subheader("➕ Adicionar produto")
    nome = st.text_input("nome do produto")
    categoria = st.text_input("cagoria do produto")
    preco = st.number_input("preco do produto", min_value=0.0, step=1)
    quantidade = st.number_input("Quantidade do produto", min_value=0, step=1)
    if st.button("Salvar Produto"):
        dados = {
            "nome": nome,
            "categoria": categoria,
            "preco": preco,
            "quantidade": quantidade
        }
        response = requests.post(f"{API_URL}/estoque", params=dados)
        if response.status_code == 200:
            st.success("Produto adicionado com sucesso!")
        else:
            st.error("Erro ao adicionar o produto")

