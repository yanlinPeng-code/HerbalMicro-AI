from datetime import datetime


from sqlmodel import SQLModel, Field


class Base(SQLModel):
    created_at:int=Field(default_factory=lambda: int(datetime.now().timestamp()))
    updated_at:int=Field(default_factory=lambda: int(datetime.now().timestamp()))




