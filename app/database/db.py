from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017", serverSelectionTimeoutMS=2000)
db = client["cine-movie"]
collection = db["filmes"]


def ensure_indexes() -> None:
    collection.create_index("titulo")


try:
    ensure_indexes()
except Exception:
    pass