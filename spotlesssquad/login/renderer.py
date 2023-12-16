import streamlit as st

from spotlesssquad.common import State
from spotlesssquad.login.common import login


def render(state: State) -> None:
    _, col, _ = st.columns([1, 2, 1])

    with col:
        st.title("SpotlessSquad", anchor="center")

        with st.form(key="my_form"):
            username = st.text_input("Username", key="username")
            password = st.text_input("Password", type="password", key="password")
            submit_button = st.form_submit_button(label="Login")

            if submit_button:
                if login(username, password, state.sql_engine):
                    st.session_state["authentication_status"] = True
                    st.session_state["name"] = username
                    st.experimental_rerun()

                else:
                    st.error("The username or password you have entered is invalid.")
