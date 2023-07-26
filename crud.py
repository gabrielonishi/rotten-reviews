from sqlalchemy.orm import Session

from . import models, schemas

# Filmes


def get_film_by_id(db: Session, film_id: int):
    return db.query(models.Film).filter(models.Film.id == film_id).first()


def get_film_by_title(db: Session, title: str):
    return db.query(models.Film).filter(models.Film.title == title).first()


def get_all_films(db: Session):
    return db.query(models.Film).all()


def create_film(db: Session, film: schemas.FilmCreate, director_id: int, genre_id: int):
    db_film = models.Film(
        film.model_dump, director_id=director_id, genre_id=genre_id)
    db.add(db_film)
    db.commit()
    db.refresh(db_film)

    return db_film


# Diretores
def get_director_by_id(db: Session, director_id: int):
    return db.query(models.Director).filter(models.Director.id == director_id).first()


def get_director_by_name(db: Session, name: int):
    return db.query(models.Director).filter(models.Director.name == name).first()


def get_all_directors(db: Session):
    return db.query(models.Director).all()


def create_director(db: Session, director: schemas.DirectorCreate):
    db_director = models.Director(director.model_dump)
    db.add(db_director)
    db.commit()
    db.refresh(db_director)

    return db_director

# Gêneros


def get_genre_by_id(db: Session, genre_id: int):
    return db.query(models.Genre).filter(models.Genre.id == genre_id).first()


def get_genre_by_name(db: Session, name: int):
    return db.query(models.Genre).filter(models.Genre.name == name).first()


def get_all_genre(db: Session):
    return db.query(models.Genre).all()

def create_genre(db: Session, genre: schemas.GenreCreate):
    db_genre = models.Genre(genre.model_dump)
    db.add(db_genre)
    db.commit()
    db.refresh(db_genre)

    return db_genre    

# Reviews


def get_review_by_id(db: Session, review_id: int):
    return db.query(models.Review).filter(models.REview.id == review_id).first()


def get_all_reviews(db: Session):
    return db.query(models.Review).all()

def create_review(db: Session, review: schemas.ReviewCreate, film_id: int):
    db_review = models.Genre(review.model_dump, film_id = film_id)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)

    return db_review 
