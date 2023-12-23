import streamlit as st

from spotlesssquad.common import State
from spotlesssquad.login.common import login
from spotlesssquad.signup.common import signup

def render(state: State) -> None:
    _, col, _ = st.columns([1, 2, 1])

    with col:
        st.title("SpotlessSquad", anchor="center")

        with st.form(key="my_form"):
            username = st.text_input("Username", key="username")
            password = st.text_input("Password", type="password", key="password")
            submit_button = st.form_submit_button(label="Login")
            submit_button2 = st.form_submit_button(label="Register")

            if submit_button:
                if login(username, password, state.sql_engine):
                    st.session_state["authentication_status"] = True
                    st.session_state["name"] = username
                    st.rerun()

                else:
                    st.error("The username or password you have entered is invalid.")
            if submit_button2:
                username = st.text_input("Username", key="username1")
                password = st.text_input("Password", type="password", key="password1")
                name = st.text_input("Name", key="name")
                email = st.text_input("Email", key="email")
                city = st.text_input("City", key="city")
                address = st.text_input("Address", key="address")
                country = st.text_input("Country", key="country")
                zip = st.text_input("Zip", key="zip")
                phone = st.text_input("Phone", key="phone")
                submit_button3 = st.form_submit_button(label="Sign up")
                if submit_button3:
                    if signup(username, password, name, email, city, address, country, zip, phone, state.sql_engine):
                        print("done")
                        # st.session_state["authentication_status"] = True
                        # st.session_state["name"] = username
                        # st.experimental_rerun()
                        st.text("Success")

                    else:
                        st.error("The username or password you have entered is invalid.")