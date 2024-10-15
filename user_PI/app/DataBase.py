from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "mysql+pymysql://root:@localhost:3306/testedb"

# Criar engine de conexão com o MySQL
engine = create_engine(DATABASE_URL)

# Criar a classe base para os modelos ORM
Base = declarative_base()

# Definir o modelo de uma tabela chamada 'usuarios'
class Administradores(Base):
    __tablename__ = 'Administrador'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    email = Column(Integer, unique=True, nullable=False)
    senha = Column(String(255), nullable=False)

class Malls(Base):
    __tablename__ = 'Mall'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    cep = Column(Integer, nullable=False)
    cnpj = Column(Integer, unique=True, nullable=False)
    localizacao = Column(String(255))

class Adm_Malls(Base):
    __tablename__ = 'Adm_Mall'
    id_adm_mall = Column(Integer, primary_key=True, autoincrement=True)
    id_adm = Column(Integer, ForeignKey('Administrador.id', ondelete='CASCADE'))
    id_mall = Column(Integer, ForeignKey('Mall.id', ondelete='CASCADE'))


# Criar as tabelas no banco de dados
Base.metadata.create_all(engine)

