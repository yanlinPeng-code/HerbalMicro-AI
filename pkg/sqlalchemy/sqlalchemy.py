import contextlib



class SQLAlchemy:

    def __init__(self,async_engine,async_session_local):
        self.async_engine=async_engine
        self.async_session_local=async_session_local

    @contextlib.asynccontextmanager
    async def auto_commit(self):
        async with self.async_session_local() as session:
            try:
                yield session
                await session.commit()
            except Exception as e:
                await session.rollback()
                raise e










