from pydantic import BaseModel
from typing import List

class FilmBase(BaseModel):
    title: str
    description: str | None = None
    year: int

class DirectorBase(BaseModel):
    name: str
    bio: str | None = None

class GenreBase(BaseModel):
    name: str

class ReviewBase(BaseModel):
    comment: str
    rating: float

class FilmCreate(FilmBase):
    pass

class DirectorCreate(DirectorBase):
    pass

class GenreCreate(GenreBase):
    pass

class ReviewCreate(ReviewBase):
    pass

class Film(FilmBase):
    id: int
    director_id: int
    genre_id: int
    reviews: List['Review'] = []

    class Config:
        orm_mode = True

class Director(DirectorBase):
    id: int
    films: List['Film'] = []

    class Config:
        orm_mode = True

class Genre(GenreBase):
    id: int
    films: List['Film'] = []

    class Config:
        orm_mode = True

class Review(ReviewBase):
    id: int
    film_id: int

    class Config:
        orm_mode = True