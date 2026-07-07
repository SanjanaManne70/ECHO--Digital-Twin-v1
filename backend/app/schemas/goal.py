from pydantic import BaseModel


class GoalCreate(BaseModel):

    title: str

    description: str