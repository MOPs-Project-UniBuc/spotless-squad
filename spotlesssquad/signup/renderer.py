import streamlit as st

from spotlesssquad.common import State
from spotlesssquad.signup import common


def client_form(state: State) -> None:
    with st.form(key="sign_up_form"):
        username = st.text_input("Username", key="username1")
        password = st.text_input("Password", type="password", key="password1")
        name = st.text_input("Name", key="name_")
        email = st.text_input("Email", key="email")
        city = st.text_input("City", key="city")
        address = st.text_input("Address", key="address")
        country = st.text_input("Country", key="country")
        zip = st.text_input("Zip", key="zip")
        phone = st.text_input("Phone", key="phone")
        submit_button3 = st.form_submit_button(label="Sign up")
        if submit_button3:
            if common.signup_client(
                username,
                password,
                name,
                email,
                city,
                address,
                country,
                zip,
                phone,
                state.sql_engine,
            ):
                print("done")
                # st.session_state["authentication_status"] = True
                # st.session_state["name"] = username
                # st.experimental_rerun()
                st.success("Success")
                st.session_state["sign_up"] = False

                st.rerun()

            else:
                st.error("The username or password you have entered is invalid.")


def clean_provider_form(state: State) -> None:
    service_types = common.get_service_types(state.sql_engine)

    with st.form(key="sign_up_form"):
        username = st.text_input("Username", key="username1")
        password = st.text_input("Password", type="password", key="password1")
        name = st.text_input("Name", key="name_")
        email = st.text_input("Email", key="email")
        city = st.text_input("City", key="city")
        address = st.text_input("Address", key="address")
        country = st.text_input("Country", key="country")
        zip = st.text_input("Zip", key="zip")
        phone = st.text_input("Phone", key="phone")
        service_type = st.selectbox(
            "Service Type",
            service_types,
            key="service_type",
        )
        if service_type is None:
            service_type = service_types[0]
        submit_button3 = st.form_submit_button(label="Sign up")
        if submit_button3:
            if common.signup_clean_provider(
                username,
                password,
                name,
                email,
                city,
                address,
                country,
                zip,
                phone,
                service_type,
                state.sql_engine,
            ):
                print("done")
                # st.session_state["authentication_status"] = True
                # st.session_state["name"] = username
                # st.experimental_rerun()
                st.success("Success")
                st.session_state["sign_up"] = False

                st.rerun()

            else:
                st.error("The username or password you have entered is invalid.")


def render(state: State) -> None:
    _, col, _ = st.columns([1, 2, 1])

    with col:
        st.title("SpotlessSquad", anchor="center")
        user_type = st.radio(
            label="Are you a client or a cleaner?",
            options=["Client", "Cleaner"],
            horizontal=True,
        )
        if user_type == "Client":
            client_form(state)
        else:
            clean_provider_form(state)
