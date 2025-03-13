from fastapi import FastAPI

app = FastAPI()

@app.get("/health",
         tags = ["Health check"],
         summary= "Проверка сервера",
         description="Возврашать статус работы",
         response_description= "Статус сервиса",
         responses={200: {"description": "Сервис работает чувак"}}
         
         )
async def health_check():
    """
    Эндпоинт для мониторинга состояния сервиса.
    
    Используется:
    - DevOps-инженерами для проверки доступности
    - Системами мониторинга
    - Балансировщиками нагрузки
    """
    return {"status": "ok"}
