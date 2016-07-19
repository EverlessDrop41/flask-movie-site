from app.database import DATABASE
from peewee import *


class Genre(Model):
    id = PrimaryKeyField()
    name = CharField()

    class Meta:
        database = DATABASE
        db_table = "TBL_GENRES"

class Movie(Model):
    id = PrimaryKeyField()
    name = CharField()
    release_date = DateField()
    genre = ForeignKeyField(Genre)

    class Meta:
        database = DATABASE
        db_table = "TBL_MOVIES"