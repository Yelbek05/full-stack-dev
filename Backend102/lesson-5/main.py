import bcrypt
from fastapi import FastAPI

app = FastAPI()


users = []

@app.post("/auth/register")
def register_user(name: str, email: str, password: str, role: str = "user"):
    # Проверка уникальности email
    if any(u["email"] == email for u in users):
        return {"error": "Email already exists"}

    # Хеширование пароля
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    # Создание нового пользователя
    new_user = {
        "id": len(users) + 1,
        "name": name,
        "email": email,
        "password": hashed_password,
        "role": role,
    }
    users.append(new_user)
    return {"message": "User registered successfully"}

@app.post("/auth/login")
def login_user(email: str, password: str):
    # Поиск пользователя
    user = next((u for u in users if u["email"] == email), None)
    if not user:
        return {"error": "Invalid email or password"}

    # Проверка пароля
    if not bcrypt.checkpw(password.encode('utf-8'), user["password"].encode('utf-8')):
        return {"error": "Invalid email or password"}

    return {"message": f"Welcome, {user['name']}"}