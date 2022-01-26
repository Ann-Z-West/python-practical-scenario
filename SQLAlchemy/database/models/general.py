from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    status = Column(Integer)

    def __repr__(self):
        return "<Student(id='%s', name='%s', status='%s')>" % (
            self.id, self.name, self.status)
