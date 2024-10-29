from models import PerguntasInformacoesClientes,PerguntasLojasVisitadas,PerguntasEstruturaMall
from sqlalchemy.orm import sessionmaker
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
load_dotenv()

DATABASE_URL = os.getenv("MYSQL_PUBLIC_URL")
engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()

def consultar_informacoes_clientes():
    # Consultar os dados
    query = session.query(PerguntasInformacoesClientes)  #Colsultando a tabela PerguntasInformacoesClientes
    dados_clientes = query.all()

    # Converter os resultados em um DataFrame
    df_informacoes_clientes = pd.DataFrame([dados.__dict__ for dados in dados_clientes])

    # Remover a coluna _sa_instance_state que é adicionada automaticamente
    df_informacoes_clientes.drop('_sa_instance_state', axis=1, inplace=True)

    print(df_informacoes_clientes)
    session.close()
    return df_informacoes_clientes

def consultar_perguntas_lojas_visitadas():

    query = session.query(PerguntasLojasVisitadas)  #Consultando a tabela PerguntasLojasVisitadas
    dados_clientes = query.all()

    df_lojas_visitadas = pd.DataFrame([dados.__dict__ for dados in dados_clientes])
    df_lojas_visitadas.drop('_sa_instance_state', axis=1, inplace=True)

    print(df_lojas_visitadas)
    session.close()
    return df_lojas_visitadas


def consultar_perguntas_estrutura_mall():

    query = session.query(PerguntasEstruturaMall)  #Consultando a tabela PerguntasEstruturaMall
    dados_clientes = query.all()

    df_perguntas_estrutura_mall = pd.DataFrame([dados.__dict__ for dados in dados_clientes])
    df_perguntas_estrutura_mall.drop('_sa_instance_state', axis=1, inplace=True)

    print(df_perguntas_estrutura_mall)
    session.close()
    return df_perguntas_estrutura_mall






