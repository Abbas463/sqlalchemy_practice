from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class person(Base):
    __tablename__ = 'people'
    ssn = Column("ssn", Integer, primary_key=True)