from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
from psycopg2.extras import RealDictCursor
import uvicorn
import os
from models import HabitLog

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

DATABASE_URL = f"postgresql://habit_user:{os.getenv('HABIT_USER_PASS')}@localhost/create_habits"

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

@app.post("/upsert_days_habits")
def upsert_habit(habit_log: HabitLog):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            """
            INSERT INTO habit_log (habit_id, date, status)
            VALUES (%s, %s, %s)
            ON CONFLICT (habit_id, date)
            DO UPDATE SET status = EXCLUDED.status
            """,
            (habit_log.habit_id, habit_log.date, habit_log.state)
        )
        conn.commit()
        return {"status": "success"}
    except Exception as e:
        conn.rollback()
        print("Error:", e)
        return {"status": "error", "message": str(e)}
    finally:
        cur.close()
        conn.close()



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=9922, reload=True)
