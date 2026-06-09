# API Séries Favoritas

## Descrição

API desenvolvida em Django para gerenciamento de séries favoritas.

O sistema permite:

* Cadastrar séries
* Listar séries
* Buscar série por ID
* Atualizar séries
* Excluir séries
* Listar séries finalizadas
* Listar séries favoritas

## Tecnologias Utilizadas

* Python
* Django
* PostgreSQL
* Docker
* Docker Compose

## Estrutura do Projeto

```
series-favoritas/
│
├── backend/
├── docker/
├── docker-compose.yml
├── requirements.txt
├── .env
└── README.md
```

## Executando o Projeto

### Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
```

### Subir os containers

```bash
docker compose up --build
```

### Acessar a API

```
http://localhost:8000/api/series/
```

## Rotas

### Listar séries

```
GET /api/series/
```

### Buscar série por ID

```
GET /api/series/<id>/
```

### Cadastrar série

```
POST /api/series/cadastrar/
```

### Atualizar série

```
PUT /api/series/atualizar/<id>/
```

### Excluir série

```
DELETE /api/series/excluir/<id>/
```

### Séries finalizadas

```
GET /api/finalizadas/
```

### Séries favoritas

```
GET /api/favoritas/
```

## Autor

Linda Christi
Engenharia de Software – Universidade de Vassouras
