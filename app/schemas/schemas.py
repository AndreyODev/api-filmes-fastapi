from pydantic import BaseModel, Field


class Movie(BaseModel):
    titulo: str = Field(..., min_length=1, max_length=200)


class MovieResponse(Movie):
    id: str