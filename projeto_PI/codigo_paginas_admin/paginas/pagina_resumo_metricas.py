import streamlit as st
from test.teste_df import get_chart, get_chart_2, get_chart_3


def mostrar_resumo_metricas():
    col1, col2 ,col3 = st.columns(3)
    with col1:
        get_chart()
    with col3:
        get_chart_2()
    with col2:
        get_chart_3()

