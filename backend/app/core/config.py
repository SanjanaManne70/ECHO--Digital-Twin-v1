from pathlib import Path
from urllib.parse import quote

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    app_name: str
    app_version: str
    debug: bool

    database_host: str
    database_port: int
    database_name: str
    database_user: str
    database_password: str

    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
    )

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+psycopg2://"
            f"{self.database_user}:{self.database_password}"
            f"@{self.database_host}:{self.database_port}/"
            f"{self.database_name}"
        )

    @property
    def sqlalchemy_database_url(self) -> str:
        password = quote(self.database_password, safe="")

        return (
            f"postgresql+psycopg2://"
            f"{self.database_user}:{password}"
            f"@{self.database_host}:{self.database_port}/"
            f"{self.database_name}"
        )


settings = Settings()
