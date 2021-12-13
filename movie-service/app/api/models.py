
from sqlalchemy import Boolean, Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship

from .db import Base

class Catalog(Base):
    __tablename__ = 'catalog'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    
    

catalogs = Catalog.__table__    

class Product(Base):
    __tablename__ = 'product'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    
    
    
    
    
    