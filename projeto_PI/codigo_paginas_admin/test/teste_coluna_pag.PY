import streamlit as st

import streamlit as st
from teste_df import get_chart, get_chart_3,get_chart_4


def mostrar_resumo_metricas():
    col1, col2 ,col3,col4 = st.columns(3)
    with col1:
        st.title("Texto de grafico1")
        get_chart_4()
    with col3:
        st.title("Texto de grafico2")
        get_chart()
    with col2:
        st.title("Texto de grafico3")
        get_chart_3()


mostrar_resumo_metricas()