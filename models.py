from sqlalchemy import Boolean, Column, ForeignKey, Integer, VARCHAR, Float
from sqlalchemy.orm import relationship

from .database import Base

NAME_MAX_LENGHT = 100
SHORT_TEXT_LENGHT = 400

class Film(Base):
    __tablename__ = "film"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(VARCHAR(NAME_MAX_LENGHT))
    description = Column(VARCHAR(SHORT_TEXT_LENGHT))
    year = Column(Integer)

    director_id = Column(Integer, ForeignKey("film.id"))
    genre_id = Column(Integer, ForeignKey("film.id"))

    director = relationship("Director", back_populates="films")
    genre = relationship("Genre", back_populates="film")
    reviews = relationship("Review", back_populates="film")

class Director(Base):
    __tablename__ = "director"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(VARCHAR(NAME_MAX_LENGHT))
    bio = Column(VARCHAR(SHORT_TEXT_LENGHT))

    films = relationship("Film", back_populates="director")

class Genre(Base):
    __tablename__ = "genre"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(VARCHAR(NAME_MAX_LENGHT))

    films = relationship("Film", back_populates="genre")

class Review(Base):
    __tablename__ = "review"

    id = Column(Integer, primary_key=True, index=True)
    comment = Column(VARCHAR(SHORT_TEXT_LENGHT))
    rating = Column(Float)
    
    film_id = Column(Integer, ForeignKey("film.id"))

    film = relationship("Film", back_populates="reviews")