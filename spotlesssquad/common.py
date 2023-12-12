import logging

import streamlit as st


class State:
    def __init__(self) -> None:
        logging.info("State.__init__")


def get_state() -> State:
    if "state" not in st.session_state:
        print("WARNING: new state created")
        st.session_state["state"] = State()

    return st.session_state["state"]
