import sqlalchemy

from spotlesssquad.sql import tables


def update_name(email: str, new_name: str, con: sqlalchemy.Connection) -> None:
    """
    Update user for the given email.
    """

    stmt = (
        sqlalchemy.update(tables.ClientUsers)
        .where(tables.ClientUsers.email == email)
        .values({
            tables.ClientUsers.name: new_name,
        })
    )

    con.execute(stmt)
