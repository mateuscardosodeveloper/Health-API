# Health API

API simples para exibir alguns dados para o setor financeiro.


<h2> Ferramentas Utilizadas </h2>

A API foi desenvolvida utilizando a linguagem **Python**, junto da framework **Fastapi**, a ferramenta utilizada para execução dos testes automatizado foi o **Pytest**, também possui um **Continuous Integration**, que toda vez que for feito alguma alteração na branch master irá executar o github actions, que executará de forma automatizada os testes, caso algum teste falhe o build não prossegue.

Não utilizei o **Docker** no projeto, devido a minha falta de experiência.


<h2> Como Executar o Projeto Localmente</h2>

* Precisa ter instalado o gerenciador de depencias [poetry](https://python-poetry.org/docs/) e [python 3.10](https://www.python.org/downloads/).

* Após instalar as ferramentas, crie um arquivo .env dentro da pasta /app.

```properties
# Valores do arquivo .env
DEBUG=True
API_PREFIX=/health
EXPIRATION_TIME_HOUR=24
DATABASE_SQLITE_URL=sqlite+aiosqlite:///backend_test.db
USER_PROJECT_KEY=qsc8u3p5y67nlt4dvhdsz9okae8fd8aurc8rlom90z3byxez4x

```

* Agora no terminal de sua preferência entre dentro da pasta **app/** e execute os comandos a seguir:

```bash
# cria o arquivo .venv
poetry env use python3.10
# entra dentro da .venv
poetry shell
# instala todas as dependências contida no arquivo pyproject.toml
poetry install
# Atalho para execução do projeto local
python manage.py runserver
# para abrir o swagger este é o caminho http://0.0.0.0:4002/health/docs
```


<h2>Executar os Testes Automatizados</h2>

* Primeiro você deve comentar a variável **DATABASE_SQLITE_URL** dentro do arquivo .env, com isso não passará a usar o banco de dados original, e sim o de teste que está dentro **tests/db_test.db**

* Agora dentro do terminal basta executar o comando **pytest**:
```bash
# lembre-se de estar dentro da pasta /app
pytest
```
