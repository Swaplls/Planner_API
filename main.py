from fastapi import FastAPI
from routes.users import user_router
from routes.events import event_router
import uvicorn

app = FastAPI(title="Planner API — Swap11s")

# Регистрация маршрутов
app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")


@app.get("/")
async def root() -> dict:
    return {"message": "Planner API работает!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)