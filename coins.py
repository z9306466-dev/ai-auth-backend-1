from fastapi import HTTPException
from database import SessionLocal
from models import User

def spend_coins(user_id: int, amount: int):
    db = SessionLocal()
    user = db.query(User).get(user_id)

    if user.coins < amount:
        raise HTTPException(403, "Not enough coins")

    user.coins -= amount
    db.commit()