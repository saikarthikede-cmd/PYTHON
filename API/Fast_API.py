from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session

# ----------------------------
# Database Configuration
# ----------------------------

DATABASE_URL = "postgresql://postgres:karthik@localhost:5432/test_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# ----------------------------
# FastAPI App
# ----------------------------

app = FastAPI()

# ----------------------------
# Database Model
# ----------------------------

class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)

# Create table if not exists
Base.metadata.create_all(bind=engine)

# ----------------------------
# Pydantic Schema
# ----------------------------

class User(BaseModel):
    name: str
    email: str

# ----------------------------
# Database Dependency
# ----------------------------

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ----------------------------
# Routes
# ----------------------------

# Root route
@app.get("/")
def root():
    return {"message": "FastAPI + PostgreSQL is running 🚀"}

# GET all users
@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(UserDB).all()

# GET user by ID
@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserDB).filter(UserDB.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# POST create user
@app.post("/users")
def create_user(user: User, db: Session = Depends(get_db)):
    db_user = UserDB(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# DELETE user by ID
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserDB).filter(UserDB.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(user)
    db.commit()

    return {"message": "User deleted successfully", "user_id": user_id}
