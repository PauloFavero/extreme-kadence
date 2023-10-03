"""FastAPI Server Setup"""
from datetime import datetime
from http import HTTPStatus

from config import environment
from .monitoring import enable_sentry
from .routers.kadence.routes import kadence_router

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

enable_sentry(environment.sentry)

allowed_methods = ["POST, GET"]

tags_metadata = [
    {
        "name": "Kadence Integration",
        "description": "Endpoints to integrate with the Kadence API",
    },
    {
        "name": "ExtremeCloudIQ Integration",
        "description": "Endpoints to integrate with the ExtremeCloudIQ API",
    },
]

app = FastAPI(openapi_tags=tags_metadata)

app.add_middleware(
    CORSMiddleware,
    # allow_origins=allowed_origins,
    allow_credentials=False,
    allow_methods=allowed_methods,
    allow_headers=["*"],
)

app.include_router(kadence_router)

@app.get("/", status_code=HTTPStatus.OK)
def root():
    return "ExtremeCloudIQ & Kadence Integrator"


@app.on_event("startup")
def startup_event():
    print(f"{datetime.now()} - Starting up server...")


@app.on_event("shutdown")
def shutdown_event():
    print(f"{datetime.now()} - Shutting down server...")


