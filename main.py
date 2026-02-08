from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import health, credit
from app.config.logger import setup_logging

setup_logging()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Vite
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(credit.router)
app.include_router(health.router)


@app.get("/")
def read_root():
    return {"message": "Hello from Credit Sim API!"}
