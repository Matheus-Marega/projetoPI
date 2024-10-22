import streamlit as st
from config.lists_for_functions import lista_segmentos, escala_satisfacao, sim_nao
from database.models import PerguntasInformacoesClientes, PerguntasEstruturaMall, PerguntasLojasVisitadas
from database.db_setup import get_db  # Importa a função que obtém a sessão
from sqlalchemy.orm import Session
from contextlib import contextmanager

@contextmanager
def get_session():
    db = next(get_db())  # Obtém a sessão do banco de dados
    try:
        yield db
    finally:
        db.close()

def perguntas_lojas():
    st.title("Perguntas Sobre as Lojas visitadas")

    # Estado inicial das perguntas (pode ser ajustado conforme sua necessidade)
    if 'p1_pl' not in st.session_state:
        st.session_state.p1_pl = "Nenhuma"
    if 'p2_pl' not in st.session_state:
        st.session_state.p2_pl = "-"
    if 'p3_pl' not in st.session_state:
        st.session_state.p3_pl = "-"
    if 'p4_pl' not in st.session_state:
        st.session_state.p4_pl = "-"
    if 'p5_pl' not in st.session_state:
        st.session_state.p5_pl = "-"
    if 'sm_pl' not in st.session_state:
        st.session_state.sm_pl = ''

    # Renderizando os componentes no Streamlit
    st.session_state.p1_pl = st.selectbox("Dentre as Lojas visitadas, qual segmento você mais frequenta?: ", lista_segmentos, index=lista_segmentos.index(st.session_state.p1_pl))
    st.session_state.p2_pl = st.selectbox("Você encontrou facilidade para localizar as lojas que estava procurando?", sim_nao, index=sim_nao.index(st.session_state.p2_pl))
    st.session_state.p3_pl = st.selectbox("Como você avalia o atendimento nas lojas que visitou?", sim_nao, index=sim_nao.index(st.session_state.p3_pl))
    st.session_state.p4_pl = st.selectbox("As lojas oferecem produtos que atendem suas necessidades e expectativas?", sim_nao, index=sim_nao.index(st.session_state.p4_pl))
    st.session_state.p5_pl = st.selectbox("Como você avalia a variedade de lojas disponíveis no shopping?: ", escala_satisfacao, index=escala_satisfacao.index(st.session_state.p5_pl))
    st.session_state.sm_pl = st.text_area("Sugestão: Quais produtos ou serviços você gostaria de ver nas lojas que ainda não estão disponíveis? Melhoria", value=st.session_state.sm_pl)

    # Inserção no banco de dados
    if st.button("Finalizar >>"):
        st.session_state.pagina = 'pagina4'
        
        with get_session() as session:
            # Adicionando as informações coletadas ao banco de dados
            insercao_informacoes_cliente = PerguntasInformacoesClientes(
                nome=st.session_state.nome, 
                email=st.session_state.email,
                data_visita=st.session_state.data,
                genero=st.session_state.gender
            )

            insercao_respostas_perguntas_estrutura_mall = PerguntasEstruturaMall(
                pergunta1_estrutura_mall=st.session_state.p1_pe,
                pergunta2_estrutura_mall=st.session_state.p2_pe,
                pergunta3_estrutura_mall=st.session_state.p3_pe,
                pergunta4_estrutura_mall=st.session_state.p4_pe,
                pergunta5_estrutura_mall=st.session_state.sm_pe
            )

            insercao_respostas_perguntas_lojas_visitadas = PerguntasLojasVisitadas( 
                pergunta1_lojas_visitadas=st.session_state.p1_pl,
                pergunta2_lojas_visitadas=st.session_state.p2_pl,
                pergunta3_lojas_visitadas=st.session_state.p3_pl,
                pergunta4_lojas_visitadas=st.session_state.p4_pl,
                pergunta5_lojas_visitadas=st.session_state.sm_pl
            )

            session.add(insercao_informacoes_cliente)
            session.add(insercao_respostas_perguntas_estrutura_mall)
            session.add(insercao_respostas_perguntas_lojas_visitadas)
            session.commit()

    # Botão de voltar para a página anterior
    if st.button("<< Voltar"):
        st.session_state.pagina = 'pagina2'
