import contextlib

from fastapi import FastAPI
from fastapi_sqla import SqlaSession, startup




class SQLAlchemy(SqlaSession):
    @contextlib.asynccontextmanager
    async def lifespan(self):
        await startup()
        yield
    @contextlib.asynccontextmanager
    async def auto_commit(self):
        try:
            yield self
            self.commit()
        except Exception as e:
            self.rollback()
            raise e










