import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseAppSettings(BaseSettings):
    env: str = "local"
    model_config = SettingsConfigDict(
        env_file=".env" if os.path.exists(".env") else None,
        env_prefix="",
        extra="ignore",
    )


class DBSettings(BaseAppSettings):
    postgres_db: str
    postgres_user: str
    postgres_password: str
    postgres_host: str
    postgres_port: int

    @property
    def database_url(self) -> str:
        url = (
            f"postgresql+psycopg2://"
            f"{self.postgres_user}:"
            f"{self.postgres_password}@"
            f"{self.postgres_host}:"
            f"{self.postgres_port}/"
            f"{self.postgres_db}"
        )
        if self.env != "local":
            url += "?sslmode=require"
        return url


class AppSettings(BaseAppSettings):
    ui_url: str = ""
