from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("sqlite:///:tkd", echo=True)

Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base(engine)
meta = Base.metadata

SessionMaker: Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(engine)
