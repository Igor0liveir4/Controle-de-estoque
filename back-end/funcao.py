from conexao import conectar

def criar_tabela():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS produtos(
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            categoria VARCHAR(50),
            preco NUMERIC (10,2),
            quantidade INT                   
            )
            """)
            conexao.commit()
        except Exception as erro:
            print(f'Erro ao criar a tabela {erro}')
        finally:
            cursor.close()
            conexao.close()

def cadastrar_produtos(nome, categoria, preco, quantidade):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "INSERT INTO produtos (nome, categoria, preco, quantidade)",
                (nome, categoria, preco, quantidade)
            )
            conexao.commit()
        except Exception as erro:
            print(f'Erro ao cadastrar produto {erro}')
        finally:
            cursor.close()
            conexao.close()

def listar_produtos():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("SELECT * FROM produtos ORDER BY id")
            return cursor.fetchall()
        except Exception as erro:
             print(f'Erro ao tentar visualizar o estoque {erro}')
        finally:
            cursor.close()
            conexao.close()