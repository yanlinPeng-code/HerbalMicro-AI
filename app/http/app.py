import uvicorn

from config import Settings
from internal.router import Router
from internal.http import Http
from pkg.sqlalchemy import SQLAlchemy

from .module import injector
app=Http(
    title="HerbalMicro-AI",
    router=injector.get(Router),
    db=injector.get(SQLAlchemy),
    setting=injector.get(Settings)
)




if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000,reload=True,log_level="info")