#Configurações globais (e.x: conexões com o banco de dados)

from dotenv import load_dotenv
import os
load_dotenv()

username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
database = os.getenv('DB_NAME')

# Criar a engine de conexão com SQLAlchemy
DATABASE_URL = (f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')
