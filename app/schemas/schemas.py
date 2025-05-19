from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')


class Task(BaseModel):
    id: Optional[int] = None
    name: str
    title: str
    description: Optional[str] = None
    status: str

    def dict(self) -> dict:
        return {
            "name": str(self.name),
            "description": str(self.description),
            "title": str(self.title),
            "status": str(self.status),
        }

    class Config:
        orm_mode = True


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T] = None