# Backend Estudo - Filmes

## Objetivo

Este projeto é uma API REST para cadastro, listagem, consulta, atualização e exclusão de filmes. A estrutura foi organizada em camadas para manter separação clara entre rotas, schemas, serviços e acesso ao banco de dados.

## Tecnologias utilizadas

- Python 3.12
- FastAPI
- Pydantic
- PyMongo
- MongoDB
- Uvicorn
- pytest

## Arquitetura e organização

A aplicação foi mantida em uma estrutura simples e coerente com a ideia original do projeto:

- [app/main.py](app/main.py): inicialização da aplicação FastAPI e rota raiz.
- [app/index.html](app/index.html): página HTML simples servida na rota inicial.
- [app/routes/rotas.py](app/routes/rotas.py): endpoints da API.
- [app/schemas/schemas.py](app/schemas/schemas.py): modelos de entrada e saída da API.
- [app/servicos/servicos.py](app/servicos/servicos.py): regras de negócio e conversão de dados.
- [app/repositories/repositorio.py](app/repositories/repositorio.py): acesso ao banco MongoDB.
- [app/database/db.py](app/database/db.py): conexão e configuração da base de dados.
- [tests/test_movies_api.py](tests/test_movies_api.py): testes de integração da API.

## Banco de dados

O projeto foi ajustado para usar MongoDB local com PyMongo. A conexão padrão é:

- URI: mongodb://localhost:27017
- Banco: cine-movie
- Coleção: filmes

A estrutura de persistência usa o campo _id do MongoDB (ObjectId) e armazena os filmes no formato:

```json
{
  "_id": "<ObjectId>",
  "titulo": "Matrix"
}
```

## Requisitos

As dependências do projeto são listadas em [app/requisitos/requirements.txt](app/requisitos/requirements.txt):

```txt
fastapi
uvicorn[standard]
pydantic
pymongo
pytest
httpx
```

## Como instalar

### 1. Criar ambiente virtual

```bash
python -m venv venv
```

### 2. Ativar ambiente virtual

No Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

No Windows CMD:

```cmd
venv\Scripts\activate.bat
```

No Linux/macOS:

```bash
source venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r app/requisitos/requirements.txt
```

## Como configurar o MongoDB

O projeto assume que o MongoDB está rodando localmente na porta 27017.

Se o MongoDB estiver instalado no sistema, pode ser iniciado com o binário `mongod.exe`:

```powershell
"C:\Program Files\MongoDB\Server\8.2\bin\mongod.exe" --dbpath "C:\data\db" --logpath "C:\data\logs\mongod.log" --bind_ip 127.0.0.1 --port 27017
```

> O diretório `C:\data\db` precisa existir.

## Como executar

Na raiz do projeto, com o ambiente virtual ativado:

```bash
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

Ou diretamente com Python:

```bash
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

## Endereço da API

- API: http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs
- OpenAPI JSON: http://127.0.0.1:8000/openapi.json

## Endpoints principais

### POST /movie
Cria um filme.

Exemplo de corpo:

```json
{
  "titulo": "Matrix"
}
```

### GET /movie
Lista todos os filmes.

### GET /movie/{movie_id}
Busca um filme pelo identificador MongoDB.

### PUT /movie/{movie_id}
Atualiza um filme.

### DELETE /movie/{movie_id}
Exclui um filme.

### GET /
Retorna a página HTML simples de status em [app/index.html](app/index.html).

## Exemplos de uso

### Criar filme

```bash
curl -X POST "http://127.0.0.1:8000/movie" \
  -H "Content-Type: application/json" \
  -d '{"titulo":"Matrix"}'
```

### Listar filmes

```bash
curl http://127.0.0.1:8000/movie
```

### Buscar filme por ID

```bash
curl http://127.0.0.1:8000/movie/<movie_id>
```

### Atualizar filme

```bash
curl -X PUT "http://127.0.0.1:8000/movie/<movie_id>" \
  -H "Content-Type: application/json" \
  -d '{"titulo":"Matrix Reloaded"}'
```

### Excluir filme

```bash
curl -X DELETE "http://127.0.0.1:8000/movie/<movie_id>"
```

## Estrutura de pastas

```text
backend-estudo/
├── app/
│   ├── database/
│   │   └── db.py
│   ├── repositories/
│   │   └── repositorio.py
│   ├── requisitos/
│   │   └── requirements.txt
│   ├── routes/
│   │   └── rotas.py
│   ├── schemas/
│   │   └── schemas.py
│   ├── servicos/
│   │   └── servicos.py
│   ├── index.html
│   ├── main.py
│   └── __init__.py (se necessário em alguns ambientes)
├── tests/
│   └── test_movies_api.py
├── .vscode/
│   └── settings.json
├── venv/
├── README.md
└── .gitignore
```

## Observações importantes

- O projeto foi estruturado em camadas, com fluxo completo: rota → schema → serviço → repositório → banco.
- O MongoDB é a persistência real adotada, e não uma lista em memória.
- A página HTML em [app/index.html](app/index.html) serve apenas como resposta inicial da rota raiz; o foco principal é a API.
- O projeto foi validado com testes de CRUD e com resposta do Swagger/OpenAPI.

## Validação executada

Os testes do projeto foram executados com sucesso:

```bash
python -m pytest -q tests/test_movies_api.py
```

Resultado esperado:

```text
2 passed, 1 warning in 25.94s
```

A advertência é de depreciação do TestClient do Starlette com o httpx, mas não impede o funcionamento da API.
