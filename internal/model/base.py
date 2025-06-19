from datetime import datetime
from uuid import UUID

from sqlmodel import SQLModel, Field


class Base(SQLModel):
    id:UUID=Field(default_factory=UUID,primary_key=True)
    created_at:int=Field(default_factory=lambda: int(datetime.now().timestamp()))
    updated_at:int=Field(default_factory=lambda: int(datetime.now().timestamp()))

    class Config:
        orm_mode=True


