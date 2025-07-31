import json
from datetime import datetime
from symtable import Class

from fastapi import FastAPI, Request
from starlette.responses import Response
from fastapi.responses import HTMLResponse, JSONResponse, Response
from pydantic import BaseModel
from typing import List

app = FastAPI()

@app.get("/ping", status_code=200)
async def ping():
    return "pong"

@app.get("/home", status_code=200)
async def welcome_home():
    with open("index.html", "r", encoding="utf-8") as file:
        html_content = file.read()
        return  html_content

class Book(BaseModel):
    author: str
    title: str
    content: str
    creation_datetime: datetime

list_book: list[Book]= []

@app.post("/posts", status_code=201)
async def add_book(new_books: list[Book]):
    list_book.extend(new_books)
    return  list_book

@app.get("/posts", status_code=200)
async def get_books():
    return list_book

@app.put("posts")
def create_or_update_post(post: Book):
    for i, existing_post in enumerate(list_book):
        if existing_post.title == post.title:
            if existing_post.content != post.content:
                list_book[i] = post
                return {"message": "Post updated"}
            else:
                return {"message": "Post already exists with same content"}
    list_book.append(post)
    return {"message": "Post added"}

@app.get("/{full_path:path}", status_code=404)
def catch_all(full_path: str):
    with open("notFound.html", "r", encoding="utf-8") as file_not_found:
        html_content = file_not_found.read()
        return html_content




