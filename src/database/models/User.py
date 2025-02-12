from pony import orm

from src.database.models import db


class User(db.Entity):
    username = orm.Required(str)
