# Configuração e inicialização da conexão com o banco
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
load_dotenv()

DATABASE_URL = os.getenv("MYSQL_PUBLIC_URL")

# Configurar o engine de conexão com o banco de dados
engine = create_engine(DATABASE_URL)

# Configurar a sessão para interagir com o banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Função para obter a sessão
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
