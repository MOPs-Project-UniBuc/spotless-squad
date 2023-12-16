import pandas as pd
import sqlalchemy

from spotlesssquad.settings import models
from spotlesssquad.settings.common import update_name, update_password, update_phone
from spotlesssquad.sql import tables


def populate_table(sql_engine: sqlalchemy.engine.Engine):
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


def test_update_user_name_1(sql_engine: sqlalchemy.engine.Engine):
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

    assert res == models.UpdateStatus.SUCCESS
    assert users_df.shape[0] == 1
    assert users_df.iloc[0]["name"] == "new_user"


def test_update_user_name_2(sql_engine: sqlalchemy.engine.Engine):
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

    assert res == models.UpdateStatus.USER_NOT_FOUND
    assert users_df.shape[0] == 0


def test_update_user_password_1(sql_engine: sqlalchemy.engine.Engine):
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


def test_update_user_password_2(sql_engine: sqlalchemy.engine.Engine):
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

    assert res == models.UpdateStatus.USER_NOT_FOUND
    assert users_df.shape[0] == 0


def test_update_user_password_3(sql_engine: sqlalchemy.engine.Engine):
    """
    Scenario: Update an user's password
    Context: user exists, password too short
    """

    populate_table(sql_engine)

    with sql_engine.begin() as con:
        res = update_password(email="email@gmail.com", new_password="passw", con=con)

    assert res == models.UpdatePasswordStatus.PASSWORD_TOO_SHORT


def test_update_user_phone_1(sql_engine: sqlalchemy.engine.Engine):
    """
    Scenario: Update an user's phone number
    Context: user exists, phone number too short
    """

    populate_table(sql_engine)

    with sql_engine.begin() as con:
        res = update_phone(email="email@gmail.com", new_phone="076715", con=con)

    assert res == models.UpdatePhoneStatus.NUMBER_TOO_SHORT


def test_update_user_phone_2(sql_engine: sqlalchemy.engine.Engine):
    """
    Scenario: Update an user's phone number
    Context: user exists, phone number too short
    """

    populate_table(sql_engine)

    with sql_engine.begin() as con:
        res = update_phone(email="email@gmail.com", new_phone="07671588667", con=con)

    assert res == models.UpdatePhoneStatus.NUMBER_TOO_LONG


def test_update_user_phone_3(sql_engine: sqlalchemy.engine.Engine):
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


def test_update_user_phone_4(sql_engine: sqlalchemy.engine.Engine):
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
