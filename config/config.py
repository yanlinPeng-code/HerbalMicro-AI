import os

from pydantic_settings import BaseSettings

from functools import lru_cache


class Settings(BaseSettings):

       # 关闭wtf的csrf保护
       WTF_CSRF_ENABLED:bool
       # SQLAlchemy数据库配置
       SQLALCHEMY_URL:str
       SQLALCHEMY_POOL_SIZE: int = 5
       SQLALCHEMY_POOL_RECYCLE: int = 3600
       SQLALCHEMY_ECHO:bool

       @property
       def SQLALCHEMY_ENGINE_OPTIONS(self) -> dict:
           return {
               "pool_size": self.SQLALCHEMY_POOL_SIZE,
               "pool_recycle": self.SQLALCHEMY_POOL_RECYCLE,
           }
       class  Config:
           env_file = ".env"
           env_file_encoding = "utf-8"

@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
