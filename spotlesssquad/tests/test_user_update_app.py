import pandas as pd
import sqlalchemy
import sqlalchemy.engine
from streamlit.testing.v1 import AppTest


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
                "password": "admin",
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


def test_settings_1(at: AppTest, sql_engine_app: sqlalchemy.engine.Engine) -> None:
    """
    Scenario: User enters valid credentials
    """

    users_df = pd.DataFrame(
        [
            {
                "name": "name",
                "username": "admin",
                "password": "admin",
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

    assert at.sidebar.radio[0].value == "Settings"

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

    at.button[0].click().run()

    # check that the values are updated
    with sql_engine_app.begin() as con:
        users_df = pd.read_sql_table("ClientUsers", con)

    assert users_df["name"][0] == "name1"
    assert users_df["phone"][0] == "0767156688"
