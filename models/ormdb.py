from sqlalchemy import (create_engine, Integer, String,
                Text, DateTime, BigInteger, Column, ForeignKey)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
#import psycopg2


import datetime

# +-------------------------+-------------------------+
# +-------------------------+-------------------------+
db_schema = create_engine("sqlite:///c:\sqlite3\inventorydb", echo=True)
modelBase = declarative_base()

# +-------------------------+-------------------------+
# Re table schema
# +-------------------------+-------------------------+



#
class Reg(modelBase):

    __tablename__ = "user"
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
    #LoginTable()
    #create_table()
    #drop_table()
    view_rec()
