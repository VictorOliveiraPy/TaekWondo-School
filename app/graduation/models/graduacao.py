from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app import Base


class Graduation(Base):
    __tablename__ = "graduation"

    id = Column("id", Integer, primary_key=True, index=True)
    color = Column("color", String)
    gub = Column("gub", Integer)

    content = relationship('Content', lazy="subquery", back_populates="graduation")






g = Graduation(id=2, color="red", gub=1)
print(g)