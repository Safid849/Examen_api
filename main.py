import json
from fastapi import FastAPI, Request
from starlette.responses import Response
from fastapi.responses import HTMLResponse, JSONResponse, Response
from pydantic import BaseModel
from typing import List

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
