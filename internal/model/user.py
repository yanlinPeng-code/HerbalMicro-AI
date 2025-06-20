from datetime import datetime
from uuid import UUID

from pydantic import EmailStr
from sqlmodel import Field

from .base import Base

class  UserBase(Base):
    email:EmailStr | None=Field(unique=True,index=True,max_length=255)
    full_name: str | None = Field(default=None, max_length=255)
    is_active: bool = Field(default=True)
    is_superuser: bool = Field(default=False)

class User(UserBase,table=True):
      __tablename__ = "users"
      id: UUID = Field(default_factory=UUID, primary_key=True)












