from fastapi import FastAPI
import funcao 

#python -m uvicorn api:app --reload
app = FastAPI(title="Controle de Produtos e Estoque")

@app.get("/")
def home():
    return {"mensagem": "bem-Vindo ao Controle de produtos e Estoque"}

@app.post("/estoque")
def criar_produtos(nome: str, categoria: str, preco: float, quantidade: int):
    funcao.cadastrar_produtos(nome, categoria, preco, quantidade)
    return {"mensagem": "Produto adicionado com sucesso!"}

app.get("/estoque")
def listar_produtos():
    produtos = funcao.listar_produtos()
    lista = []
    for linha in produtos:
        lista.append({
            "nome": linha[0],
            "categoria": linha[1],
            "preco": linha[2],
            "quantidade": linha[3]
            })
    return {"produtos": lista}

app.put("/estoque/{id_produto}")
def atualizar_produto(id_produto: int, nova_quantidade: float):
    produto = funcao.atualizar_produto(id_produto, nova_quantidade)
    if produto:
        return {"mensagem": f"prduto atualizado com sucesso"}
    else:
        return {"mensagem": f"Produto não encontrado!"}