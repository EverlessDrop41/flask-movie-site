from database import DATABASE as db
from flask import Flask, g
from movie.models import Movie, Genre
from movie.views import movies_bp

tables = [Movie, Genre]

db.connect()

for table in tables:
    print(table)
    try:
        db.create_table(table)
    except:
        continue

db.close()

server = Flask(__name__)
server.register_blueprint(movies_bp)


@server.before_request
def before_request():
    g.db = db
    g.db.connect()


@server.after_request
def after_request(response):
    g.db.close()
    return response
