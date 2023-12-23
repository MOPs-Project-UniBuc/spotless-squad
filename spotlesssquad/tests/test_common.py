import os
import random
import string
from typing import Generator

import pytest
import sqlalchemy
from streamlit.testing.v1 import AppTest

from spotlesssquad.sql import tables


@pytest.fixture()
def sql_engine() -> sqlalchemy.engine.Engine:
    # open in-memory database
    engine = sqlalchemy.create_engine("sqlite:///:memory:", echo=True)

    # create tables
    tables.create_client_users_table(engine)
    tables.create_clean_service_providers_table(engine)

    return engine


@pytest.fixture()
def sql_engine_app() -> Generator[sqlalchemy.engine.Engine, None, None]:
    # create database
    random.seed(random.randint(0, 1000))
    random_string = "".join(random.choices(string.ascii_lowercase, k=10))
    print(f"random_string: {random_string}")
    db_name = f"{random_string}.db"
    engine = sqlalchemy.create_engine(
        f"sqlite:///{db_name}?cache=shared&mode=memory",
        echo=True,
    )

    # DROP TABLES
    tables.drop_client_users_table(engine)
    tables.drop_clean_service_providers_table(engine)

    # create tables
    tables.create_client_users_table(engine)
    tables.create_clean_service_providers_table(engine)

    yield engine

    # delete database
    os.remove(db_name)


@pytest.fixture()
def at(sql_engine_app: sqlalchemy.engine.Engine) -> AppTest:
    at = AppTest.from_file("spotlesssquad/app/main.py", default_timeout=60)
    at.session_state["sql_engine"] = sql_engine_app
    at.run()

    return at
