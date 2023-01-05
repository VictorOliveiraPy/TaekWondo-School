from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker


engine: Engine = None
DBSession = sessionmaker()


def init_db(files: str):
    engine = create_engine(files)
    Base.metadata.bind = engine
    DBSession.bind = engine
