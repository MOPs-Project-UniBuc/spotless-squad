import base64

import cv2
import numpy as np
import streamlit as st

from spotlesssquad.common import State, get_user_details
from spotlesssquad.settings import common, models


def render(state: State) -> None:
    st.header("Settings")

    user = get_user_details(st.session_state["name"], state.sql_engine)

    if user.imgBase64 == "":
        image = cv2.imread("user.jpg")
    else:
        nparr = np.fromstring(  # type: ignore
            string=base64.b64decode(user.imgBase64),
            dtype=np.uint8,
        )
        image = cv2.imdecode(nparr, cv2.IMREAD_ANYCOLOR)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    st.subheader("User: ", user.name)

    col1, col2 = st.columns(2)
    with col1:
        st.image(
            image,
            caption="Account picture",
            width=100,
        )
    with col2:
        file = st.file_uploader(
            "Upload a new profile picture",
            type=["png", "jpg"],
        )

    st.subheader("Account Details")
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
            changed = False
            if name != user.name:
                ret1 = common.update_name(user.email, name, con)
                if ret1 != models.UpdateNameStatus.SUCCESS:
                    st.error("Failed to update name")
                    return
                changed = True
            if phone != user.phone:
                ret2 = common.update_phone(user.email, phone, con)
                if ret2 != models.UpdatePhoneStatus.SUCCESS:
                    st.error("Failed to update phone")
                    return  # blalasas
                changed = True
            if address != user.address:
                ret3 = common.update_address(user.email, address, con)
                if ret3 != models.UpdateAddressStatus.SUCCESS:
                    st.error("Failed to update address")
                    return
                changed = True
            if city != user.city:
                ret4 = common.update_city(user.email, city, con)
                if ret4 != models.UpdateCityStatus.SUCCESS:
                    st.error("Failed to update city")
                    return
                changed = True
            if country != user.country:
                ret5 = common.update_country(user.email, country, con)
                if ret5 != models.UpdateCountryStatus.SUCCESS:
                    st.error("Failed to update country")
                    return
                changed = True
            if zip != user.zip:
                ret6 = common.update_zip(user.email, zip, con)
                if ret6 != models.UpdateZipStatus.SUCCESS:
                    st.error("Failed to update zip")
                    return
                changed = True
            if file is not None:
                file_b64 = base64.b64encode(file.read()).decode("utf-8")
                ret7 = common.update_imgBase64(user.email, file_b64, con)
                if ret7 != models.UpdateImgStatus.SUCCESS:
                    st.error("Failed to update image")
                    return
                changed = True
            if changed:
                st.success("Successfully updated")
            else:
                st.info("Nothing to update")
