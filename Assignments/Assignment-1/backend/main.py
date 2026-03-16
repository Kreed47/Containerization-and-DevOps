from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import psycopg2
import os

app = FastAPI()

conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD")
)

@app.get("/")
def home():
    return FileResponse("static/index.html")

@app.post("/users")
def add_user(name:str):

    cur = conn.cursor()
    cur.execute("INSERT INTO users(name) VALUES(%s)", (name,))
    conn.commit()

    return {"message":"User added"}

@app.get("/users")
def get_users():

    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()

    return rows

@app.get("/health")
def health():
    return {"status":"ok"}

app.mount("/static", StaticFiles(directory="static"), name="static")