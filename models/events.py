from pydantic import BaseModel
from typing import List


class Event(BaseModel):
    id: int = None
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Запуск FastAPI",
                "image": "https://linktomymage.com/image.png",
                "description": "Обсудим книгу по FastAPI от Swap11s",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }