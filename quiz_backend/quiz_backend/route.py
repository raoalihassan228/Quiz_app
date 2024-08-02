from fastapi import FastAPI, Request
from quiz_backend.db.db_connector import get_session, createTable
from contextlib import asynccontextmanager
from quiz_backend.models.user_models import User
import quiz_backend.models.admin_models
import quiz_backend.models.quiz_models
from quiz_backend.utils.imports import (
    InvalidInputException,
    NotFoundException,
    ConflictException,
)
from fastapi.responses import JSONResponse


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("create table")
    createTable()
    yield


app: FastAPI = FastAPI(lifespan=lifespan)


@app.exception_handler(NotFoundException)
def not_found(request: Request, exception: NotFoundException):
    return JSONResponse(status_code=404, content=f"{exception.not_found} not found")


@app.get("/")
def home():
    return "Quiz project with fastapi and nextjs"

@app.get("/api/getUser")
def getUser(user:str):
    if user == "Ali":
        raise NotFoundException("User")
    return "User found"