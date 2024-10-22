# Testes para validação de formulários


# CREATE DATABASE testedb 


import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()

# Obter a URL do banco de dados a partir do .env
DATABASE_URL = os.getenv("DATABASE_URL")

# Criar o engine de conexão
engine = create_engine(DATABASE_URL, echo=True)

# Testar a conexão
try:
    with engine.connect() as connection:
        result = connection.execute("SELECT DATABASE();")
        for row in result:
            print(f"Banco de dados conectado: {row[0]}")
except Exception as e:
    print(f"Erro ao conectar no banco de dados: {e}")
