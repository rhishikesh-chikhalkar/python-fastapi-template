import os
import sys

if os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")) not in sys.path:
    sys.path.insert(
        0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    )

from fastapi import FastAPI

from src.app.routers.health import health_router

app = FastAPI(title="Python FastAPI Template")


@app.get("/")
def root():
    return {"message": "FastAPI app is running"}


app.include_router(health_router)
