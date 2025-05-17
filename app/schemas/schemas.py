from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')


class Task(BaseModel):
    id: Optional[int] = None
    title: str
    description: Optional[str] = None
    status: str

    def dict(self) -> dict:
        return {
            "title": str(self.title),
            "description": self.description,
            "status": self.completed,
        }

    class Config:
        orm_mode = True


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T] = None