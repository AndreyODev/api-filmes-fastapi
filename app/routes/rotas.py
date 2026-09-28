from fastapi import APIRouter, HTTPException, status

from app.schemas.schemas import Movie, MovieResponse
from app.servicos.servicos import (
    create_movie_servico,
    delete_movie_servico,
    get_movie_by_id_servicos,
    listar_movies_servico,
    update_movie_servico,
)

router = APIRouter(prefix="/movie", tags=["movies"])


@router.post("", response_model=MovieResponse, status_code=status.HTTP_201_CREATED)
def create_movie(movie: Movie):
    try:
        return create_movie_servico(movie)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao criar filme: {exc}",
        ) from exc


@router.get("", response_model=list[MovieResponse])
def listar_movies():
    try:
        return listar_movies_servico()
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao listar filmes: {exc}",
        ) from exc


@router.get("/{movie_id}", response_model=MovieResponse)
def get_movie_by_id(movie_id: str):
    try:
        return get_movie_by_id_servicos(movie_id)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao buscar filme: {exc}",
        ) from exc


@router.put("/{movie_id}", response_model=MovieResponse)
def update_movie(movie_id: str, movie: Movie):
    try:
        return update_movie_servico(movie_id, movie)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao atualizar filme: {exc}",
        ) from exc


@router.delete("/{movie_id}")
def delete_movie(movie_id: str):
    try:
        delete_movie_servico(movie_id)
        return {"message": "Filme excluído com sucesso"}
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao excluir filme: {exc}",
        ) from exc