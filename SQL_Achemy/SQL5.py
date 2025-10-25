# ORM ----> Object Relational Mapping 

# Orm maps databse table  to python classes  and rows to class instance , instead of writing sql queries ,you woll writing python objects 
# and let orm handle sql generation , transaction and queries

from sqlalchemy import Column , String , Integer , create_engine , ForeignKey , select , MetaData

from sqlalchemy.orm import declarative_base , Session , relationship

Base = declarative_base()          # A blueprint or container for all your ORM models.


""" declarative_base() is a factory function that creates a base class for your ORM models.

Any class you define that inherits from Base will automatically:

Be mapped to a database table.

Register itself with SQLAlchemy’s internal metadata system."""


class User(Base):
    __tablename__ = 'users'  # table name in the db 
    
    id = Column(Integer , primary_key=True)
    name = Column(String , nullable = False , unique=True)
    email = Column(String , nullable=True , unique=True)
    
    # one-to-many : User ---> Address
    
    addresses = relationship("Address" , back_populates="user" , cascade = "all, delete-orphan")
    
    
    def __repr__(self):
        return f"User(id = {self.id} , name = {self.name!r})"
    
    # back_populates="user"

     # This is used for bidirectional relationships.

     # It must match the name of the relationship defined on the other side (Address).
     
    # cascade="all, delete-orphan"
    
     # This controls what happens when you add or delete objects.

     # all → all operations (save, delete, merge, etc.) cascade from parent (User) to children (Address).

     # delete-orphan → if an Address is no longer linked to a User, it gets deleted automatically (like an orphan cleanup).  
     

class Address(Base):
    __tablename__ =  "addresses"
    
    id = Column(Integer , primary_key=True)
    email = Column(String , nullable=True) 
    user_id = Column(Integer, ForeignKey("users.id"))
    
    user = relationship("User" , back_populates="addresses")
    
    
    def __repr__(self):
        return f"Address(id = {self.id} , email = {self.email!r})"   
    



engine = create_engine("sqlite+pysqlite:///example.db", echo=True, future=True)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
    
    
# Create Insert data    

from sqlalchemy.orm import Session 

with Session(engine) as session:
    # create a user 
    
    user1 = User(name = "Parveen" )
    
    # Add related address one to many 
    
    user1.addresses = [
        Address(email = 'parveen@example.com'),
        Address(email = 'alice@example.com')
       
    ]
    
    # add to session 
    session.add(user1)
    
    # commint transation 
    
    session.commit()
    
    print("Inserted:", user1)
    


# Read Data

from sqlalchemy import select 

with Session(engine) as session:
    
    # get all user 
    
    smt = select(User)
    
    users = session.execute(smt).scalars().all()
    
    print("All users" , users)