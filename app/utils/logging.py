# External module
import logging

from termcolor import colored

from settings import settings

logging.basicConfig(
    format="%(asctime)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    level=settings.LOG_LEVEL,
)


def info(message):
    logging.info(colored(f"INFO - {message}", "green"))


def warn(message):
    logging.warn(colored(f"WARNIG - {message}", "yellow"))


def error(message):
    logging.error(colored(f"ERROR - {message}", "red"))
