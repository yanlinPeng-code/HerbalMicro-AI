from pydantic import EmailStr
from sqlmodel import SQLModel,Field
from .base import Base
class User(Base,table=True):
      email:EmailStr=Field(unique=True,index=True,max_length=255)
      password:str=Field(min_length=8,max_length=15)
      is_active:bool=Field(default=True)
      is_superuser:bool=Field(default=False)
      full_name:str | None=Field(default=None,max_length=255)











