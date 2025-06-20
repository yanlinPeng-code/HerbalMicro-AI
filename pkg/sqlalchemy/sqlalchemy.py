import contextlib



class SQLAlchemy:

    def __init__(self,engine,async_session_local):
        self.engine=engine
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










