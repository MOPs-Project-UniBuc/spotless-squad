import streamlit as st

from spotlesssquad.common import State


def render(state: State) -> None:
    st.header("Hello World!")
