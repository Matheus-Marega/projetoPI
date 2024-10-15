import streamlit as st
from app.pages import pag_inicial, pagina_dashboard

def main():

    if 'pagina' not in st.session_state:
        st.session_state.pagina = 'pagina0'

    st.title("Area de Acesso ADMIN 🔒 ")
        
    username = st.text_input("Username")
    password = st.text_input("Password")

    if st.button("Entrar"):
        if username == "admin" and password == "123":
            st.session_state.pagina == 'pagina2'
            pag_inicial()



if __name__ == "__main__":
    main()

        
