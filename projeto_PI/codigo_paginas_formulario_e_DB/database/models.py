# Definição das tabelas usando SQLAlchemy

from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from config.settings import engine


Base = declarative_base()

# Definir o modelo de uma tabela chamada 'Administrador'
class Administradores(Base):
    __tablename__ = 'Administrador'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    email = Column(Integer, unique=True, nullable=False)
    senha = Column(String(255), nullable=False)

# Definir o modelo de uma tabela chamada 'Maçç'
class Malls(Base):
    __tablename__ = 'Mall'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    cep = Column(Integer, nullable=False)
    cnpj = Column(Integer, unique=True, nullable=False)
    localizacao = Column(String(255))

# Definir o modelo de uma tabela chamada 'Adm_Mall'
class Adm_Malls(Base):
    __tablename__ = 'Adm_Mall'
    id_adm_mall = Column(Integer, primary_key=True, autoincrement=True)
    id_adm = Column(Integer, ForeignKey('Administrador.id', ondelete='CASCADE'))
    id_mall = Column(Integer, ForeignKey('Mall.id', ondelete='CASCADE'))

# Definir o modelo de uma tabela chamada 'Formulario_Informacoes_Clientes'
class PerguntasInformacoesClientes(Base):
    __tablename__ = 'Formulario_Informacoes_Clientes'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    data_visita = Column(Date(), nullable=False)
    genero = Column(String(100), nullable=False)

# Definir o modelo de uma tabela chamada 'Formulario_Estrutura_Mall'
class PerguntasEstruturaMall(Base):
    __tablename__ = 'Formulario_Estrutura_Mall'

    id = Column(Integer, primary_key=True, autoincrement=True)
    pergunta1_estrutura_mall = Column(String(100), nullable=False)
    pergunta2_estrutura_mall = Column(String(100), nullable=False)
    pergunta3_estrutura_mall = Column(String(100), nullable=False)
    pergunta4_estrutura_mall = Column(String(100), nullable=False)
    pergunta5_estrutura_mall = Column(String(500), nullable=False)

# Definir o modelo de uma tabela chamada 'Formulario_Lojas_Visitadas'
class PerguntasLojasVisitadas(Base):
    __tablename__ = 'Formulario_Lojas_Visitadas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    pergunta1_lojas_visitadas = Column(String(100), nullable=False)
    pergunta2_lojas_visitadas = Column(String(100), nullable=False)
    pergunta3_lojas_visitadas = Column(String(100), nullable=False)
    pergunta4_lojas_visitadas = Column(String(100), nullable=False)
    pergunta5_lojas_visitadas = Column(String(500), nullable=False)

# Criar as tabelas no banco de dados
Base.metadata.create_all(engine)