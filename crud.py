from sqlalchemy.orm import Session

from . import models, schemas

# Filmes
def get_film_by_id(db: Session, film_id:int):
    return db.query(models.Film).filter(models.Film.id == film_id).first()

def get_film_by_title(db: Session, title: str):
    return db.query(models.Film).filter(models.Film.title == title).first()

def get_all_films(db: Session):
    return db.query(models.Film).all()

# Diretores

def get_director_by_id(db: Session, director_id:int):
    return db.query(models.Director).filter(models.Director.id == director_id).first()

def get_director_by_name(db: Session, name:int):
    return db.query(models.Director).filter(models.Director.name == name).first()

def get_all_directors(db: Session):
    return db.query(models.Director).all()

# Gêneros

def get_genre_by_id(db: Session, genre_id:int):
    return db.query(models.Genre).filter(models.Genre.id == genre_id).first()

def get_genre_by_name(db: Session, name:int):
    return db.query(models.Genre).filter(models.Genre.name == name).first()

def get_all_genre(db: Session):
    return db.query(models.Genre).all()

# Reviews

def get_review_by_id(db: Session, review_id:int):
    return db.query(models.Review).filter(models.REview.id == review_id).first()

def get_all_reviews(db: Session):
    return db.query(models.Review).all()

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()

def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
