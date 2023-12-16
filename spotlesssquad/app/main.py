import logging
from datetime import datetime

import sentry_sdk
import streamlit as st

from spotlesssquad.authentication import renderer as auth_renderer
from spotlesssquad.calc import renderer as calc_renderer
from spotlesssquad.common import get_state


def init_logging() -> None:
    logging.basicConfig(level=logging.DEBUG)


sentry_sdk.init(
    dsn="https://543eb31bb3cfa5133800e1afad552524@o4506404697210880.ingest.sentry.io/4506404699635712",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
    enable_tracing=True,
)


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
