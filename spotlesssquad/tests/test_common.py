import sqlite3

import pytest
import sqlalchemy

from spotlesssquad.sql import tables


@pytest.fixture()
def sql_engine() -> sqlite3.Connection:
    # open in-memory database
    engine = sqlalchemy.create_engine("sqlite:///:memory:", echo=True)

    # create tables
    tables.create_client_users_table(engine)
    tables.create_clean_service_providers_table(engine)

    return engine
