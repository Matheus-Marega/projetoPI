import streamlit as st
from paginas.auth_adm import auth_admin
import streamlit as st
from paginas.pagina_inical_adm import mostrar_relatorio_semanal
from paginas.pagina_resumo_metricas import mostrar_resumo_metricas
from paginas.pagina_sugetsao_melhorias import mostrar_sugestao_melhorias_feedback


def main():
   authenticator =  auth_admin()
   authenticator.login()
   
   if st.session_state["authentication_status"] is False:
        st.error("Usuario/Senha invalido")

   elif st.session_state["authentication_status"] is None:
        st.warning("Por favor, Utilize se usuario e senha")

   elif st.session_state["authentication_status"] is True:
        opcao = st.sidebar.selectbox(
            "O que você deseja Visualizar?",
            ("Pagina Incial", "Sugestoes de Melhoria/Feedback", "Relatorio Semanal")
        )

        if opcao == "Pagina Incial":
            mostrar_resumo_metricas()
        elif opcao == "Sugestoes de Melhoria/Feedback":
            mostrar_sugestao_melhorias_feedback()
        elif opcao == "Relatorio Semanal":
            mostrar_relatorio_semanal()


if __name__ == "__main__":
    main()
