import os
from dotenv import load_dotenv

# Manual load of .env for local development
if os.path.exists(".env"):
    load_dotenv()


class DBSettings:
    def __init__(self):
        self.env = os.getenv("ENV", "local")
        self.postgres_db = os.getenv("POSTGRES_DB")
        self.postgres_user = os.getenv("POSTGRES_USER")
        self.postgres_password = os.getenv("POSTGRES_PASSWORD")
        self.postgres_host = os.getenv("POSTGRES_HOST")
        self.postgres_port = os.getenv("POSTGRES_PORT", "5432")

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


class AppSettings:
    def __init__(self):
        self.env = os.getenv("ENV", "local")
        self.ui_url = os.getenv("UI_URL", "")
