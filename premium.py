from datetime import datetime, timedelta
from database import SessionLocal
from models import User

def activate_premium(user_id):
    db = SessionLocal()
    user = db.query(User).get(user_id)
    user.is_premium = True
    user.premium_until = datetime.utcnow() + timedelta(days=30)
    db.commit()