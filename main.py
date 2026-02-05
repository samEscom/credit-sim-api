from fastapi import FastAPI

from app.api.routes import health, credit
from app.config.logger import setup_logging

setup_logging()

app = FastAPI()


app.include_router(credit.router)
app.include_router(health.router)


@app.get("/")
def read_root():
    return {"message": "Hello from Credit Sim API!"}
