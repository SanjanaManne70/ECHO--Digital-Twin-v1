from pydantic import BaseModel


class MemoryCreate(BaseModel):
    title: str
    description: str
    