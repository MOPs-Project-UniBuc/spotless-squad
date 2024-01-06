import hashlib

import pandas as pd
import sqlalchemy
import sqlalchemy.engine
from streamlit.testing.v1 import AppTest

from spotlesssquad.signup.common import signup_client, signup_clean_provider
from spotlesssquad.sql import tables


def test_login_1(at: AppTest) -> None:
    """
    Scenario: User enters invalid credentials
    """

    # check that the login page is rendered
    assert at.title[0].value == "SpotlessSquad"
    assert at.text_input[0].label == "Username"
    assert at.text_input[1].label == "Password"
    assert at.button[0].label == "Login"

    # enter invalid credentials
    at.text_input[0].input("user1").run()
    at.text_input[1].input("pass1").run()
    at.button[0].click().run()

    # check that the login page is rendered again
    assert at.error[0].value == "The username or password you have entered is invalid."


def test_login_2(at: AppTest, sql_engine_app: sqlalchemy.engine.Engine) -> None:
    """
    Scenario: User enters valid credentials
    """

    users_df = pd.DataFrame(
        [
            {
                "name": "name",
                "username": "admin",
                "password": hashlib.sha256("admin".encode()).hexdigest(),
                "email": "admin@gmail.com",
                "phone": "0767158866",
                "address": "address",
                "city": "city",
                "zip": "zip",
                "country": "country",
                "imgBase64": "",
            },
        ]
    )
    with sql_engine_app.begin() as con:
        users_df.to_sql("ClientUsers", con, if_exists="append", index=False)

    at.text_input[0].input("admin").run()
    at.text_input[1].input("admin").run()
    at.button[0].click().run()

    assert at.sidebar.title[0].value == "SpotlessSquad"


def test_settings_1(at: AppTest, sql_engine_app: sqlalchemy.engine.Engine) -> None:
    """
    Scenario: User enters valid credentials
    """

    users_df = pd.DataFrame(
        [
            {
                "name": "name",
                "username": "admin",
                "password": hashlib.sha256("admin".encode()).hexdigest(),
                "email": "admin@gmail.com",
                "phone": "0767158866",
                "address": "address",
                "city": "city",
                "zip": "zip",
                "country": "country",
                "imgBase64": "",
            },
        ]
    )
    with sql_engine_app.begin() as con:
        users_df.to_sql("ClientUsers", con, if_exists="append", index=False)

    at.text_input[0].input("admin").run()
    at.text_input[1].input("admin").run()
    at.button[0].click().run()

    assert at.sidebar.title[0].value == "SpotlessSquad"

    at.sidebar.radio[0].set_value("Settings").run()

    assert at.header[0].value == "Settings"

    assert at.text_input[0].label == "Name"
    assert at.text_input[1].label == "Username"
    assert at.text_input[2].label == "Email"
    assert at.text_input[3].label == "Password"
    assert at.text_input[4].label == "Phone"
    assert at.text_input[5].label == "Address"
    assert at.text_input[6].label == "City"
    assert at.text_input[7].label == "Country"
    assert at.text_input[8].label == "ZIP Code"

    assert at.button[0].label == "Save"

    at.text_input[0].input("name1").run()
    at.text_input[4].input("0767156688").run()
    at.text_input[5].input("new_address").run()
    at.text_input[6].input("new_city").run()
    at.text_input[7].input("new_country").run()
    at.text_input[8].input("123321").run()

    at.button[0].click().run()

    # check that the values are updated
    with sql_engine_app.begin() as con:
        users_df = pd.read_sql_table("ClientUsers", con)

    assert users_df["name"][0] == "name1"
    assert users_df["phone"][0] == "0767156688"


def test_settings_2(at: AppTest, sql_engine_app: sqlalchemy.engine.Engine) -> None:
    """
    Scenario: User enters valid credentials
    Insert invalid values
    """

    users_df = pd.DataFrame(
        [
            {
                "name": "name",
                "username": "admin",
                "password": hashlib.sha256("admin".encode()).hexdigest(),
                "email": "admin@gmail.com",
                "phone": "0767158866",
                "address": "address",
                "city": "city",
                "zip": "zip",
                "country": "country",
                "imgBase64": "",
            },
        ]
    )
    with sql_engine_app.begin() as con:
        users_df.to_sql("ClientUsers", con, if_exists="append", index=False)

    at.text_input[0].input("admin").run()
    at.text_input[1].input("admin").run()
    at.button[0].click().run()

    assert at.sidebar.title[0].value == "SpotlessSquad"

    at.sidebar.radio[0].set_value("Settings").run()

    assert at.header[0].value == "Settings"

    assert at.text_input[0].label == "Name"
    assert at.text_input[1].label == "Username"
    assert at.text_input[2].label == "Email"
    assert at.text_input[3].label == "Password"
    assert at.text_input[4].label == "Phone"
    assert at.text_input[5].label == "Address"
    assert at.text_input[6].label == "City"
    assert at.text_input[7].label == "Country"
    assert at.text_input[8].label == "ZIP Code"

    assert at.button[0].label == "Save"

    at.text_input[4].input("076715668").run()

    at.button[0].click().run()

    assert at.error[0].value == "Failed to update phone"


def test_settings_3(at: AppTest, sql_engine_app: sqlalchemy.engine.Engine) -> None:
    """
    Scenario: User enters valid credentials
    Insert invalid values
    """

    users_df = pd.DataFrame(
        [
            {
                "name": "name",
                "username": "admin",
                "password": hashlib.sha256("admin".encode()).hexdigest(),
                "email": "admin@gmail.com",
                "phone": "0767158866",
                "address": "address",
                "city": "city",
                "zip": "zip",
                "country": "country",
                "imgBase64": "",
            },
        ]
    )
    with sql_engine_app.begin() as con:
        users_df.to_sql("ClientUsers", con, if_exists="append", index=False)

    at.text_input[0].input("admin").run()
    at.text_input[1].input("admin").run()
    at.button[0].click().run()

    assert at.sidebar.title[0].value == "SpotlessSquad"

    at.sidebar.radio[0].set_value("Settings").run()

    assert at.header[0].value == "Settings"

    assert at.text_input[0].label == "Name"
    assert at.text_input[1].label == "Username"
    assert at.text_input[2].label == "Email"
    assert at.text_input[3].label == "Password"
    assert at.text_input[4].label == "Phone"
    assert at.text_input[5].label == "Address"
    assert at.text_input[6].label == "City"
    assert at.text_input[7].label == "Country"
    assert at.text_input[8].label == "ZIP Code"

    assert at.button[0].label == "Save"

    at.text_input[5].input("").run()

    at.button[0].click().run()

    assert at.error[0].value == "Failed to update address"


def test_settings_4(at: AppTest, sql_engine_app: sqlalchemy.engine.Engine) -> None:
    """
    Scenario: User enters valid credentials
    Insert invalid values
    """

    users_df = pd.DataFrame(
        [
            {
                "name": "name",
                "username": "admin",
                "password": hashlib.sha256("admin".encode()).hexdigest(),
                "email": "admin@gmail.com",
                "phone": "0767158866",
                "address": "address",
                "city": "city",
                "zip": "zip",
                "country": "country",
                "imgBase64": "",
            },
        ]
    )
    with sql_engine_app.begin() as con:
        users_df.to_sql("ClientUsers", con, if_exists="append", index=False)

    at.text_input[0].input("admin").run()
    at.text_input[1].input("admin").run()
    at.button[0].click().run()

    assert at.sidebar.title[0].value == "SpotlessSquad"

    at.sidebar.radio[0].set_value("Settings").run()

    assert at.header[0].value == "Settings"

    assert at.text_input[0].label == "Name"
    assert at.text_input[1].label == "Username"
    assert at.text_input[2].label == "Email"
    assert at.text_input[3].label == "Password"
    assert at.text_input[4].label == "Phone"
    assert at.text_input[5].label == "Address"
    assert at.text_input[6].label == "City"
    assert at.text_input[7].label == "Country"
    assert at.text_input[8].label == "ZIP Code"

    assert at.button[0].label == "Save"

    at.text_input[0].input("").run()

    at.button[0].click().run()

    assert at.error[0].value == "Failed to update name"


def test_settings_5(at: AppTest, sql_engine_app: sqlalchemy.engine.Engine) -> None:
    """
    Scenario: User enters valid credentials
    Insert invalid values
    """

    users_df = pd.DataFrame(
        [
            {
                "name": "name",
                "username": "admin",
                "password": hashlib.sha256("admin".encode()).hexdigest(),
                "email": "admin@gmail.com",
                "phone": "0767158866",
                "address": "address",
                "city": "city",
                "zip": "zip",
                "country": "country",
                "imgBase64": "",
            },
        ]
    )
    with sql_engine_app.begin() as con:
        users_df.to_sql("ClientUsers", con, if_exists="append", index=False)

    at.text_input[0].input("admin").run()
    at.text_input[1].input("admin").run()
    at.button[0].click().run()

    assert at.sidebar.title[0].value == "SpotlessSquad"

    at.sidebar.radio[0].set_value("Settings").run()

    assert at.header[0].value == "Settings"

    assert at.text_input[0].label == "Name"
    assert at.text_input[1].label == "Username"
    assert at.text_input[2].label == "Email"
    assert at.text_input[3].label == "Password"
    assert at.text_input[4].label == "Phone"
    assert at.text_input[5].label == "Address"
    assert at.text_input[6].label == "City"
    assert at.text_input[7].label == "Country"
    assert at.text_input[8].label == "ZIP Code"

    assert at.button[0].label == "Save"

    at.text_input[6].input("").run()

    at.button[0].click().run()

    assert at.error[0].value == "Failed to update city"


def test_settings_6(at: AppTest, sql_engine_app: sqlalchemy.engine.Engine) -> None:
    """
    Scenario: User enters valid credentials
    Insert invalid values
    """

    users_df = pd.DataFrame(
        [
            {
                "name": "name",
                "username": "admin",
                "password": hashlib.sha256("admin".encode()).hexdigest(),
                "email": "admin@gmail.com",
                "phone": "0767158866",
                "address": "address",
                "city": "city",
                "zip": "zip",
                "country": "country",
                "imgBase64": "",
            },
        ]
    )
    with sql_engine_app.begin() as con:
        users_df.to_sql("ClientUsers", con, if_exists="append", index=False)

    # enter invalid credentials
    at.text_input[0].input("admin").run()
    at.text_input[1].input("admin").run()
    at.button[0].click().run()

    assert at.sidebar.title[0].value == "SpotlessSquad"

    at.sidebar.radio[0].set_value("Settings").run()

    assert at.header[0].value == "Settings"

    assert at.text_input[0].label == "Name"
    assert at.text_input[1].label == "Username"
    assert at.text_input[2].label == "Email"
    assert at.text_input[3].label == "Password"
    assert at.text_input[4].label == "Phone"
    assert at.text_input[5].label == "Address"
    assert at.text_input[6].label == "City"
    assert at.text_input[7].label == "Country"
    assert at.text_input[8].label == "ZIP Code"

    assert at.button[0].label == "Save"

    at.text_input[7].input("").run()

    at.button[0].click().run()

    assert at.error[0].value == "Failed to update country"


def test_settings_7(at: AppTest, sql_engine_app: sqlalchemy.engine.Engine) -> None:
    """
    Scenario: User enters valid credentials
    Insert invalid values
    """

    users_df = pd.DataFrame(
        [
            {
                "name": "name",
                "username": "admin",
                "password": hashlib.sha256("admin".encode()).hexdigest(),
                "email": "admin@gmail.com",
                "phone": "0767158866",
                "address": "address",
                "city": "city",
                "zip": "zip",
                "country": "country",
                "imgBase64": "",
            },
        ]
    )
    with sql_engine_app.begin() as con:
        users_df.to_sql("ClientUsers", con, if_exists="append", index=False)

    # enter invalid credentials
    at.text_input[0].input("admin").run()
    at.text_input[1].input("admin").run()
    at.button[0].click().run()

    assert at.sidebar.title[0].value == "SpotlessSquad"

    at.sidebar.radio[0].set_value("Settings").run()

    assert at.header[0].value == "Settings"

    assert at.text_input[0].label == "Name"
    assert at.text_input[1].label == "Username"
    assert at.text_input[2].label == "Email"
    assert at.text_input[3].label == "Password"
    assert at.text_input[4].label == "Phone"
    assert at.text_input[5].label == "Address"
    assert at.text_input[6].label == "City"
    assert at.text_input[7].label == "Country"
    assert at.text_input[8].label == "ZIP Code"

    assert at.button[0].label == "Save"

    at.text_input[8].input("").run()

    at.button[0].click().run()

    assert at.error[0].value == "Failed to update zip"


def test_logout_1(at: AppTest, sql_engine_app: sqlalchemy.engine.Engine) -> None:
    """
    Scenario: Log in and Log out
    """

    users_df = pd.DataFrame(
        [
            {
                "name": "name",
                "username": "admin",
                "password": hashlib.sha256("admin".encode()).hexdigest(),
                "email": "admin@gmail.com",
                "phone": "0767158866",
                "address": "address",
                "city": "city",
                "zip": "zip",
                "country": "country",
                "imgBase64": "",
            },
        ]
    )
    with sql_engine_app.begin() as con:
        users_df.to_sql("ClientUsers", con, if_exists="append", index=False)

    at.text_input[0].input("admin").run()
    at.text_input[1].input("admin").run()
    at.button[0].click().run()

    assert at.sidebar.title[0].value == "SpotlessSquad"

    at.sidebar.button[0].label = "Logout"
    at.sidebar.button[0].click().run()

    assert at.title[0].value == "SpotlessSquad"


def test_signup_1(at: AppTest, sql_engine: sqlalchemy.engine.Engine) -> None:
    """
    Scenario: User does not already exist in database
    """

    test1 = signup_client(
        "nameclient",
        "123",
        "nameclient",
        "test@test.com",
        "city",
        "adresa",
        "country",
        "zip",
        "0735454311",
        sql_engine,
    )
    test2 = signup_clean_provider(
        "nameclean",
        "123",
        "nameclean",
        "test@test.com",
        "city",
        "adresa",
        "country",
        "zip",
        "0735454311",
        "service",
        sql_engine,
    )

    assert test1 is True
    assert test2 is True


def test_signup_2(at: AppTest, sql_engine: sqlalchemy.engine.Engine) -> None:
    """
    Scenario: User does  already exist in database
    """
    test1 = signup_client(
        "nameclient",
        "123",
        "nameclient",
        "test@test.com",
        "city",
        "adresa",
        "country",
        "zip",
        "0735454311",
        sql_engine,
    )
    test2 = signup_clean_provider(
        "nameclean",
        "123",
        "nameclean",
        "test@test.com",
        "city",
        "adresa",
        "country",
        "zip",
        "0735454311",
        "service",
        sql_engine,
    )

    test1 = signup_client(
        "nameclient",
        "123",
        "nameclient",
        "test@test.com",
        "city",
        "adresa",
        "country",
        "zip",
        "0735454311",
        sql_engine,
    )
    test2 = signup_clean_provider(
        "nameclean",
        "123",
        "nameclean",
        "test@test.com",
        "city",
        "adresa",
        "country",
        "zip",
        "0735454311",
        "service",
        sql_engine,
    )

    assert test1 is False
    assert test2 is False
