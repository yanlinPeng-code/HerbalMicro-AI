from dataclasses import dataclass

from fastapi import FastAPI
from injector import inject
from config import Settings
from internal.router import Router
from pkg.sqlalchemy import SQLAlchemy
from fastapi_sqla import setup_middlewares

class Http(FastAPI):
    """Http服务引擎"""

    def __init__(self,
                 *args,
                 setting: Settings,
                 db:SQLAlchemy,
                 router: Router,
                 **kwargs):

        super().__init__(*args,**kwargs)
        self.lifespan=db.lifespan
        setup_middlewares(self)














        router.register_router(self)




