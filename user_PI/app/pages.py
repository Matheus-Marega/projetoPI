import streamlit as st
from pydantic import ValidationError
from dataContract import User, lojas_shopping, lista_segmentos, nota


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

    genero = ["Masculino", "Feminino", "Outros"]

    # Criação dos campos com valores guardados no session_state
    st.session_state.nome = st.text_input("Nome", value=st.session_state.nome)
    st.session_state.email = st.text_input("Email", value=st.session_state.email)
    st.session_state.data = st.date_input("Data da Visita", value=st.session_state.data)
    st.session_state.gender = st.selectbox("Gênero", genero, index=genero.index(st.session_state.gender))


    if st.button("Próximo >>"):
        try:
            dados_usuario = User(
                nome=st.session_state.nome, 
                email=st.session_state.email,
                data=st.session_state.data,
                gender=st.session_state.gender
            )
            st.success("Dados cadastrados com sucesso!")
            st.write(dados_usuario)
            st.session_state.pagina = 'pagina2'
        except ValidationError as e:
            st.error(f"Erro ao cadastrar os dados: {e}")

def perguntas_estrutura():
    st.title("Perguntas Sobre a estrutura do Mall")


    # De acordo com as Perguntas, alterar as funções, a estrutura abaixo, esta validando apenas dados em STR.
    if 'p1_pe' not in st.session_state:
        st.session_state.p1_pe = ''
    if 'p2_pe' not in st.session_state:
        st.session_state.p2_pe = ''
    if 'p3_pe' not in st.session_state:
        st.session_state.p3_pe = ''
    if 'p4_pe' not in st.session_state:
        st.session_state.p4_pe = ''
    if 'sm_pe' not in st.session_state:
        st.session_state.sm_pe = ''  

    # De acordo com as Perguntas, alterar as funções, a estrutura abaixo, esta validando apenas dados em STR.
    st.session_state.p1_pe = st.text_input("Pergunta 1", value=st.session_state.p1_pe)
    st.session_state.p2_pe = st.text_input("Pergunta 2", value=st.session_state.p2_pe)
    st.session_state.p3_pe = st.text_input("Pergunta 3", value=st.session_state.p3_pe)
    st.session_state.p4_pe = st.text_input("Pergunta 4", value=st.session_state.p4_pe)
    st.session_state.sm_pe = st.text_area("Sugestão de Melhoria", value=st.session_state.sm_pe)

    if st.button("Proximo >>"):
        st.session_state.pagina = 'pagina3'
    if st.button("<< Voltar"):
        st.session_state.pagina = 'pagina1'



def perguntas_lojas():
    st.title("Perguntas Sobre as Lojas visitadas")

    if 'p1_pl' not in st.session_state:
        st.session_state.p1_pl = "Nenhuma"
    if 'p2_pl' not in st.session_state:
        st.session_state.p2_pl = 'Nenhuma'
    if 'p3_pl' not in st.session_state:
        st.session_state.p3_pl = '-'
    if 'p4_pl' not in st.session_state:
        st.session_state.p4_pl = ''
    if 'sm_pl' not in st.session_state:
        st.session_state.sm_pl = ''  

        
    st.session_state.p1_pl = st.selectbox("Segmento: ",lista_segmentos, index=lista_segmentos.index(st.session_state.p1_pl))
    st.session_state.p2_pl = st.selectbox("Lojas Visitadas",lojas_shopping, index=lojas_shopping.index(st.session_state.p2_pl))
    st.session_state.p3_pl = st.selectbox("Nota de atendimento e produto",nota, index=nota.index(st.session_state.p3_pl))
    st.session_state.p4_pl = st.text_input("Pergunta Adicional", value=st.session_state.p4_pl)
    st.session_state.sm_pl = st.text_area("Sugestão de Melhoria", value=st.session_state.sm_pl)


    if st.button("Finalizar >>"):
        st.session_state.pagina = 'pagina4'
    if st.button("<< Voltar"):
        st.session_state.pagina = 'pagina2'



def pagina_final():
    st.title("Obrigado por participar!")
