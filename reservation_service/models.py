from pydantic import BaseModel

class Reservation(BaseModel):
    id: int
    user_id: int
    location: str
    time: str
    guests: int
