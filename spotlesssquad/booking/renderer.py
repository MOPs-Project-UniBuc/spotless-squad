import streamlit as st

from spotlesssquad.booking import common, models
from spotlesssquad.common import State


def render(state: State) -> None:
    st.header("Booking")

    st.subheader("Search for a provider")
    username = st.session_state["name"]
    service_types = common.get_unique_service_types(state.sql_engine)

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input(label="Search by name")

    with col2:
        types = st.multiselect(label="Select service type", options=service_types)

    if len(types) == 0:
        types = service_types

    providers = common.get_all_providers(username, state.sql_engine)

    filtered_df = common.filter_provider_by_type(types, providers)
    st.date_input
    if name != "":
        filtered_df = common.filter_providers_by_name(name, filtered_df)

    st.dataframe(filtered_df)

    st.subheader("Book a provider")

    with st.form("book_provider"):
        provider_name = st.text_input(label="Provider name")
        date = st.date_input(label="Date")
        submit_button = st.form_submit_button(label="Book")

    if submit_button and date is not None:
        booking_status = common.book_provider(
            username=username,
            provider_name=provider_name,
            date=date,  # type: ignore
            sql_engine=state.sql_engine,
        )

        if booking_status == models.BookingStatus.SUCCESS:
            st.success("Booking successful")
        elif booking_status == models.BookingStatus.PROVIDER_NOT_FOUND:
            st.error("Provider not found")
        elif booking_status == models.BookingStatus.PROVIDER_NOT_AVAILABLE:
            st.error("Provider not available")
