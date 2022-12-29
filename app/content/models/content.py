from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app import Base


class Content(Base):
    __tablename__ = "content"

    id = Column("id", Integer, primary_key=True, index=True)
    techniques = Column("techniques", String)
    description = Column("description", String)
    graduation_id = Column(Integer, ForeignKey("graduation.id"))

    graduantion = relationship("Graduation", lazy="subquery", back_populates="content",  foreign_keys=[graduation_id])




c = Content(id=1, techniques="dois", description="test", graduation_id=1)
c.commit()

print(c)