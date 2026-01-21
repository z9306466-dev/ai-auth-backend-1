from fastapi import APIRouter, HTTPException
from database import SessionLocal
from models import User
import hashlib

router = APIRouter(prefix="/auth")

def hash_password(p):
    return hashlib.sha256(p.encode()).hexdigest()

@router.post("/register")
def register(email: str, password: str):
    db = SessionLocal()
    if db.query(User).filter(User.email == email).first():
        raise HTTPException(400, "User exists")

    user = User(
        email=email,
        password=hash_password(password),
        coins=50
    )
    db.add(user)
    db.commit()
    return {"msg": "Registered", "coins": 50}

@router.post("/login")
def login(email: str, password: str):
    db = SessionLocal()
    user = db.query(User).filter(User.email == email).first()
    if not user or user.password != hash_password(password):
        raise HTTPException(401, "Invalid login")

    return {
        "msg": "Logged in",
        "coins": user.coins,
        "premium": user.is_premium
    }