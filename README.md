# API Filmes FastAPI

**Repositório/projeto:** `api-filmes-fastapi`

API REST para gerenciamento de filmes. Permite cadastrar, listar, consultar por identificador, atualizar e excluir filmes, com persistência em MongoDB.

## Tecnologias

- Python
- FastAPI
- Pydantic
- PyMongo
- MongoDB
- Uvicorn
- pytest
- HTTPX, utilizado pelo `TestClient` do FastAPI nos testes

As dependências estão listadas em [`app/requisitos/requirements.txt`](app/requisitos/requirements.txt). O projeto não fixa versões nesse arquivo.

## Estrutura do projeto

```text
api-filmes-fastapi/
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
│   └── main.py
├── tests/
│   └── test_movies_api.py
├── .vscode/
│   └── settings.json
├── .gitignore
└── README.md
```

O ambiente virtual (`venv/` ou `.venv/`) é criado localmente e ignorado pelo Git; por isso, não faz parte da estrutura versionada do projeto.

## Organização e fluxo

```text
Requisição
   ↓
Rotas
   ↓
Serviços
   ↓
Repositórios
   ↓
MongoDB
```

- **Rotas** (`app/routes/rotas.py`): recebem as requisições HTTP, chamam os serviços e definem respostas e códigos HTTP.
- **Schemas** (`app/schemas/schemas.py`): validam os dados. Um filme recebe `titulo` (texto de 1 a 200 caracteres); a resposta também contém `id`.
- **Serviços** (`app/servicos/servicos.py`): coordenam as operações, verificam filmes não encontrados e formatam os dados para resposta.
- **Repositories** (`app/repositories/repositorio.py`): executam as operações de leitura e escrita usando PyMongo e convertem os identificadores para `ObjectId`.
- **Database** (`app/database/db.py`): cria o cliente MongoDB e seleciona o banco e a coleção.
- **Testes** (`tests/test_movies_api.py`): verificam a rota raiz e o fluxo de criação, listagem, consulta, atualização e exclusão.

## Banco de dados

A aplicação conecta ao MongoDB usando PyMongo com a configuração definida em `app/database/db.py`:

| Configuração   | Valor                       |
| -------------- | --------------------------- |
| URI            | `mongodb://localhost:27017` |
| Banco de dados | `cine-movie`                |
| Coleção        | `filmes`                    |

Não há variáveis de ambiente para esses valores no código atual. Os documentos guardam o campo `titulo`; o MongoDB gera `_id` como `ObjectId`, que a API devolve como `id` textual. A aplicação também solicita a criação de um índice para `titulo`.

## Instalação e execução local

### 1. Clonar o repositório

Use a URL do repositório remoto:

```powershell
git clone https://github.com/AndreyODev/api-filmes-fastapi.git
cd api-filmes-fastapi
```

Substitua `<URL_DO_REPOSITORIO>` pela URL de clone disponível no GitHub ou no provedor usado pelo projeto.

### 2. Criar e ativar o ambiente virtual

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Se a política de execução do PowerShell impedir a ativação, libere scripts apenas para a sessão atual e tente novamente:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### 3. Instalar as dependências

```powershell
python -m pip install -r app/requisitos/requirements.txt
```

### 4. Iniciar o MongoDB

Inicie o serviço local do MongoDB instalado na máquina ou execute `mongod` em um terminal. Por exemplo, no PowerShell:

```powershell
$dbPath = Join-Path $HOME "mongodb-data"
New-Item -ItemType Directory -Force -Path $dbPath
mongod --dbpath $dbPath
```

Esse exemplo usa uma pasta de dados dentro do perfil do usuário; ela é criada se ainda não existir. O comando pressupõe que `mongod` esteja no `PATH`. Caso não esteja, use o caminho do executável correspondente à sua instalação. O caminho de instalação varia entre máquinas. O servidor deve estar acessível em `localhost:27017`, conforme a URI configurada na aplicação.

### 5. Iniciar a API

Com o ambiente virtual ativado, na raiz do repositório:

```powershell
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

Esse comando disponibiliza a API em `127.0.0.1:8000`. Host e porta são definidos pelos argumentos do Uvicorn, não fixados no código da aplicação.

## Endereços

- **Aplicação/API:** <http://127.0.0.1:8000>
- **Swagger UI:** <http://127.0.0.1:8000/docs>
- **OpenAPI JSON:** <http://127.0.0.1:8000/openapi.json>

A rota `/` serve a página HTML simples de status presente em `app/index.html` e não é incluída no schema OpenAPI.

## Endpoints

Todas as rotas de filmes usam o prefixo `/movie`. O corpo de criação e atualização segue o schema `Movie`:

```json
{
  "titulo": "Matrix"
}
```

| Método   | Rota                | Finalidade                                                          |
| -------- | ------------------- | ------------------------------------------------------------------- |
| `GET`    | `/`                 | Serve a página HTML de status.                                      |
| `POST`   | `/movie`            | Cria um filme; retorna `201 Created` e o filme com `id` e `titulo`. |
| `GET`    | `/movie`            | Lista os filmes.                                                    |
| `GET`    | `/movie/{movie_id}` | Consulta um filme pelo ID do MongoDB.                               |
| `PUT`    | `/movie/{movie_id}` | Atualiza o título do filme indicado.                                |
| `DELETE` | `/movie/{movie_id}` | Exclui o filme indicado e retorna uma mensagem de confirmação.      |

Exemplo de criação:

```powershell
curl.exe -X POST "http://127.0.0.1:8000/movie" `
  -H "Content-Type: application/json" `
  -d '{"titulo":"Matrix"}'
```

Exemplo de atualização:

```powershell
curl.exe -X PUT "http://127.0.0.1:8000/movie/<ID_DO_FILME>" `
  -H "Content-Type: application/json" `
  -d '{"titulo":"Matrix Reloaded"}'
```

Substitua `<ID_DO_FILME>` pelo `id` retornado pela API. IDs inválidos ou filmes inexistentes resultam em resposta de não encontrado nas rotas de consulta, atualização e exclusão.

## Testes

Com as dependências instaladas e o MongoDB disponível na URI configurada, execute na raiz do projeto:

```powershell
python -m pytest -q tests/test_movies_api.py
```

O arquivo [`tests/test_movies_api.py`](tests/test_movies_api.py) verifica que a rota raiz responde com sucesso e exercita o fluxo CRUD (criar, listar, consultar, atualizar e excluir um filme) pela API. Este README não fixa um resultado de execução; a saída depende da execução local dos testes.
