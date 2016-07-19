from datetime import date

from app.database import DATABASE as db
from app.movie.models import Genre
from app.movie.models import Movie

if __name__ == '__main__':
    db.connect()

    sci_fi = Genre(name='Science Fiction')
    sci_fi.save()
    adv = Genre(name='Adventure')
    adv.save()
    rom = Genre(name='Romance')
    rom.save()
    com = Genre(name='Comedy')
    com.save()

    Movie(name='Star Wars Episode I', release_date=date(1999, 7, 16), genre=sci_fi).save()
    Movie(name='Star Wars Episode II', release_date=date(2002, 5, 16), genre=sci_fi).save()
    Movie(name='Indiana Jones and the Temple of Doom', release_date=date(1984, 5, 23), genre=adv).save()

