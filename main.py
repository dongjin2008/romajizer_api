from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import cutlet

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "https://music.youtube.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

katsu = cutlet.Cutlet()
katsu.use_foreign_spelling = False
class TextInput(BaseModel):
    text: str

@app.post("/")
async def root(input: TextInput):
    return {katsu.romaji(input.text)}