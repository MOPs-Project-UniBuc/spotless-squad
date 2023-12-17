import datetime

import pandas as pd
import sqlalchemy
import sqlalchemy.engine

from spotlesssquad.booking import models
from spotlesssquad.sql import tables


def get_unique_service_types(
    sql_engine: sqlalchemy.engine.Engine,
) -> list[str]:
    query = sqlalchemy.select(tables.CleanServiceProviders.cleanServiceType).distinct()

    with sql_engine.begin() as con:
        df = pd.read_sql(query, con)

    return df["cleanServiceType"].tolist()


def get_all_providers(
    username: str,
    sql_engine: sqlalchemy.engine.Engine,
) -> pd.DataFrame:
    if username == "admin":
        query = sqlalchemy.select(tables.CleanServiceProviders)
    else:
        query = sqlalchemy.select(
            tables.CleanServiceProviders.name,
            tables.CleanServiceProviders.email,
            tables.CleanServiceProviders.cleanServiceType,
            tables.CleanServiceProviders.zip,
        )

    with sql_engine.begin() as con:
        df = pd.read_sql(query, con)

    df = df.rename(
        columns={
            "name": "Nume",
            "email": "Email",
            "cleanServiceType": "Tip serviciu",
            "zip": "Cod postal",
        }
    )

    return df


def filter_provider_by_type(fitlers: list[str], df: pd.DataFrame) -> pd.DataFrame:
    return df[df["Tip serviciu"].isin(fitlers)]


def filter_providers_by_name(name: str, df: pd.DataFrame) -> pd.DataFrame:
    df_temp = df["Nume"].str.lower()
    name = name.lower()

    return df[df_temp.str.contains(name)]


def book_provider(
    username: str,
    provider_name: str,
    date: datetime.date,
    sql_engine: sqlalchemy.engine.Engine,
) -> models.BookingStatus:
    query = sqlalchemy.select(tables.CleanServiceProviders).where(
        tables.CleanServiceProviders.name == provider_name
    )

    with sql_engine.begin() as con:
        provider_df = pd.read_sql(query, con)

    if len(provider_df) == 0:
        return models.BookingStatus.PROVIDER_NOT_FOUND

    provider_id = int(provider_df["id"].iloc[0])

    query = (
        sqlalchemy.select(tables.CleanServiceProvidersBookings)
        .where(tables.CleanServiceProvidersBookings.provider_id == provider_id)
        .where(tables.CleanServiceProvidersBookings.date == date)
    )

    with sql_engine.begin() as con:
        bookings_df = pd.read_sql(query, con)

    if len(bookings_df) > 0:
        return models.BookingStatus.PROVIDER_NOT_AVAILABLE

    query = sqlalchemy.select(tables.ClientUsers).where(
        tables.ClientUsers.username == username
    )

    with sql_engine.begin() as con:
        user_df = pd.read_sql(query, con)

    user_id = int(user_df["id"].iloc[0])

    insert_stmt = sqlalchemy.insert(tables.CleanServiceProvidersBookings).values(
        [
            {
                "client_id": user_id,
                "provider_id": provider_id,
                "date": date,
            }
        ]
    )

    with sql_engine.begin() as con:
        con.execute(insert_stmt)

    return models.BookingStatus.SUCCESS
