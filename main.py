from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Filmes


@app.get("/films/", response_model=list[schemas.Film])
def read_all_films(db: Session = Depends(get_db)):
    films = crud.get_all_films(db)
    return films


@app.get("/films/{film_id}", response_model=schemas.Film)
def read_film_by_id(film_id: int, db: Session = Depends(get_db)):
    db_film = crud.get_film_by_id(db, film_id=film_id)
    if db_film is None:
        raise HTTPException(status_code=404, detail="Film not found")
    return db_film


@app.get("/films/{film_title}", response_model=schemas.Film)
def read_film_by_title(film_title: str, db: Session = Depends(get_db)):
    db_film = crud.get_film_by_title(db, title=film_title)
    if db_film is None:
        raise HTTPException(status_code=404, detail="Film not found")
    return db_film


@app.post("/films/", response_model=schemas.Film)
def create_film(film: schemas.FilmCreate, director_id: int, genre_id: int, db: Session = Depends(get_db)):
    db_film = crud.get_film_by_title(db, title=film.title)
    if db_film:
        raise HTTPException(status_code=400, detail="Film already registred")
    return crud.create_film(db=db, film=film, director_id=director_id, genre_id=genre_id)

# Diretores


@app.get("/directors/", response_model=list[schemas.Director])
def read_all_directors(db: Session = Depends(get_db)):
    films = crud.get_all_films(db)
    return films


@app.get("/directors/{director_id}", response_model=schemas.Director)
def read_director_by_id(director_id: int, db: Session = Depends(get_db)):
    db_director = crud.get_director_by_id(db, director_id=director_id)
    if db_director is None:
        raise HTTPException(status_code=404, detail="Director not found")
    return db_director


@app.get("/directors/{name}", response_model=schemas.Director)
def read_director_by_name(film_title: str, db: Session = Depends(get_db)):
    db_director = crud.get_director_by_name(db, name=film_title)
    if db_director is None:
        raise HTTPException(status_code=404, detail="Director not found")
    return db_director


@app.post("/directors/", response_model=schemas.Director)
def create_director(director: schemas.DirectorCreate, db: Session = Depends(get_db)):
    db_director = crud.get_director_by_name(db, name=director.name)
    if db_director:
        raise HTTPException(
            status_code=400, detail="Director already registred")
    return crud.create_director(db=db, director=director)

# Gêneros


@app.get("/genres/", response_model=list[schemas.Genre])
def read_all_genres(db: Session = Depends(get_db)):
    genres = crud.get_all_genre(db)
    return genres


@app.get("/genres/{genre_id}", response_model=schemas.Genre)
def read_genre_by_id(genre_id: int, db: Session = Depends(get_db)):
    db_genre = crud.get_genre_by_id(db, genre_id=genre_id)
    if db_genre is None:
        raise HTTPException(status_code=404, detail="Genre not found")
    return db_genre


@app.get("/genres/{name}", response_model=schemas.Genre)
def read_genre_by_name(name: str, db: Session = Depends(get_db)):
    db_genre = crud.get_genre_by_name(db, name=name)
    if db_genre is None:
        raise HTTPException(status_code=404, detail="Genre not found")
    return db_genre


@app.post("/genres/", response_model=schemas.Genre)
def create_genre(genre: schemas.GenreCreate, db: Session = Depends(get_db)):
    db_genre = crud.get_genre_by_name(db, name=genre.name)
    if db_genre:
        raise HTTPException(status_code=400, detail="Genre already registred")
    return crud.create_genre(db=db, genre=genre)

# Reviews


@app.get("/reviews/", response_model=list[schemas.Review])
def read_all_reviews(db: Session = Depends(get_db)):
    reviews = crud.get_all_reviews(db)
    return reviews


@app.get("/reviews/{review_id}", response_model=schemas.Review)
def read_review_by_id(review_id: int, db: Session = Depends(get_db)):
    db_review = crud.get_review_by_id(db, review_id=review_id)
    if db_review is None:
        raise HTTPException(status_code=404, detail="Review not found")
    return db_review

@app.get("/films/{film_id}/review/", response_model=schemas.Review)
def read_reviews_from_movie(film_id: int, db: Session = Depends(get_db)):
    film = crud.get_film_by_id(db, film_id=film_id)
    return film.reviews