# Lazy Loading IN SQL-ALCHEMy

from sqlalchemy import create_engine , Column , Integer , String , ForeignKey
from sqlalchemy.orm import Session , declarative_base , relationship

Base = declarative_base()

# Parent User 

class User(Base):
    __tablename__ = 'users'
    id  = Column(Integer , primary_key=True)
    name = Column(String(50) , nullable=False)
    
    # Relationship one to Many (lazy loading by default)
    addresses = relationship("Address" , back_populates='user' , lazy='select')
    
    

# Child : Address

class Address(Base):
        __tablename__ = 'addresses'
        id = Column(Integer , primary_key= True)
        email = Column(String , nullable=False )
        
        user_id = Column(Integer , ForeignKey("users.id"))
        
        
        # Realtion 
        user = relationship("User" , back_populates='addresses')


# Database Setup 
engine = create_engine('sqlite:///example2.db' , echo=True , future=True)

Base.metadata.create_all(engine)

# Insert data        

with Session(engine) as session:
    user1 = User(name = "Alice" , addresses = [Address(email = "alice@example.com"),
                                              Address(email = "bob.work@example.com")])
    
    user2 = User(name = "Bob")
    
    session.add_all([user1 , user2])
    
    session.commit()
    
   
#---------------Lazy Loading IN Action-------------------#

with Session(engine) as session:
    
    # Fetech users
    
    users = session.query(User).all()
    
    print("\nUsers fetched" , users)
    
    
    # Access the address of first user 
    
    print("\nAccessing alices addresses") 
    print(users[0].addresses)  