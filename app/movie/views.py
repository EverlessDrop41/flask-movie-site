from models import Movie, Genre
from flask import jsonify, Blueprint
import peewee

movies_bp = Blueprint('movies', 'movies_bp')


@movies_bp.route("/api/movies/")
def getMovies():
    movies = []

    sel_mov = Movie.select()

    for mov in sel_mov:
        movies.append(mov.__dict__['_data'])

    return jsonify(movies)


@movies_bp.route("/api/movies/<int:id>")
def getMovie(id):
    try:
        movie = Movie.select().where(Movie.id == id).dicts().get()
        return jsonify(movie)
    except peewee.DoesNotExist:
        return jsonify({'error': 'Movie not found'})


@movies_bp.route("/api/genres/")
def getGenres():
    genres = []

    for g in Genre.select():
        genres.append(g.__dict__['_data'])

    return jsonify(genres)


@movies_bp.route("/api/genres/<int:id>")
def getGenre(id):
    try:
        genre = Genre.select().where(Genre.id == id).dicts().get()
        return jsonify(genre)
    except peewee.DoesNotExist:
        return jsonify({'error': 'Movie not found'})
