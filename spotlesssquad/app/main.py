import logging
from datetime import datetime

import streamlit as st

from spotlesssquad.authentication import renderer as auth_renderer
from spotlesssquad.calc import renderer as calc_renderer
from spotlesssquad.common import get_state


def init_logging() -> None:
    logging.basicConfig(level=logging.DEBUG)


def main() -> None:
    init_logging()
    state = get_state()

    PAGES = {
        "Authentication": auth_renderer.render,
        "Calculator": calc_renderer.render,
    }

    st.sidebar.title("Navigation")
    st.sidebar.write("Time: {}".format(datetime.now()))
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    if selection is None:
        selection = "Main"

    page = PAGES[selection]
    page(state)


if __name__ == "__main__":
    st.set_page_config(page_title="NER", layout="wide")
    main()
