from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
from psycopg2.extras import RealDictCursor
import uvicorn
import os

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

DATABASE_URL = f"postgresql://habit_user:{os.getenv('HABIT_USER_PASSWORD')}@localhost/create_habits"

def get_db_connection():
    return psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)


@app.get("/habits")
def get_habits():
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM habit")
        habits = cur.fetchall()
        return {"habits": habits}
    finally:
        cur.close()
        conn.close()


@app.get("/habits/{year}/{month}")
def get_habits_for_month(year: int, month: int):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            """
            SELECT * FROM habit_log
            WHERE date >= %s::DATE AND date < (%s::DATE + INTERVAL '1 month')
            """,
            (f"{year}-{month}-01", f"{year}-{month}-01")
        )
        habit_logs = cur.fetchall()
        return {"habit_logs": habit_logs}
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=9922, reload=True)
