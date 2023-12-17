import streamlit as st

from spotlesssquad.common import State
from spotlesssquad.my_bookings import common


def render(state: State) -> None:
    st.header("My Bookings")

    username = st.session_state["name"]

    df = common.get_all_bookings(username, state.sql_engine)

    st.dataframe(df)
