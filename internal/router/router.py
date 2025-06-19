from dataclasses import dataclass

from fastapi import FastAPI,APIRouter
from injector import inject

from internal.controller import AppHandler


@inject
@dataclass
class Router:
    """路由"""
    app_handler:AppHandler


    def register_router(self,app:FastAPI):
        """注册路由"""
        router=APIRouter()
        router.add_api_route("/ping",methods=["GET"],endpoint=self.app_handler.debug)



        app.include_router(router)

