from fastapi import FastAPI
from sqlmodel import SQLModel
from internal.router import Router
from pkg.sqlalchemy import SQLAlchemy


class Http(FastAPI):
    """Http服务引擎"""

    def __init__(self,
                 *args,
                 db:SQLAlchemy,
                 router: Router,
                 **kwargs):

        super().__init__(*args,**kwargs)

        async def init_db():
            async with db.async_engine.begin() as conn:
                # 执行 SQLModel 的 create_all 同步方法，但在异步连接中运行
                await conn.run_sync(SQLModel.metadata.create_all)

        async def delete_all_tables():
            async with db.async_engine.begin() as conn:
                await conn.run_sync(SQLModel.metadata.drop_all)

        @self.on_event("startup")
        async def on_startup():
            await delete_all_tables()
            await init_db()







        router.register_router(self)




