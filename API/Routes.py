from fastapi import APIRouter
from Models import User, UpdateUser

router = APIRouter()

@router.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

@router.post("/users")
def create_user(user: User):
    return {"message": "user created", "user": user}

@router.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    return {"message": "user updated", "user_id": user_id, "user": user}

@router.patch("/users/{user_id}")
def update_user_partial(user_id: int, user: UpdateUser):
    return {"message": "user partially updated", "user": user}

@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    return {"message": "user deleted", "user_id": user_id}
