import streamlit as st
from config.lists_for_functions import escala_satisfacao,frequencia_visita,sim_nao



def perguntas_estrutura():
    st.title("Perguntas Sobre a estrutura do Mall")

    ## O codigo abaixo verifica se as variaveis possuem valor zerado para que se recarregado a pagina, as informações sejam salvas com os Dados do Usuario
    if 'p1_pe' not in st.session_state:
        st.session_state.p1_pe = '-'
    if 'p2_pe' not in st.session_state:
        st.session_state.p2_pe = '-'
    if 'p3_pe' not in st.session_state:
        st.session_state.p3_pe = '-'
    if 'p4_pe' not in st.session_state:
        st.session_state.p4_pe = '-'
    if 'sm_pe' not in st.session_state:
        st.session_state.sm_pe = ''  

    st.session_state.p1_pe = st.selectbox(f"Como você avalia a infraestrutura geral do shopping {st.session_state.nome}?",escala_satisfacao, index=escala_satisfacao.index(st.session_state.p1_pe))
    st.session_state.p2_pe = st.selectbox("Com que frequência você visita o shopping?",frequencia_visita, index=frequencia_visita.index(st.session_state.p2_pe))
    st.session_state.p3_pe = st.selectbox("Como você avalia a limpeza e manutenção das áreas comuns do shopping?",escala_satisfacao, index=escala_satisfacao.index(st.session_state.p3_pe))
    st.session_state.p4_pe = st.selectbox("Você se sente seguro(a) durante sua visita ao shopping?", sim_nao,index=sim_nao.index(st.session_state.p4_pe))
    st.session_state.sm_pe = st.text_area("Quais melhorias você sugeriria para a experiência geral no shopping?", value=st.session_state.sm_pe)

    if st.button("Proximo >>"):
        st.session_state.pagina = 'pagina3'
    if st.button("<< Voltar"):
        st.session_state.pagina = 'pagina1'