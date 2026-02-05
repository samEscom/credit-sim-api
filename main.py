from fastapi import FastAPI

from app.api.routes import health

app = FastAPI()


# app.include_router(chat.router)
app.include_router(health.router)


@app.get("/")
def read_root():
    return {"message": "Hello from Credit Sim API!"}
