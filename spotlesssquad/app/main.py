import logging
import sys

import sentry_sdk
import streamlit as st

from spotlesssquad.booking import renderer as booking_renderer
from spotlesssquad.common import get_state
from spotlesssquad.login import renderer as login_renderer
from spotlesssquad.my_bookings import renderer as my_bookings_renderer
from spotlesssquad.settings import renderer as settings_renderer
from spotlesssquad.signup import renderer as signup_renderer

runner = sys.modules["streamlit.runtime.scriptrunner.script_runner"]
original_handler = runner.handle_uncaught_app_exception


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


def sentry_handler(exception: Exception) -> None:
    """Pass the provided exception through to sentry."""
    sentry_sdk.capture_exception(exception)
    return original_handler(exception)


if original_handler != sentry_handler:
    print("---> add exception handler with sentry_handler")
    runner.handle_uncaught_app_exception = sentry_handler  # type: ignore


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

            st.rerun()

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
        st.session_state.get("sign_up", False) is True
        and st.session_state.get("name", "") == ""
    ):
        signup_renderer.render(state)

    elif (
        st.session_state.get("authentication_status", False) is False
        and st.session_state.get("name", "") == ""
    ):
        login_renderer.render(state)


if __name__ == "__main__":
    st.set_page_config(page_title="SpotlessSquad", layout="wide")
    main()
