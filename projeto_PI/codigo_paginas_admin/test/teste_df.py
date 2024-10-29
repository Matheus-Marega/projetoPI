import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt



def get_chart():
    import plotly.express as px

    df = px.data.tips()
    fig = px.pie(df, values='tip', names='sex', color_discrete_sequence=px.colors.sequential.RdBu)
    fig.update_layout(template="seaborn")

    st.plotly_chart(fig)
    

def get_chart_2():
    import plotly.express as px

    df = px.data.tips()
    fig = px.bar(df, x="sex", y="total_bill", color='time')
    st.plotly_chart(fig, theme="streamlit")

def get_chart_3():
    import plotly.express as px

    df = px.data.gapminder().query("country == 'Canada'")
    fig = px.bar(df, x='year', y='pop',
                 labels={'pop':'population of Canada'}, height=400)

    st.plotly_chart(fig, theme="streamlit")


def get_chart_4():


    # Configura o tamanho do gráfico
    fig, ax = plt.subplots(figsize=(12, 8))  # Ajuste o tamanho para o desejado
    ax.plot([1, 2, 3, 4], [10, 20, 25, 30])

    # Mostra o gráfico no Streamlit
    st.pyplot(fig)