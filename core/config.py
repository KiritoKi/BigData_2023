from os import environ
from typing import Optional, Dict, Any

from dotenv import load_dotenv
from decouple import config
from pydantic import validator
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    VERSION: str = '0.0.1'
    PROJECT_NAME: str = '---'

    # DATABASE
    HOST_DB:str = environ.get('HOST_DB', 'localhost')
    USER_DB:str = environ.get('USER_DB', 'root')
    PASSWORD_DB:str = environ.get('PASSWORD_DB', '')
    DATABASE_DB:str = environ.get('DATABASE_DB', '')
    PORT_DB:str = environ.get('PORT_DB', '3306')
    CHARSET_DB:str = environ.get('CHARSET_DB', 'utf8mb4')
    LOAD_DATASET:str = environ.get('LOAD_DATASET', 'no')
    SQLALCHEMY_DATABASE_URI: str = f'postgresql://{USER_DB}:{PASSWORD_DB}@{HOST_DB}:{PORT_DB}/{DATABASE_DB}'


settings = Settings()