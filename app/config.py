import os
from typing import Optional


from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env")
    )
    # БД
    database_dsn: str
    echo_db_engine: Optional[bool] = True
    db_host: str
    db_port: int
    db_user: str
    db_pass: str
    db_name: str

settings = Settings()