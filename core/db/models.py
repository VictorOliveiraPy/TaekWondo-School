from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Graduation(Base):
    __tablename__ = "graduation"

    id = Column("id", Integer, primary_key=True, index=True)
    color = Column("color", String)
    gub = Column("gub", Integer)


class Content(Base):
    __tablename__ = "content"

    id = Column("id", Integer, primary_key=True, index=True)
    techniques = Column("techniques", String)
    description = Column("description", String)
    graduation_id = Column(Integer, ForeignKey("graduation.id"))

    graduantion = relationship(Graduation)


c = Content(id=1, techniques="dois", description="test", graduation_id=1)

