import datetime

import sqlalchemy
import sqlalchemy.orm


class Base(sqlalchemy.orm.DeclarativeBase):  # type: ignore
    pass


class ClientUsers(Base):
    __tablename__ = "ClientUsers"

    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, index=True, unique=True
    )
    name = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
    username = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
    password = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
    email = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
    phone = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
    address = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
    city = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
    zip = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
    country = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now())
    imgBase64 = sqlalchemy.Column(sqlalchemy.Text)


def create_client_users_table(sql_engine: sqlalchemy.engine.Engine) -> None:
    # CREATE CLIENT USERS TABLE
    with sql_engine.begin() as con:
        create = sqlalchemy.text(
            """CREATE TABLE IF NOT EXISTS ClientUsers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            address TEXT NOT NULL,
            city TEXT NOT NULL,
            zip TEXT NOT NULL,
            country TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            imgBase64 TEXT
        )"""
        )
        con.execute(create)


def drop_client_users_table(sql_engine: sqlalchemy.engine.Engine) -> None:
    # DROP CLIENT USERS TABLE
    with sql_engine.begin() as con:
        drop = sqlalchemy.text("DROP TABLE IF EXISTS ClientUsers")
        con.execute(drop)


class CleanServiceProviders(Base):
    __tablename__ = "CleanServiceProviders"

    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, index=True, unique=True
    )
    name = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
    username = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
    password = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
    email = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
    phone = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
    address = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
    city = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
    zip = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
    country = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now())
    cleanServiceType = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
    imgBase64 = sqlalchemy.Column(sqlalchemy.Text)


def create_clean_service_providers_table(sql_engine: sqlalchemy.engine.Engine) -> None:
    # CREATE CLEAN SERVICE PROVIDERS TABLE
    with sql_engine.begin() as con:
        create = sqlalchemy.text(
            """CREATE TABLE IF NOT EXISTS CleanServiceProviders (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            address TEXT NOT NULL,
            city TEXT NOT NULL,
            zip TEXT NOT NULL,
            country TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            cleanServiceType TEXT NOT NULL,
            imgBase64 TEXT
        )"""
        )
        con.execute(create)


def drop_clean_service_providers_table(sql_engine: sqlalchemy.engine.Engine) -> None:
    # DROP CLEAN SERVICE PROVIDERS TABLE
    with sql_engine.begin() as con:
        drop = sqlalchemy.text("DROP TABLE IF EXISTS CleanServiceProviders")
        con.execute(drop)


class CleanServiceProvidersBookings(Base):
    __tablename__ = "CleanServiceProvidersBookings"

    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, index=True, unique=True
    )
    client_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    provider_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    date = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now())


def create_clean_service_providers_bookings_table(
    sql_engine: sqlalchemy.engine.Engine,
) -> None:
    # CREATE CLEAN SERVICE PROVIDERS BOOKINGS TABLE
    with sql_engine.begin() as con:
        create = sqlalchemy.text(
            """CREATE TABLE IF NOT EXISTS CleanServiceProvidersBookings (
            id INTEGER PRIMARY KEY,
            client_id INTEGER NOT NULL,
            provider_id INTEGER NOT NULL,
            date TIMESTAMP NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )"""
        )
        con.execute(create)


def drop_clean_service_providers_bookings_table(
    sql_engine: sqlalchemy.engine.Engine,
) -> None:
    # DROP CLEAN SERVICE PROVIDERS BOOKINGS TABLE
    with sql_engine.begin() as con:
        drop = sqlalchemy.text("DROP TABLE IF EXISTS CleanServiceProvidersBookings")
        con.execute(drop)
