from sqlalchemy import (create_engine, Integer, String,
                Text, DateTime, BigInteger, Column, ForeignKey)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
#import psycopg2
import os


import datetime

# +-------------------------+-------------------------+
# +-------------------------+-------------------------+
# db_schema = create_engine("sqlite:///c:\sqlite3\inventorydb", echo=True)
db_schema = create_engine("postgres://ydgielxylcswqh:a2558be5543a818e80e18179d604c9cc118d08dc8beb8b33c8b2416ffe565815@ec2-54-163-226-238.compute-1.amazonaws.com:5432/d8j9fgf7o86lcq", echo=True)
modelBase = declarative_base()

# +-------------------------+-------------------------+
# Re table schema
# +-------------------------+-------------------------+



#
class Reg(modelBase):

    __tablename__ = "testdb"
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    fname = Column(String(50), nullable=False)
    lname = Column(String(50), nullable=False)
    gender = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    referral = Column(String(50), nullable=True, unique=True)
    referred = Column(String(50), nullable=True)
    current_bal  = Column(String(10), nullable=True)
    profile_pic = Column(String(50), nullable=True )
    date_created = Column(DateTime, nullable=False,
                          default=datetime.datetime.now())





# +-------------------------+-------------------------+
# +-------------------------+-------------------------+


def create_table():
    modelBase.metadata.create_all(db_schema)


def drop_table():
    modelBase.metadata.drop_all(db_schema)

# +-------------------------+-------------------------+
# +-------------------------+-------------------------

# run this when you want to create the tables that you need for a project

if __name__ == '__main__':
    create_table()
    
    
