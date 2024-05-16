# from typing import Union
from fastapi import FastAPI, Request 
from fastapi.responses import HTMLResponse 

from pymongo import MongoClient
client = MongoClient('mongodb+srv://Fast_api:Fastapi11@cluster0.twzmfju.mongodb.net/')



# Notes = client['notes']
# Notes_collection = Notes['notes']


app = FastAPI()



