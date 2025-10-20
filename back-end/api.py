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

@app.get("/produtos")
def listar_produtos():
    produtos = funcao.listar_produtos()
    lista = []
    for linha in produtos:
        lista.append({
            "id_produto": linha[0],
            "nome": linha[1],
            "categoria": linha[2],
            "preco": linha[3],
            "quantidade": linha[4]
            })
    return {"produtos": lista}

@app.put("/estoque/{id_produto}")
def atualizar_produto(id_produto: int, nova_quantidade: float):
    produto = funcao.atualizar_produto(id_produto, nova_quantidade)
    if produto:
        return {"mensagem": f"produto atualizado com sucesso"}
    else:
        return {"mensagem": f"Produto não encontrado!"}

@app.delete("/produto")
def deletar_produto(id_produto):
    produto = funcao.deletar_porduto(id_produto)
    if produto:
        return {"mensagem": f"Produto removido com sucesso"}
    else:
        return {"mensagem": f"Não foi possivel remover esse produto!"}