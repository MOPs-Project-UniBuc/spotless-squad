import pandas as pd
import sqlalchemy

from spotlesssquad.settings.common import update_name
from spotlesssquad.sql import tables


def test_update_user_1(sql_engine: sqlalchemy.engine.Engine):
    """
    Scenario: Update an user
    Context: user exists
    """

    # INSERT CLIENT USER
    # Populate ClientUsers Table
    users_df = pd.DataFrame(
        [
            (
                "name",
                "username",
                "password",
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

        update_name(email="email@gmail.com", new_name="new_user", con=con)

        # Check that the user was updated
        stmt = sqlalchemy.select(tables.ClientUsers).where(
            tables.ClientUsers.name == "new_user"
        )

        users_df = pd.read_sql_query(stmt, con)

    assert users_df.shape[0] == 1
    assert users_df.iloc[0]["name"] == "new_user"


def test_update_user_2(sql_engine: sqlalchemy.engine.Engine):
    """
    Scenario: Update an user
    Context: user exists
    """

    # INSERT CLIENT USER
    # Populate ClientUsers Table
    users_df = pd.DataFrame(
        [
            (
                "name",
                "username",
                "password",
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

        update_name(email="wrong_email@gmail.com", new_name="new_user", con=con)

        # Check that the user was updated
        stmt = sqlalchemy.select(tables.ClientUsers).where(
            (tables.ClientUsers.name == "new_user")
        )
        users_df = pd.read_sql_query(stmt, con)

    assert users_df.shape[0] == 0
