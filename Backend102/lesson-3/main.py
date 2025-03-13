from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field
from typing import List

app = FastAPI()

users_db = [
    {"id": 1, "name": "Adilet", "email": "adilet@example.com", "role": "admin"},
    {"id": 2, "name": "Anuar", "email": "anuar@example.com", "role": "user"}
]

class User(BaseModel):
    id: int = Field(..., examples=[42])
    name: str = Field(..., min_length=2, examples=["Name Surname"])
    email: EmailStr = Field(..., examples=["user@example.com"])
    role: str = Field(..., pattern="^(admin|user)$")

@app.post("/users")
async def create_user(user: User):
    for existing_user in users_db:
        if existing_user["id"] == user.id:
            raise HTTPException(400, detail="User ID already exists, please choose another ID") 
    
    user_data = user.dict()
    users_db.append(user_data)
    return user

@app.get("/users")
async def get_users():
    """
    Получение список пользователей
    """
    return users_db

@app.get("/users/{id}")
async def get_users_by_id(user_id: int):
    """
    Получение список пользователей по списку
    """
    for existing_user in users_db:
        if existing_user["id"] == user_id:
            return existing_user
    raise HTTPException(404, detail="User not found")

@app.delete("/users/{id}")
async def delete_by_id(user_id: int):
    """
    Delete user by ID
    """
    index_user = None
    for i, existing_user in enumerate(users_db):
        if existing_user["id"] == user_id:
            index_user = i
            break
        
    if index_user is None:
        raise HTTPException(404, detail="User not found")
        
    deleted_user = users_db.pop(index_user)
    return{"message": "User deleted successfully", "deleted_user": deleted_user}

@app.put("/users/{id}")
async def update_users(user_id: int, updated_user: User):
    """
    Update user with user_id
    """

    try:
        index = next(i for i, user in enumerate(users_db) if user["id"] == user_id)
    except StopIteration:
        raise HTTPException(status_code=404, detail="User not found")
    
    users_db[index] = updated_user.dict()
    return users_db[index]