from pydantic import BaseModel
from datetime import date

class HabitLog(BaseModel):
    habit_id: int
    date: date
    state: bool
