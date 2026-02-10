from fastapi import FastAPI
from app.config.cors import setup_cors
from app.api.routes import health, credit
from app.config.logger import setup_logging

setup_logging()

app = FastAPI()

setup_cors(app)

app.include_router(credit.router)
app.include_router(health.router)


@app.get("/")
def read_root():
    return {"message": "Hello from Credit Sim API!"}
