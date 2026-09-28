from bson import ObjectId

from app.database.db import collection


def normalize_object_id(movie_id):
    if not ObjectId.is_valid(movie_id):
        raise ValueError("ID de filme inválido")
    return ObjectId(movie_id)


def create_movie_repositorio(movie_dict):
    result = collection.insert_one(movie_dict)
    return collection.find_one({"_id": result.inserted_id})


def listar_movies_repositorio():
    return list(collection.find())


def get_movie_by_id_repositorio(movie_id):
    return collection.find_one({"_id": normalize_object_id(movie_id)})


def update_movie_repositorio(movie_id, movie_dict):
    object_id = normalize_object_id(movie_id)
    collection.update_one({"_id": object_id}, {"$set": movie_dict})
    return collection.find_one({"_id": object_id})


def delete_movie_repositorio(movie_id):
    result = collection.delete_one({"_id": normalize_object_id(movie_id)})
    return result.deleted_count > 0