import streamlit as st
from paginas.pagina_de_cadastro import pagina_cadastro
from paginas.pagina_perguntas_sobre_estrutura_do_mall import perguntas_estrutura
from paginas.pagina_perguntas_sobre_lojas_do_mall import perguntas_lojas
from paginas.pagina_final_do_formulario import pagina_final

    
def main():
# Inicializa a sessão se ainda não estiver inicializada
    if 'pagina' not in st.session_state:
        st.session_state.pagina = 'pagina1'

    # Navega para a página correspondente
    if st.session_state.pagina == 'pagina1':
        pagina_cadastro()
    elif st.session_state.pagina == 'pagina2':
        perguntas_estrutura()
    elif st.session_state.pagina == 'pagina3':
        perguntas_lojas()
    elif st.session_state.pagina == 'pagina4':
        pagina_final()
   

if __name__ == "__main__":
    main()
