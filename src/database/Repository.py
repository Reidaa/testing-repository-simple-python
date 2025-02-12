from urllib.parse import urlparse

from pony import orm

from src.database.BaseRepository import BaseRepository
from src.database.models import db
from src.database.models.User import User
from src.env import env


class DBUserRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        p = urlparse(str(env.DATABASE_URL))

        # db.bind(provider="sqlite", filename="database.sqlite", create_db=True)
        db.bind(
            provider="postgres",
            dbname=p.path[1:],
            user=p.username,
            password=p.password,
            port=p.port,
            host=p.hostname,
        )
        db.generate_mapping(create_tables=True)

    @orm.db_session
    def read(self) -> dict[str, list[str]]:
        users: list[str] = []

        db_user = orm.select(u for u in User)

        for u in db_user:
            users.append(u.username)

        return {
            "users": users,
        }

    @orm.db_session
    def insert(self, username: str) -> None:
        User(username=username)


user_repository = DBUserRepository()
