from fastapi import FastAPI, Depends

from app.config import get_settings, Setting

app = FastAPI()


@app.get("/ping")
async def pong(settings: Setting = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing,
    }
