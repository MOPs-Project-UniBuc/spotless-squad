import logging

import streamlit as st

from spotlesssquad.booking import renderer as booking_renderer
from spotlesssquad.common import get_state
from spotlesssquad.login import renderer as login_renderer
from spotlesssquad.my_bookings import renderer as my_bookings_renderer
from spotlesssquad.settings import renderer as settings_renderer


def init_logging() -> None:
    logging.basicConfig(level=logging.DEBUG)


def main() -> None:
    init_logging()
    state = get_state()

    if st.session_state.get("name", "") != "":
        st.sidebar.title("SpotlessSquad", anchor="center")
        username = st.session_state["name"]
        st.sidebar.title(f"Salutare, *{username}*")

        logout = st.sidebar.button("Logout")

        if logout:
            del st.session_state["authentication_status"]
            del st.session_state["name"]

            st.experimental_rerun()

        PAGES = {
            "Booking": booking_renderer.render,
            "My Booking": my_bookings_renderer.render,
            "Settings": settings_renderer.render,
        }

        username = st.session_state["name"]

        selection = st.sidebar.radio("Go to", list(PAGES.keys()))

        if selection is None:
            selection = "Booking"

        page = PAGES[selection]
        page(state)

    elif (
        st.session_state.get("authentication_status", False) is False
        and st.session_state.get("name", "") == ""
    ):
        login_renderer.render(state)


if __name__ == "__main__":
    st.set_page_config(page_title="SpotlessSquad", layout="wide")
    main()
