import hashlib

import pandas as pd
import sqlalchemy.engine
from sqlalchemy import insert

from spotlesssquad.sql.tables import ClientUsers


def signup(
    username: str,
    password: str,
    name: str,
    email: str,
    city: str,
    address: str,
    country: str,
    zip: str,
    phone: str,
    sql_engine: sqlalchemy.engine.Engine,
) -> bool:
    query_user = sqlalchemy.select(ClientUsers).where(ClientUsers.username == username)
    with sql_engine.begin() as con:
        user_df = pd.read_sql(query_user, con)

    if not user_df.empty:
        return False

    query = insert(ClientUsers).values(
        [
            {
                "username": username,
                "password": hashlib.sha256(password.encode()).hexdigest(),
                "name": name,
                "email": email,
                "city": city,
                "address": address,
                "country": country,
                "zip": zip,
                "phone": phone,
            }
        ]
    )

    with sql_engine.begin() as con:
        result = con.execute(query)

    return result.rowcount == 1
