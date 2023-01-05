from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.db.models import Base


def create_db(file: str):
    engine = create_engine(file)
    Base.metadata.create_all(engine)

    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # Insert a few customers into the customers table

    # Insert a few rooms into the rooms table
    session.commit()
