# TODO: Criar alias para identar o código
import logging

import typer
from uvicorn.config import LOGGING_CONFIG

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger("uvicorn.error")


cli = typer.Typer(
    add_completion=False,
    help="Basic CLI manager for the API",
    name="Health API Manager",
)


@cli.command(help="Run the API server locally")
def runserver() -> None:
    from uvicorn import run as run_server

    from settings import settings

    if settings.DEBUG:
        logger.warning(
            "Dont run with \033[94msettings.DEBUG=True\033[0m in production mode"
        )
        logger.info(
            "By default, raw HTTP exception data is onlyavailable in the local and dev environments"
        )

    run_server(app="main:app", host="0.0.0.0", port=4002, reload=settings.DEBUG)


@cli.command(help="Open code coverage report")
def cov(path: str = "./htmlcov/index.html") -> None:
    import webbrowser

    webbrowser.open(path)


@cli.command(help="Indentation code with Black and Isort")
def indentation() -> None:
    import os

    os.system("black ../app*")
    os.system("isort .")


if __name__ == "__main__":
    cli()
