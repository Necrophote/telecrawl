from sqlalchemy import create_engine, Column, Table, ForeignKey, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
	Integer, String, Date, DateTime, Float, Boolean, Text)
from scrapy.utils.project import get_project_settings

Base = declarative_base()

def db_connect():
	return create_engine(get_project_settings().get("CONNECTION_STRING"))

def create_table(engine):
	Base.metadata.create_all(engine)

class Product(Base):
	__tablename__ = "product"

	id = Column(Integer, primary_key=True)
	name = Column('name', String(150))
	code = Column('code', String(150), unique=True)
	price_nkim = Column('price_nkim', String(20))
	price_tiki = Column('price_tiki', String(100))