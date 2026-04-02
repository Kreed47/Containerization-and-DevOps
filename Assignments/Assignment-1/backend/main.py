from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
import os
import time

app = FastAPI()

# ✅ CORS (required for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Wait for DB to be ready (IMPORTANT in Docker)
while True:
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD")
        )
        break
    except Exception:
        print("Waiting for database...")
        time.sleep(2)


@app.post("/users")
def add_user(name: str):
    cur = conn.cursor()
    cur.execute("INSERT INTO users(name) VALUES(%s)", (name,))
    conn.commit()
    cur.close()
    return {"message": "User added"}


@app.get("/users")
def get_users():
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    cur.close()
    return rows


@app.get("/health")
def health():
    return {"status": "ok"}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
    conn.commit()
    cur.close()
    return {"message": "User deleted"}