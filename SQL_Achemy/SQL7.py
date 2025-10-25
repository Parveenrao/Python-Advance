# Commit and Rollback in SQL ALchemy

from sqlalchemy import Integer , String , create_engine , Column
from sqlalchemy.orm import Session , declarative_base , sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer , primary_key = True)
    name = Column(String)
    
    

engine = create_engine("sqlite:///parveen.db", echo=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind = engine)

session = Session()


# Add new user 

user1 = User(name = "Alice")

user2 = User(id = 1 , name = "Duplication_id")   # will raise integrity error

session.add_all([user1 , user2])

try:
    session.commit()
    print("Transaction Completed")

except Exception as e:
    print("Error:" , e)
    
    session.rollback()      # unoo all commited changes
    
finally:
    session.close()    

    