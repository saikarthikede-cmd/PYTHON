from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

class UpdateUser(BaseModel):
    name: str | None = None
    age: int | None = None
