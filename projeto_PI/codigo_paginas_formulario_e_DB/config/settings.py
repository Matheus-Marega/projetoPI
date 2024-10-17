#Configurações globais (e.x: conexões com o banco de dados)

from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL") #Variavel de ambiente para o banco de Dados

