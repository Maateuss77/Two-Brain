# Two Brain

## Descrição

API RESTful desenvolvida para gerenciar **notas, pensamentos e ideias**, seguindo o modelo **single-tenant**, onde cada usuário possui acesso apenas às suas próprias notas.

O projeto foi pensado com foco em **organização, segurança e boas práticas**, sendo criado para uso pessoal.

---

## 🚀 Stack

- **FastAPI** — framework web moderno e performático
- **SQLAlchemy 2.0** — ORM para modelagem e acesso ao banco de dados
- **PostgreSQL** — banco de dados relacional
- **pwdlib[argon]** — hashing seguro de senhas (Argon2)
- **Alembic** — controle de migrations do banco de dados

---

## 🗂 Organização do Projeto

O projeto segue uma estrutura simples e bem definida:

- **Database/**
  Contém tudo relacionado ao banco de dados: models, sessão, engine e configurações.

- **routes/**
  Define todas as rotas da API (endpoints), separadas por contexto.

- **security/**
  Responsável pela parte de segurança da aplicação, incluindo:
    - Geração e validação de tokens
    - Hash e verificação de senhas

---

## ▶️ Como Rodar o Projeto

### 1️⃣ Pré-requisitos

- **Python 3.10+**
- **PostgreSQL** em execução
- **uv** instalado (gerenciador de dependências)

---

### 2️⃣ Clonando o repositório

```bash
git clone <url-do-repositorio>
cd two-brain
```

---

### 3️⃣ Configuração do ambiente

Crie um arquivo `.env` com base no `.env.example`:

```bash
cp .env.example .env
```

Exemplo de variáveis de ambiente utilizadas:

```env
DATABASE_URL=postgresql+psycopg://user:password@localhost:5432/twobrain
SECRET_KEY=super-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

⚠️ Ajuste os valores conforme seu ambiente local.

---

### 4️⃣ Instalando as dependências

As dependências do projeto são instaladas utilizando o **uv**:

```bash
uv sync
```

---

### 5️⃣ Migrations com Alembic

O projeto utiliza **Alembic** para versionamento do banco de dados.

Criar as tabelas no banco:

```bash
alembic upgrade head
```

Criar uma nova migration:

```bash
alembic revision --autogenerate -m "descrição da migration"
```

---

### 6️⃣ Rodando a aplicação

Para iniciar a API:

```bash
uv run serv
```

A aplicação estará disponível em:

```
http://localhost:8000
```

Documentação automática (Swagger):

```
http://localhost:8000/docs
```

---

### 7️⃣ Ambiente de desenvolvimento (opcional)

Para instalar dependências de desenvolvimento:

```bash
uv sync --dev
```

Inclui ferramentas como **pytest** e **ruff**.

---

## ⚙️ Em Desenvolvimento

- [ ] Expansão dos testes
- [ ] Documentação completa dos endpoints
- [ ] Frontend
