from sqlalchemy import Boolean, Column, ForeignKey, Integer, VARCHAR, Float
from sqlalchemy.orm import relationship

from .database import Base

class Film(Base):
    __tablename__ = "film"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(VARCHAR(100))
    description = Column(VARCHAR(400))
    year = Column(Integer)
    director_id = Column(Integer, ForeignKey("director.id"))

    director = relationship("Director", back_populates="films")
    reviews = relationship("Reviews", back_populates="film")

class Director(Base):
    __tablename__ = "director"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(VARCHAR(100))
    bio = Column(VARCHAR(400))

    films = relationship("Film", back_populates="reviews")

class Reviews(Base):
    __tablename__ = "Director"

    id = Column(Integer, primary_key=True, index=True)
    comment = Column(VARCHAR(400))
    rating = Column(Float)
    film_id = Column(Integer)

    film = relationship("Film", back_populates="reviews")
