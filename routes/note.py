from fastapi import APIRouter
from fastapi import FastAPI, Request 
from fastapi.responses import HTMLResponse 
from modules.note import Note
from config.db import client
from schemas.note import noteEntity , notesEntity
from fastapi.templating import Jinja2Templates

app = FastAPI()
note = APIRouter()
templates = Jinja2Templates(directory="templates")

@note.get("/" , response_class=HTMLResponse)
async def read_item(request:Request):

    docs = client.notes.Notes_collection.find({})
    new_docs = []
    for doc in docs:
        new_docs +=(
        {
            "id" : doc["_id"],
            "title" : doc["title"],
            "desc" : doc["desc"]
            #"important" : doc["important"]
        }
    )
    return templates.TemplateResponse("index.html", {"request":request, "new_docs" : new_docs})


@note.post("/")
async def post_item(request:Request):
    form = await request.form()
    note = client.notes.Notes_collection.insert_one(dict(form))
    return {"Success" : True}

