import hashlib

import pandas as pd
import sqlalchemy.engine
from sqlalchemy import insert

from spotlesssquad.sql import tables


def signup_client(
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
    query_user = sqlalchemy.select(tables.ClientUsers).where(
        tables.ClientUsers.username == username
    )
    with sql_engine.begin() as con:
        user_df = pd.read_sql(query_user, con)

    if not user_df.empty:
        return False

    query = insert(tables.ClientUsers).values(
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


def signup_clean_provider(
    username: str,
    password: str,
    name: str,
    email: str,
    city: str,
    address: str,
    country: str,
    zip: str,
    phone: str,
    service_type: str,
    sql_engine: sqlalchemy.engine.Engine,
) -> bool:
    query_user = sqlalchemy.select(tables.CleanServiceProviders).where(
        tables.CleanServiceProviders.username == username
    )
    with sql_engine.begin() as con:
        user_df = pd.read_sql(query_user, con)

    if not user_df.empty:
        return False

    query = insert(tables.CleanServiceProviders).values(
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
                "cleanServiceType": service_type,
            }
        ]
    )

    with sql_engine.begin() as con:
        result = con.execute(query)

    return result.rowcount == 1


def get_service_types(sql_engine: sqlalchemy.engine.Engine) -> list[str]:
    query = sqlalchemy.select(tables.CleanServiceProviders.cleanServiceType).distinct()
    with sql_engine.begin() as con:
        result = con.execute(query)

    return [row[0] for row in result]
