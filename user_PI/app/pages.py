import streamlit as st
from pydantic import ValidationError
from dataContract import User,lista_segmentos,escala_satisfacao,frequencia_visita,sim_nao,genero
from DataBase import PerguntasInformacoesClientes, PerguntasEstruturaMall, PerguntasLojasVisitadas, engine
from sqlalchemy.orm import sessionmaker

# Criação da sessão para interagir com o banco de dados
Session = sessionmaker(bind=engine)
session = Session()

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



def perguntas_lojas():
    st.title("Perguntas Sobre as Lojas visitadas")

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

        
    
    st.session_state.p1_pl = st.selectbox("Dentre as Lojas visitadas, qual segmento você mais frequenta?: ",lista_segmentos, index=lista_segmentos.index(st.session_state.p1_pl))
    st.session_state.p2_pl = st.selectbox("Você encontrou facilidade para localizar as lojas que estava procurando?",sim_nao, index=sim_nao.index(st.session_state.p2_pl))
    st.session_state.p3_pl = st.selectbox("Como você avalia o atendimento nas lojas que visitou?",sim_nao, index=sim_nao.index(st.session_state.p3_pl))
    st.session_state.p4_pl = st.selectbox("As lojas oferecem produtos que atendem suas necessidades e expectativas?",sim_nao, index=sim_nao.index(st.session_state.p4_pl))
    st.session_state.p5_pl = st.selectbox("Como você avalia a variedade de lojas disponíveis no shopping?: ",escala_satisfacao, index=escala_satisfacao.index(st.session_state.p5_pl))
    st.session_state.sm_pl = st.text_area("Sugestão Quais produtos ou serviços você gostaria de ver nas lojas que ainda não estão disponíveis? Melhoria", value=st.session_state.sm_pl)


    if st.button("Finalizar >>"):
        st.session_state.pagina = 'pagina4'

        #Adicionando as Informações coletadas ao Banco de Dados
        insercao_informacoes_cliente = PerguntasInformacoesClientes(
            nome=st.session_state.nome, 
            email=st.session_state.email,
            data_visita=st.session_state.data,
            genero=st.session_state.gender
        )

        insercao_respostas_perguntas_estrutura_mall = PerguntasEstruturaMall(
            pergunta1_estrutura_mall = st.session_state.p1_pe,
            pergunta2_estrutura_mall = st.session_state.p2_pe,
            pergunta3_estrutura_mall = st.session_state.p3_pe,
            pergunta4_estrutura_mall = st.session_state.p4_pe,
            pergunta5_estrutura_mall = st.session_state.sm_pe
        )

        insercao_respostas_perguntas_lojas_visitadas = PerguntasEstruturaMall(
            pergunta1_lojas_visitadas = st.session_state.p1_pl,
            pergunta2_lojas_visitadas = st.session_state.p2_pl,
            pergunta3_lojas_visitadas = st.session_state.p3_pl,
            pergunta4_lojas_visitadas = st.session_state.p4_pl,
            pergunta5_lojas_visitadas = st.session_state.sm_pl
        )

        session.add(insercao_informacoes_cliente)
        session.add(insercao_respostas_perguntas_estrutura_mall)
        session.add(insercao_respostas_perguntas_lojas_visitadas)
        session.commit()

    if st.button("<< Voltar"):
        st.session_state.pagina = 'pagina2'



def pagina_final():
    st.title("Obrigado por participar!")
