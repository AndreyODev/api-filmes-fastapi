from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse

from app.routes.rotas import router

app = FastAPI(
    title="Backend Estudo - Filmes",
    version="1.0.0",
    description="API para cadastro, consulta, atualização e exclusão de filmes."
)


@app.get("/", include_in_schema=False)
def home():
    return FileResponse(Path(__file__).resolve().parent / "index.html")


app.include_router(router)