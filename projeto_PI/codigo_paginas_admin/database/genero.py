import streamlit as st
import pandas as pd
import plotly.express as px
from queries import consultar_informacoes_clientes

def grafico_de_torta_genero():
    data = consultar_informacoes_clientes()
    df = pd.DataFrame(data)

    # Criação do gráfico de torta usando Plotly Express
    fig = px.pie(df, names='genero', title='Proporção de Gênero')

    # Exibir o gráfico diretamente no Streamlit com o componente nativo
    st.plotly_chart(fig)



