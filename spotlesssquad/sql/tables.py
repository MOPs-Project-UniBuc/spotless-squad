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


def create_client_users_table(con: sqlalchemy.engine.Engine) -> None:
    # CREATE CLIENT USERS TABLE
    ClientUsers.__table__.create(con)


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


def create_clean_service_providers_table(con: sqlalchemy.engine.Engine) -> None:
    # CREATE CLEAN SERVICE PROVIDERS TABLE
    CleanServiceProviders.__table__.create(con)
