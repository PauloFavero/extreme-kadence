"""FastAPI Server Setup"""
from datetime import datetime
from http import HTTPStatus

from .routers.kadence.routes import kadence_router

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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

server = FastAPI(openapi_tags=tags_metadata)

server.add_middleware(
    CORSMiddleware,
    # allow_origins=allowed_origins,
    allow_credentials=False,
    allow_methods=allowed_methods,
    allow_headers=["*"],
)

server.include_router(kadence_router)

@server.get("/", status_code=HTTPStatus.OK)
def root():
    return f"ExtremeCloudIQ & Kadence Integrator"


@server.on_event("startup")
def startup_event():
    print(f"{datetime.now()} - Starting up server...")


@server.on_event("shutdown")
def shutdown_event():
    print(f"{datetime.now()} - Shutting down server...")
