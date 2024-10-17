import streamlit as st
from pydantic import ValidationError
from forms.user_form import User
from config.lists_for_functions import genero

def pagina_cadastro():
    st.title("Formulário de Cadastro")
    ## O codigo abaixo verifica se as variaveis possuem valor zerado para que se recarregado a pagina, as informações sejam salvas com os Dados do Usuario

    if 'nome' not in st.session_state:
        st.session_state.nome = ''
    if 'email' not in st.session_state:
        st.session_state.email = ''
    if 'data' not in st.session_state:
        st.session_state.data = None
    if 'gender' not in st.session_state:
        st.session_state.gender = 'Masculino'  

    # Criação dos campos com valores guardados no session_state
    st.session_state.nome = st.text_input("Nome", value=st.session_state.nome)
    st.session_state.email = st.text_input("Email", value=st.session_state.email)
    st.session_state.data = st.date_input("Data da Visita", value=st.session_state.data)
    st.session_state.gender = st.selectbox("Gênero", genero, index=genero.index(st.session_state.gender))

    #Botão de proxima pagina, que quando clicado, valida as Informações preenchidas
    if st.button("Próximo >>"):
        try:
            dados_usuario = User(
                nome=st.session_state.nome, 
                email=st.session_state.email,       #Validação das infomações
                data=st.session_state.data,
                gender=st.session_state.gender
            )
            st.success("Dados cadastrados com sucesso!")
            st.session_state.pagina = 'pagina2'
        except ValidationError as e:
            st.error(f"Erro ao cadastrar os dados: {e}")