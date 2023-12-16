import streamlit as st

from spotlesssquad.common import State


def render(state: State) -> None:
    st.header("Sum Calculation!")

    st.number_input("a", value=1)
    st.number_input("b", value=1)
