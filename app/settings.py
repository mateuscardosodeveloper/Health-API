import os
import toml
from dotenv import load_dotenv

from typing import Optional


class InformationsApi:
    __BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def __init__(self):
        with open(os.path.join(self.__BASE_DIR, 'app/pyproject.toml')) as f:
            package_info = toml.load(f)

        self.PROJECT_NAME = package_info['tool']['poetry']['name']
        self.PROJECT_VERSION = package_info['tool']['poetry']['version']
        self.PROJECT_DESCRIPTION = package_info['tool']['poetry']['description']


class EnvironmentVariables:
    load_dotenv()

    LOG_LEVEL: str = os.environ.get('LOG_LEVEL')
    API_PREFIX: str = os.environ.get('API_PREFIX')
    DEBUG: Optional[bool] = os.environ.get('DEBUG', False)
    USER_PROJECT_KEY: str = os.environ.get('USER_PROJECT_KEY')
    DATABASE_SQLITE_URL: str = os.environ.get('DATABASE_SQLITE_URL')
    EXPIRATION_TIME_HOUR: int = os.environ.get('EXPIRATION_TIME_HOUR')


pyproject = InformationsApi()
settings = EnvironmentVariables()
