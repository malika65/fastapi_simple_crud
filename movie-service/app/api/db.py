import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


DATABASE_URI = 'postgresql://maks:123@localhost/movie_db'


engine = create_engine(DATABASE_URI)

# Creating SessionLocal class which will be database session on the request..

engine.connect()

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

## Creating the base clase, using the declerative_base() method which returns a class.
## Later we will need this Base Class to create each of the database models
# The declarative_base() base class contains a MetaData object where 
# newly defined Table objects are collected.
Base = declarative_base()



