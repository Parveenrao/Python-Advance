#  Bulk inserting mapping ---> bulk_insert_mappings allows you to insert multiple rows efficiently without 
# creating Python objects for each row.

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer , primary_key=True)
    name = Column(String , nullable=False)
    age = Column(Integer)
    
    

engine = create_engine("sqlite:///bulk_example.db" , echo=True , future=True)
Base.metadata.create_all(engine)

with Session(engine) as session:
    data = [
            {"name": "Alice" , "age" : 25},
            {"name" : "Bob" , "age" : 30},
            {"name" : "Charlie" , "age" : 22}
    ]
    
    session.bulk_insert_mappings(User , data)
    session.commit()
        
#----------------------------------------------------------------------------------------------------------------

"""Bulk Update Using bulk_update_mappings

bulk_update_mappings updates multiple rows in bulk based on a primary key."""

with Session(engine) as session:
    updates = [
        {"id": 1, "age": 26},   # Alice's new age
        {"id": 2, "age": 31},   # Bob's new age
        {"id": 3, "age": 23}    # Charlie's new age
    ]
    
    
    session.bulk_update_mappings(User , updates)
    session.commit()        
    
    
#------------------------------------------------------------------------------------------

"""Mixed insert and update"""

with Session(engine) as session:
    # Bulk insert
    session.bulk_insert_mappings(User, [
        {"name": "David", "age": 28},
        {"name": "Eva", "age": 27}
    ])
    
    # Bulk update
    session.bulk_update_mappings(User, [
        {"id": 1, "age": 27},
        {"id": 4, "age": 29}  # David's new age
    ])
    
    session.commit()
