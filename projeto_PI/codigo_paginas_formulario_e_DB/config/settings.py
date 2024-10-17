#Configurações globais (e.x: conexões com o banco de dados)

from dotenv import load_dotenv
import os
from database.db_setup import SessionLocal

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL") #Variavel de ambiente para o banco de Dados

# Função para obter a sessão
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()