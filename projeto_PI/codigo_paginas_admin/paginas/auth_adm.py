import streamlit_authenticator as stauth
import streamlit as st
import yaml
from yaml.loader import SafeLoader

def auth_admin():
    with open('config/config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)


    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days']
    )

    authenticator.login()


    if st.session_state["authentication_status"]:
        authenticator.logout()
        st.write(f"Bem vindo {st.session_state["name"]}")
        st.write("Pagina de Sistema")
    elif st.session_state["authentication_status"] is False:
        st.error("Usuario/Senha invalido")
    elif st.session_state["authentication_status"] is None:
        st.warning("Por favor, Utilize se usuario e senha")

    