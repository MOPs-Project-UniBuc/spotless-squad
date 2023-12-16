import sqlalchemy
import sqlalchemy.engine

from spotlesssquad.sql.tables import ClientUsers


def login(username: str, password: str, sql_engine: sqlalchemy.engine.Engine) -> bool:
    query = sqlalchemy.select(ClientUsers).where(
        sqlalchemy.and_(
            ClientUsers.username == username, ClientUsers.password == password
        )
    )
    with sql_engine.begin() as con:
        result = con.execute(query)

    return result.fetchone() is not None
