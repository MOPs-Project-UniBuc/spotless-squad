import pandas as pd
import sqlalchemy

from spotlesssquad.settings import models
from spotlesssquad.settings.common import (
    update_address,
    update_city,
    update_country,
    update_imgBase64,
    update_name,
    update_password,
    update_phone,
    update_zip,
)
from spotlesssquad.sql import tables


def populate_table(sql_engine: sqlalchemy.engine.Engine) -> None:
    # INSERT CLIENT USER
    # Populate ClientUsers Table
    users_df = pd.DataFrame(
        [
            (
                "name",
                "username",
                "password123",
                "email@gmail.com",
                "0767158866",
                "address",
                "city",
                "zip",
                "country",
                "",
            ),
        ],
        columns=[
            "name",
            "username",
            "password",
            "email",
            "phone",
            "address",
            "city",
            "zip",
            "country",
            "imgBase64",
        ],
    )

    with sql_engine.begin() as con:
        insert_stmt = sqlalchemy.insert(tables.ClientUsers).values(
            users_df.to_dict(orient="records")
        )
        con.execute(insert_stmt)


def test_update_user_name_1(sql_engine: sqlalchemy.engine.Engine) -> None:
    """
    Scenario: Update an user's name
    Context: user exists
    """

    populate_table(sql_engine)

    with sql_engine.begin() as con:
        res = update_name(email="email@gmail.com", new_name="new_user", con=con)

        # Check that the user was updated
        stmt = sqlalchemy.select(tables.ClientUsers).where(
            tables.ClientUsers.name == "new_user"
        )

        users_df = pd.read_sql_query(stmt, con)

    assert res == models.UpdateNameStatus.SUCCESS
    assert users_df.shape[0] == 1
    assert users_df.iloc[0]["name"] == "new_user"


def test_update_user_name_2(sql_engine: sqlalchemy.engine.Engine) -> None:
    """
    Scenario: Update an user's name
    Context: user doesn't exist
    """

    populate_table(sql_engine)

    with sql_engine.begin() as con:
        res = update_name(email="wrong_email@gmail.com", new_name="new_user", con=con)

        # Check that the user was updated
        stmt = sqlalchemy.select(tables.ClientUsers).where(
            (tables.ClientUsers.email == "wrong_email@gmail.com")
        )
        users_df = pd.read_sql_query(stmt, con)

    assert res == models.UpdateNameStatus.USER_NOT_FOUND
    assert users_df.shape[0] == 0


def test_update_user_password_1(sql_engine: sqlalchemy.engine.Engine) -> None:
    """
    Scenario: Update an user's password
    Context: user exists
    """

    populate_table(sql_engine)

    with sql_engine.begin() as con:
        res = update_password(
            email="email@gmail.com", new_password="password1234", con=con
        )

        # Check that the user was updated
        stmt = sqlalchemy.select(tables.ClientUsers).where(
            (tables.ClientUsers.name == "name")
        )
        users_df = pd.read_sql_query(stmt, con)

    assert res == models.UpdatePasswordStatus.SUCCESS
    assert users_df.shape[0] == 1
    assert users_df.iloc[0]["password"] == "password1234"


def test_update_user_password_2(sql_engine: sqlalchemy.engine.Engine) -> None:
    """
    Scenario: Update an user's password
    Context: user doesn't exist
    """

    populate_table(sql_engine)

    with sql_engine.begin() as con:
        res = update_password(
            email="wrong_email@gmail.com", new_password="password123", con=con
        )

        # Check that the user was updated
        stmt = sqlalchemy.select(tables.ClientUsers).where(
            (tables.ClientUsers.email == "wrong_email@gmail.com")
        )
        users_df = pd.read_sql_query(stmt, con)

    assert res == models.UpdatePasswordStatus.USER_NOT_FOUND
    assert users_df.shape[0] == 0


def test_update_user_password_3(sql_engine: sqlalchemy.engine.Engine) -> None:
    """
    Scenario: Update an user's password
    Context: user exists, password too short
    """

    populate_table(sql_engine)

    with sql_engine.begin() as con:
        res = update_password(email="email@gmail.com", new_password="passw", con=con)

    assert res == models.UpdatePasswordStatus.PASSWORD_TOO_SHORT


def test_update_user_phone_1(sql_engine: sqlalchemy.engine.Engine) -> None:
    """
    Scenario: Update an user's phone number
    Context: user exists, phone number too short
    """

    populate_table(sql_engine)

    with sql_engine.begin() as con:
        res = update_phone(email="email@gmail.com", new_phone="076715", con=con)

    assert res == models.UpdatePhoneStatus.NUMBER_TOO_SHORT


def test_update_user_phone_2(sql_engine: sqlalchemy.engine.Engine) -> None:
    """
    Scenario: Update an user's phone number
    Context: user exists, phone number too short
    """

    populate_table(sql_engine)

    with sql_engine.begin() as con:
        res = update_phone(email="email@gmail.com", new_phone="07671588667", con=con)

    assert res == models.UpdatePhoneStatus.NUMBER_TOO_LONG


def test_update_user_phone_3(sql_engine: sqlalchemy.engine.Engine) -> None:
    """
    Scenario: Update an user's phone number
    Context: user exists, phone ok
    """

    populate_table(sql_engine)

    with sql_engine.begin() as con:
        res = update_phone(email="email@gmail.com", new_phone="0767156688", con=con)

        # Check that the user was updated
        stmt = sqlalchemy.select(tables.ClientUsers).where(
            (tables.ClientUsers.email == "email@gmail.com")
        )
        users_df = pd.read_sql_query(stmt, con)

    assert res == models.UpdatePhoneStatus.SUCCESS
    assert users_df.shape[0] == 1
    assert users_df.iloc[0]["phone"] == "0767156688"


def test_update_user_phone_4(sql_engine: sqlalchemy.engine.Engine) -> None:
    """
    Scenario: Update an user's phone number
    Context: user doesn't exist
    """

    populate_table(sql_engine)

    with sql_engine.begin() as con:
        res = update_phone(
            email="wrong_email@gmail.com", new_phone="0767156688", con=con
        )

        # Check that the user was updated
        stmt = sqlalchemy.select(tables.ClientUsers).where(
            (tables.ClientUsers.email == "wrong_email@gmail.com")
        )
        users_df = pd.read_sql_query(stmt, con)

    assert res == models.UpdatePhoneStatus.USER_NOT_FOUND
    assert users_df.shape[0] == 0


def test_update_user_address_1(sql_engine: sqlalchemy.engine.Engine) -> None:
    """
    Scenario: Update an user's address
    Context: user exists, address is empty
    """

    populate_table(sql_engine)

    with sql_engine.begin() as con:
        res = update_address(email="email@gmail.com", new_address="", con=con)

    assert res == models.UpdateAddressStatus.ADDRESS_IS_NONE


def test_update_user_address_2(sql_engine: sqlalchemy.engine.Engine) -> None:
    """
    Scenario: Update an user's address
    Context: user exists, address is ok
    """

    populate_table(sql_engine)

    with sql_engine.begin() as con:
        res = update_address(
            email="email@gmail.com", new_address="new_address", con=con
        )

        # Check that the user was updated
        stmt = sqlalchemy.select(tables.ClientUsers).where(
            (tables.ClientUsers.email == "email@gmail.com")
        )
        users_df = pd.read_sql_query(stmt, con)

    assert res == models.UpdateAddressStatus.SUCCESS
    assert users_df.shape[0] == 1
    assert users_df.iloc[0]["address"] == "new_address"


def test_update_user_address_3(sql_engine: sqlalchemy.engine.Engine) -> None:
    """
    Scenario: Update an user's address
    Context: user doesn't exist
    """

    populate_table(sql_engine)

    with sql_engine.begin() as con:
        res = update_address(
            email="wrong_email@gmail.com", new_address="new_address", con=con
        )

    assert res == models.UpdateAddressStatus.USER_NOT_FOUND


def test_update_user_city_1(sql_engine: sqlalchemy.engine.Engine) -> None:
    """
    Scenario: Update an user's city
    Context: user exists, city is empty
    """

    populate_table(sql_engine)

    with sql_engine.begin() as con:
        res = update_city(email="email@gmail.com", new_city="", con=con)

    assert res == models.UpdateCityStatus.CITY_IS_NONE


def test_update_user_city_2(sql_engine: sqlalchemy.engine.Engine) -> None:
    """
    Scenario: Update an user's city
    Context: user exists, city is ok
    """

    populate_table(sql_engine)

    with sql_engine.begin() as con:
        res = update_city(email="email@gmail.com", new_city="new_city", con=con)

        # Check that the user was updated
        stmt = sqlalchemy.select(tables.ClientUsers).where(
            (tables.ClientUsers.email == "email@gmail.com")
        )
        users_df = pd.read_sql_query(stmt, con)

    assert res == models.UpdateCityStatus.SUCCESS
    assert users_df.shape[0] == 1
    assert users_df.iloc[0]["city"] == "new_city"


def test_update_user_city_3(sql_engine: sqlalchemy.engine.Engine) -> None:
    """
    Scenario: Update an user's city
    Context: user doesn't exist
    """

    populate_table(sql_engine)

    with sql_engine.begin() as con:
        res = update_city(email="wrong_email@gmail.com", new_city="new_city", con=con)

    assert res == models.UpdateCityStatus.USER_NOT_FOUND


def test_update_user_zip_1(sql_engine: sqlalchemy.engine.Engine) -> None:
    """
    Scenario: Update an user's zip
    Context: user exists, zip is empty
    """

    populate_table(sql_engine)

    with sql_engine.begin() as con:
        res = update_zip(email="email@gmail.com", new_zip="", con=con)

    assert res == models.UpdateZipStatus.ZIP_INVALID


def test_update_user_zip_2(sql_engine: sqlalchemy.engine.Engine) -> None:
    """
    Scenario: Update an user's zip
    Context: user exists, zip is ok
    """

    populate_table(sql_engine)

    with sql_engine.begin() as con:
        res = update_zip(email="email@gmail.com", new_zip="123456", con=con)

        # Check that the user was updated
        stmt = sqlalchemy.select(tables.ClientUsers).where(
            (tables.ClientUsers.email == "email@gmail.com")
        )
        users_df = pd.read_sql_query(stmt, con)

    assert res == models.UpdateZipStatus.SUCCESS
    assert users_df.shape[0] == 1
    assert users_df.iloc[0]["zip"] == "123456"


def test_update_user_zip_3(sql_engine: sqlalchemy.engine.Engine) -> None:
    """
    Scenario: Update an user's zip
    Context: user doesn't exist
    """

    populate_table(sql_engine)

    with sql_engine.begin() as con:
        res = update_zip(email="wrong_email@gmail.com", new_zip="123456", con=con)

    assert res == models.UpdateZipStatus.USER_NOT_FOUND


def test_update_country_1(sql_engine: sqlalchemy.engine.Engine) -> None:
    """
    Scenario: Update an user's country
    Context: user exists, country is ok
    """

    populate_table(sql_engine)

    with sql_engine.begin() as con:
        res = update_country(
            email="email@gmail.com", new_country="new_country", con=con
        )

        # Check that the user was updated
        stmt = sqlalchemy.select(tables.ClientUsers).where(
            (tables.ClientUsers.email == "email@gmail.com")
        )
        users_df = pd.read_sql_query(stmt, con)

    assert res == models.UpdateCountryStatus.SUCCESS
    assert users_df.shape[0] == 1
    assert users_df.iloc[0]["country"] == "new_country"


def test_update_country_2(sql_engine: sqlalchemy.engine.Engine) -> None:
    """
    Scenario: Update an user's country
    Context: user doesn't exist
    """

    populate_table(sql_engine)

    with sql_engine.begin() as con:
        res = update_country(
            email="wrong_email@gmail.com", new_country="new_country", con=con
        )

    assert res == models.UpdateCountryStatus.USER_NOT_FOUND


def test_update_country_3(sql_engine: sqlalchemy.engine.Engine) -> None:
    """
    Scenario: Update an user's country
    Context: user exists, country is empty
    """

    populate_table(sql_engine)

    with sql_engine.begin() as con:
        res = update_country(email="email@gmail.com", new_country="", con=con)

    assert res == models.UpdateCountryStatus.COUNTRY_IS_NONE


def test_update_imgBase64_1(sql_engine: sqlalchemy.engine.Engine) -> None:
    """
    Scenario: Update an user's imgBase64
    Context: user exists, imgBase64 is ok
    """

    populate_table(sql_engine)

    with sql_engine.begin() as con:
        res = update_imgBase64(
            email="email@gmail.com", new_imgBase64="new_imgBase64", con=con
        )

        # Check that the user was updated
        stmt = sqlalchemy.select(tables.ClientUsers).where(
            (tables.ClientUsers.email == "email@gmail.com")
        )
        users_df = pd.read_sql_query(stmt, con)

    assert res == models.UpdateImgStatus.SUCCESS
    assert users_df.shape[0] == 1
    assert users_df.iloc[0]["imgBase64"] == "new_imgBase64"


def test_update_imgBase64_2(sql_engine: sqlalchemy.engine.Engine) -> None:
    """
    Scenario: Update an user's imgBase64
    Context: user doesn't exist
    """

    populate_table(sql_engine)

    with sql_engine.begin() as con:
        res = update_imgBase64(
            email="wrong_email@gmail.com", new_imgBase64="new_imgBase64", con=con
        )

    assert res == models.UpdateImgStatus.USER_NOT_FOUND


def test_update_imgBase64_3(sql_engine: sqlalchemy.engine.Engine) -> None:
    """
    Scenario: Update an user's imgBase64
    Context: user exists, imgBase64 is empty
    """

    populate_table(sql_engine)

    with sql_engine.begin() as con:
        res = update_imgBase64(email="email@gmail.com", new_imgBase64="", con=con)

    assert res == models.UpdateImgStatus.SUCCESS
