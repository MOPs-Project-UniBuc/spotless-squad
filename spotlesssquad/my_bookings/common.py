import pandas as pd
import sqlalchemy
import sqlalchemy.engine


def get_all_bookings(
    username: str, sql_engine: sqlalchemy.engine.Engine
) -> pd.DataFrame:
    query = sqlalchemy.text(
        f"""
        SELECT CleanServiceProviders.name AS providerName, CleanServiceProvidersBookings.date
        FROM CleanServiceProvidersBookings
        INNER JOIN CleanServiceProviders
        ON CleanServiceProviders.id = CleanServiceProvidersBookings.provider_id
        INNER JOIN ClientUsers
        ON ClientUsers.id = CleanServiceProvidersBookings.client_id
        WHERE ClientUsers.username = '{username}'
        ORDER BY CleanServiceProvidersBookings.date DESC
    """
    )
    with sql_engine.begin() as con:
        df = pd.read_sql(query, con)

    # Set Status as
    # - "Done" if the booking is in the past
    # - "Pending" if the booking is in the future
    # - "In progress" if the booking is today
    df["Status"] = pd.to_datetime(df["date"]).apply(
        lambda date: "Done"
        if date < pd.Timestamp.now()
        else "In progress"
        if date.date() == pd.Timestamp.now().date()
        else "Pending"
    )

    df = df.rename(
        columns={
            "providerName": "Nume provider",
            "date": "Data",
        }
    )

    return df
