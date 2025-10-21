📦 Gerenciador de Produtos e Estoque










🧾 Sobre o Projeto

O Gerenciador de Produtos e Estoque é uma aplicação web que facilita o controle de produtos e a gestão de estoque.
O sistema une FastAPI (backend), Streamlit (frontend) e PostgreSQL (banco de dados) em uma arquitetura simples e eficiente.

Seu objetivo é oferecer um painel intuitivo para cadastrar, atualizar, consultar e excluir produtos, tudo de forma centralizada e segura.

🚀 Funcionalidades

✅ Listar todos os produtos do estoque

➕ Adicionar novos produtos com nome, descrição e quantidade

✏️ Atualizar informações e quantidades

🗑️ Remover produtos do sistema

📊 Consultar estatísticas básicas (em futuras atualizações)

🧠 Estrutura e Funcionamento

O projeto é dividido em camadas bem definidas para facilitar a manutenção:

📦 gerenciador-estoque
├── api.py           # Backend (FastAPI) → Endpoints para operações CRUD
├── app.py           # Frontend (Streamlit) → Interface web interativa
├── funcao.py        # Funções auxiliares → CRUD no banco PostgreSQL
├── conexao.py       # Configuração da conexão com o banco
├── .env             # Variáveis de ambiente (dados sensíveis)
├── .gitignore       # Arquivos ignorados no GitHub
└── README.md        # Documentação do projeto


api.py → Cria a API REST que o Streamlit consome.
Possui rotas como /produtos, /adicionar, /atualizar e /deletar.

app.py → Exibe uma interface simples e bonita no navegador.
Permite interagir com a API de forma visual.

funcao.py → Contém as funções SQL responsáveis por inserir, atualizar e deletar dados no banco.

conexao.py → Centraliza a conexão PostgreSQL, lendo os dados do .env.

🛠️ Tecnologias Utilizadas

FastAPI
 → Criação da API backend moderna e performática

Streamlit
 → Interface visual para o usuário

PostgreSQL
 → Banco de dados relacional

psycopg2
 → Conector entre Python e PostgreSQL

python-dotenv
 → Carrega variáveis do .env com segurança

⚙️ Como Configurar o Projeto
1️⃣ Clonar o repositório
git clone https://github.com/Igor0liveir4/Controle-de-estoque.git
cd gerenciador-estoque

2️⃣ Criar ambiente virtual
python -m venv venv

3️⃣ Ativar o ambiente virtual
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate

4️⃣ Instalar dependências
pip install -r requirements.txt

5️⃣ Criar o arquivo .env
DB_HOST=localhost
DB_NAME=estoque
DB_USER=postgres
DB_PASSWORD=sua_senha
DB_PORT=5432


⚠️ O .env armazena informações sensíveis (como senha e nome do banco).
Nunca suba este arquivo para o GitHub.

6️⃣ Executar o backend (API FastAPI)
uvicorn api:app --reload


A API ficará disponível em:
👉 http://127.0.0.1:8000/docs

7️⃣ Rodar o frontend (Streamlit)
streamlit run app.py


A interface abrirá automaticamente no navegador.

🔐 Segurança

Mantenha o arquivo .env fora do repositório.
Use o seguinte conteúdo no seu .gitignore:

.env
__pycache__/
venv/


Essas regras impedem que informações sensíveis e arquivos temporários sejam enviados ao GitHub.

✅ Status do Projeto

🧩 Em desenvolvimento

O projeto já é funcional, mas futuras melhorias estão planejadas:

🔒 Sistema de login e autenticação

🧮 Relatórios e gráficos de vendas e estoque

🧠 Melhor validação dos dados

📈 Dashboard com indicadores

💡 Explicações Técnicas (Resumidas)
# FastAPI → Backend
Gerencia requisições HTTP e responde com dados do PostgreSQL.

# Streamlit → Frontend
Exibe os produtos e permite que o usuário interaja com os dados via interface web.

# PostgreSQL → Banco de Dados
Armazena todos os produtos e suas quantidades em tabelas relacionais.

# psycopg2 → Conexão
Permite que o Python execute comandos SQL de forma segura e rápida.

# dotenv → Segurança
Lê variáveis do arquivo .env (como usuário e senha do banco) sem expor no código público.

🤝 Contribuição

Contribuições são muito bem-vindas!
Sinta-se à vontade para abrir uma issue com sugestões ou enviar um pull request com melhorias.

👨‍💻 Autor

Igor Oliveira Gonçalves
📧 GitHub