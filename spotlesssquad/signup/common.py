import sqlalchemy.engine
from sqlalchemy import insert
from spotlesssquad.common import State

from spotlesssquad.sql.tables import ClientUsers


def signup(username: str, password: str, name: str, email: str, city: str, address: str, country: str, zip: str,
           phone: str, sql_engine: sqlalchemy.engine.Engine) -> bool:
    query = insert(ClientUsers).values(username=username, password=password, name=name, email=email, city=city,
                                       address=address, country=country, zip=zip, phone=phone)

    with sql_engine.begin() as con:
        result = con.execute(query)
        con.commit()
    return result.fetchone() is not None
