from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.settings import Settings


def setup_cors(app: FastAPI):
    settings = Settings()

    # Dev origins are hardcoded as they are safe for local development
    origins = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ]

    # Add UI URL from environment if provided
    if settings.ui_url:
        origins.append(settings.ui_url)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
