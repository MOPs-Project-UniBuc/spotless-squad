from typing import Any

import sqlalchemy
import sqlalchemy.engine

from spotlesssquad.settings import models
from spotlesssquad.sql import tables


def user_exists(email: str, con: sqlalchemy.engine.Connection) -> bool:
    """
    Check if user exists.
    """
    stmt = sqlalchemy.select(tables.ClientUsers).where(
        tables.ClientUsers.email == email
    )
    result = con.execute(stmt).fetchone()
    return result is not None


def update_user(
    email: str,
    values: dict[sqlalchemy.Column[Any], str],
    con: sqlalchemy.engine.Connection,
) -> bool:
    stmt = (
        sqlalchemy.update(tables.ClientUsers)
        .where(tables.ClientUsers.email == email)
        .values(values)
    )

    res = con.execute(stmt)

    return res.rowcount == 1


def check_name_validity(name: str) -> bool:
    """
    Check if name is valid.
    """
    return len(name) <= 0


def update_name(
    email: str,
    new_name: str,
    con: sqlalchemy.engine.Connection,
) -> models.UpdateNameStatus:
    # check if user exists
    if not user_exists(email, con):
        return models.UpdateNameStatus.USER_NOT_FOUND

    if check_name_validity(new_name):
        return models.UpdateNameStatus.NAME_IS_NONE

    res = update_user(
        email=email,
        values={tables.ClientUsers.name: new_name},
        con=con,
    )

    if res:
        return models.UpdateNameStatus.SUCCESS
    else:
        return models.UpdateNameStatus.FAILURE


def check_password_validity(password: str) -> bool:
    """
    Check if password is valid.
    """
    return len(password) >= 8


def update_password(
    email: str,
    new_password: str,
    con: sqlalchemy.engine.Connection,
) -> models.UpdatePasswordStatus:
    if not check_password_validity(new_password):
        return models.UpdatePasswordStatus.PASSWORD_TOO_SHORT

    # check if user exists
    if not user_exists(email, con):
        return models.UpdatePasswordStatus.USER_NOT_FOUND

    res = update_user(
        email=email,
        values={tables.ClientUsers.password: new_password},
        con=con,
    )

    if res:
        return models.UpdatePasswordStatus.SUCCESS
    else:
        return models.UpdatePasswordStatus.FAILURE


def check_phone_validity(phone: str) -> models.UpdatePhoneStatus:
    """
    Check if phone is valid.
    """
    if len(phone) < 10:
        return models.UpdatePhoneStatus.NUMBER_TOO_SHORT
    elif len(phone) > 10:
        return models.UpdatePhoneStatus.NUMBER_TOO_LONG

    return models.UpdatePhoneStatus.SUCCESS


def update_phone(
    email: str,
    new_phone: str,
    con: sqlalchemy.engine.Connection,
) -> models.UpdatePhoneStatus:
    # check if user exists
    if not user_exists(email, con):
        return models.UpdatePhoneStatus.USER_NOT_FOUND

    validity_res = check_phone_validity(new_phone)
    if validity_res != models.UpdatePhoneStatus.SUCCESS:
        return validity_res

    res = update_user(
        email=email,
        values={tables.ClientUsers.phone: new_phone},
        con=con,
    )

    if res:
        return models.UpdatePhoneStatus.SUCCESS
    else:
        return models.UpdatePhoneStatus.FAILURE


def check_address_validity(address: str) -> bool:
    """
    Check if address is valid.
    """
    return len(address) <= 0


def update_address(
    email: str,
    new_address: str,
    con: sqlalchemy.engine.Connection,
) -> models.UpdateAddressStatus:
    # check if user exists
    if not user_exists(email, con):
        return models.UpdateAddressStatus.USER_NOT_FOUND

    if check_address_validity(new_address):
        return models.UpdateAddressStatus.ADDRESS_IS_NONE

    res = update_user(
        email=email,
        values={tables.ClientUsers.address: new_address},
        con=con,
    )

    if res:
        return models.UpdateAddressStatus.SUCCESS
    else:
        return models.UpdateAddressStatus.FAILURE


def check_city_validity(city: str) -> bool:
    """
    Check if city is valid.
    """
    return len(city) <= 0


def update_city(
    email: str,
    new_city: str,
    con: sqlalchemy.engine.Connection,
) -> models.UpdateCityStatus:
    # check if user exists
    if not user_exists(email, con):
        return models.UpdateCityStatus.USER_NOT_FOUND

    if check_city_validity(new_city):
        return models.UpdateCityStatus.CITY_IS_NONE

    res = update_user(
        email=email,
        values={tables.ClientUsers.city: new_city},
        con=con,
    )

    if res:
        return models.UpdateCityStatus.SUCCESS
    else:
        return models.UpdateCityStatus.FAILURE


def check_zip_validity(zip: str) -> bool:
    """
    Check if zip is valid.
    """
    return len(zip) == 6


def update_zip(
    email: str,
    new_zip: str,
    con: sqlalchemy.engine.Connection,
) -> models.UpdateZipStatus:
    """
    Update user for the given email.
    """

    # check if user exists
    if not user_exists(email, con):
        return models.UpdateZipStatus.USER_NOT_FOUND

    if not check_zip_validity(new_zip):
        return models.UpdateZipStatus.ZIP_INVALID

    res = update_user(
        email=email,
        values={tables.ClientUsers.zip: new_zip},
        con=con,
    )

    if res:
        return models.UpdateZipStatus.SUCCESS
    else:
        return models.UpdateZipStatus.FAILURE


def check_country_validity(country: str) -> bool:
    """
    Check if country is valid.
    """
    return len(country) <= 0


def update_country(
    email: str,
    new_country: str,
    con: sqlalchemy.engine.Connection,
) -> models.UpdateCountryStatus:
    """
    Update user for the given email.
    """

    # check if user exists
    if not user_exists(email, con):
        return models.UpdateCountryStatus.USER_NOT_FOUND

    if check_country_validity(new_country):
        return models.UpdateCountryStatus.COUNTRY_IS_NONE

    res = update_user(
        email=email,
        values={tables.ClientUsers.country: new_country},
        con=con,
    )

    if res == 1:
        return models.UpdateCountryStatus.SUCCESS
    else:
        return models.UpdateCountryStatus.FAILURE


def update_imgBase64(
    email: str,
    new_imgBase64: str,
    con: sqlalchemy.engine.Connection,
) -> models.UpdateImgStatus:
    """
    Update user for the given email.
    """

    # check if user exists
    if not user_exists(email, con):
        return models.UpdateImgStatus.USER_NOT_FOUND

    res = update_user(
        email=email,
        values={tables.ClientUsers.imgBase64: new_imgBase64},
        con=con,
    )

    if res:
        return models.UpdateImgStatus.SUCCESS
    else:
        return models.UpdateImgStatus.FAILURE
