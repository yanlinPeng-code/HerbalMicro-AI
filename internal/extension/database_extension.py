from sqlalchemy import create_engine
from config import settings
from pkg.sqlalchemy import SQLAlchemy

engine=create_engine(settings.SQLALCHEMY_URL)

db=SQLAlchemy()