import streamlit as st

def pag_inicial():
    navegar_paginas()
    st.session_state.pagina = "pagina1"
    st.title("Página 1")
    st.write("Você está na Página 1")


def pagina_dashboard():
    navegar_paginas()
    st.session_state.pagina = "pagina2"
    st.title("Teste")


def navegar_paginas():
    st.session_state.pagina = "pagina3"
    st.sidebar.title("Navegação")
    pagina = st.sidebar.selectbox("Escolha uma página", ["Página 1", "Página 2"])
    if pagina == "Página 1":
        st.session_state.pagina = "pagina1"
        pag_inicial()
    elif pagina == "Página 2":
        st.session_state.pagina = "pagina2"
        pagina_dashboard()


