from app.repositories.repositorio import (
    create_movie_repositorio,
    delete_movie_repositorio,
    get_movie_by_id_repositorio,
    listar_movies_repositorio,
    update_movie_repositorio,
)


def format_movie(movie):
    if not movie:
        return None
    return {
        "id": str(movie["_id"]),
        "titulo": movie["titulo"],
    }


def create_movie_servico(movie):
    movie_data = create_movie_repositorio(movie.model_dump())
    return format_movie(movie_data)


def listar_movies_servico():
    movies = listar_movies_repositorio()
    return [format_movie(movie) for movie in movies]


def get_movie_by_id_servicos(movie_id):
    movie = get_movie_by_id_repositorio(movie_id)
    if not movie:
        raise ValueError("Filme não encontrado")
    return format_movie(movie)


def update_movie_servico(movie_id, movie):
    existing = get_movie_by_id_repositorio(movie_id)
    if not existing:
        raise ValueError("Filme não encontrado")
    updated = update_movie_repositorio(movie_id, movie.model_dump())
    return format_movie(updated)


def delete_movie_servico(movie_id):
    existing = get_movie_by_id_repositorio(movie_id)
    if not existing:
        raise ValueError("Filme não encontrado")
    deleted = delete_movie_repositorio(movie_id)
    if not deleted:
        raise ValueError("Não foi possível excluir o filme")
    return True
