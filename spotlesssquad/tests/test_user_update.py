import pandas as pd
import sqlalchemy

from spotlesssquad.settings import models
from spotlesssquad.settings.common import update_name, update_password
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


def test_update_user_1(sql_engine: sqlalchemy.engine.Engine):
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


def test_update_user_2(sql_engine: sqlalchemy.engine.Engine):
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


def test_update_user_3(sql_engine: sqlalchemy.engine.Engine):
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


def test_update_user_4(sql_engine: sqlalchemy.engine.Engine):
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


def test_update_user_5(sql_engine: sqlalchemy.engine.Engine):
    """
    Scenario: Update an user's password
    Context: user exists, password too short
    """

    populate_table(sql_engine)

    with sql_engine.begin() as con:
        res = update_password(email="email@gmail.com", new_password="passw", con=con)

    assert res == models.UpdatePasswordStatus.PASSWORD_TOO_SHORT
