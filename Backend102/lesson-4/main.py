from fastapi import FastAPI, HTTPException
from pydantic import EmailStr, Field, validator
from typing import Optional

app = FastAPI()

users = [ {"name": "Yelbek", "email": "elbekmoldabaev07@gmail.com", "password": "my_password"},
]
def validate_password(password: str):
    if len(password) < 6:
        raise ValueError("Пароль должен быть не менее 6 символов")

@app.post("/auth/register")
def register_user(name: str, email: EmailStr, password: str, role: str = "user"):
    # Проверить уникальность email
    if any(u["email"] == email for u in users):
        return {"error": "Email already exists"}
    if any(u["name"] == name for u in users):
        return {"error": "Username already exists"}
    
    try:
        validate_password(password)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    # Создать нового пользователя
    new_user = {
        "id": len(users) + 1,
        "name": name,
        "email": email,
        "password": password,  # Пароль пока хранится как обычный текст
        "role": role,
    }
    users.append(new_user)
    return {"message": "User registered successfully"}



@app.post("/auth/login")
def login_user(username_or_email: str, password: str):
    # Найти пользователя
    
    user = next((u for u in users if u["email"] == username_or_email or u for u in users if u["name"] == username_or_email), None)

    if not user:
        raise HTTPException(status_code=400, detail="Email не найден")
    
    if user["password"] != password:
        raise HTTPException(status_code=400, detail="Неправильный пароль")
    
    return {"message": f"Қош келдіңіз, {user['name']}"}

    
    
    

