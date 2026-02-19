from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class person(Base):
    __tablename__ = 'people'
    ssn = Column("ssn", Integer, primary_key=True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    gender = Column("gender", CHAR)
    age = Column("age", Integer)

    def __init__(self, ssn, first, last, gender, age):
        self.ssn = ssn
        self.firstname = first
        self.lastname = last
        self.gender = gender
        self.age = age
