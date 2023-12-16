import streamlit as st

from spotlesssquad.common import State, get_user_details
from spotlesssquad.settings import common, models


def render(state: State) -> None:
    st.header("Settings")

    user = get_user_details(st.session_state["name"], state.sql_engine)

    st.write("User: ", user.name)

    name = st.text_input("Name", value=user.name, key="user_name")
    st.text_input("Username", value=user.username, key="username", disabled=True)
    st.text_input("Email", value=user.email, key="email", disabled=True)
    st.text_input("Password", value="********", key="password", disabled=True)
    phone = st.text_input("Phone", value=user.phone, key="phone")
    address = st.text_input("Address", value=user.address, key="address")
    city = st.text_input("City", value=user.city, key="city")
    country = st.text_input("Country", value=user.country, key="country")
    zip = st.text_input("ZIP Code", value=user.zip, key="postal_code")

    save = st.button("Save")

    if save:
        with st.spinner("Saving..."), state.sql_engine.begin() as con:
            if name != user.name:
                ret1 = common.update_name(user.email, name, con)
                if ret1 != models.UpdateStatus.SUCCESS:
                    st.error("Failed to update name")
                    return
            if phone != user.phone:
                ret2 = common.update_phone(user.email, phone, con)
                if ret2 != models.UpdatePhoneStatus.SUCCESS:
                    st.error("Failed to update phone")
                    return
            if address != user.address:
                ret3 = common.update_address(user.email, address, con)
                if ret3 != models.UpdateAddressStatus.SUCCESS:
                    st.error("Failed to update address")
                    return
            if city != user.city:
                ret4 = common.update_city(user.email, city, con)
                if ret4 != models.UpdateCityStatus.SUCCESS:
                    st.error("Failed to update city")
                    return
            if country != user.country:
                ret5 = common.update_country(user.email, country, con)
                if ret5 != models.UpdateCountryStatus.SUCCESS:
                    st.error("Failed to update country")
                    return
            if zip != user.zip:
                ret6 = common.update_zip(user.email, zip, con)
                if ret6 != models.UpdateZipStatus.SUCCESS:
                    st.error("Failed to update zip")
                    return
