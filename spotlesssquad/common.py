import pandas as pd
import sqlalchemy
import sqlalchemy.engine
import streamlit as st

from spotlesssquad import models
from spotlesssquad.sql.tables import ClientUsers


class State:
    def __init__(self) -> None:
        sql_engine = st.session_state.get("sql_engine", None)

        self.sql_engine: sqlalchemy.engine.Engine

        if sql_engine is not None:
            self.sql_engine = sql_engine
        else:
            path = "sqlite:///spotlesssquad/SpotlessSquad.db"
            self.sql_engine = sqlalchemy.create_engine(path)


def get_user_details(
    username: str,
    sql_engine: sqlalchemy.engine.Engine,
) -> models.ClientUsers:
    with sql_engine.begin() as con:
        query = sqlalchemy.select(ClientUsers).where(ClientUsers.username == username)
        user_df = pd.read_sql(query, con)

    entry = user_df.to_dict(orient="records")[0]

    return models.ClientUsers(**entry)  # type: ignore


def get_state() -> State:
    if "state" not in st.session_state:
        print("WARNING: new state created")
        st.session_state["state"] = State()

    return st.session_state["state"]
