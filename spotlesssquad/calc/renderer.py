import streamlit as st

from spotlesssquad.calc.common import calc_sum
from spotlesssquad.common import State


def render(state: State) -> None:
    st.header("Sum Calculation!")

    a = st.number_input("a", value=1)
    b = st.number_input("b", value=1)

    st.write("Result:", calc_sum(a, b))
