

from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker

# +-------------------------+-------------------------+
# User defined imports
# +-------------------------+-------------------------+

from models.ormdb import db_schema, Reg  # imported from the ormdb.py file
# +-------------------------+-------------------------+
# +-------------------------+-------------------------+

CursorObj = sessionmaker(bind=db_schema)

def view_rec():
    with sql_cursor() as db:
        qry = db.query(Reg.id, Reg.email, Reg.fname, Reg.lname, Reg.referred,Reg.current_bal).filter(
            Reg.id == 3
        ).all()  
        print(qry) 

# +-------------------------+-------------------------+
# +-------------------------+-------------------------+

@contextmanager  # decorator to handle database connections
def sql_cursor():
    cursor = CursorObj()

    yield cursor

    try:
        cursor.commit()
    except Exception as e:
        cursor.rollback()
        raise e
        # add a logger here
def see_all_users():
    with sql_cursor() as db:
        qry = db.query(Reg.email, Reg.password).all()
        print(qry)

# +-------------------------+-------------------------+
# +-------------------------+-------------------------+
if __name__ == "__main__":
    
    view_rec()
