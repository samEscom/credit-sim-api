from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    env: str = "dev"
    ui_url: str = ""

    postgres_db: str
    postgres_user: str
    postgres_password: str
    postgres_host: str
    postgres_port: int

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+psycopg2://"
            f"{self.postgres_user}:"
            f"{self.postgres_password}@"
            f"{self.postgres_host}:"
            f"{self.postgres_port}/"
            f"{self.postgres_db}"
        )

    model_config = {"env_file": ".env", "extra": "ignore"}
