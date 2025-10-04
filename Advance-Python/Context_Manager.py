""" Context manager in python is way to allocate and release resource precisely when you want 
    Most commonly it is used for file operation and network connection and db connections"""
    
with open("file.txt", "r") as f:
    data = f.read()
# file is automatically closed here


# Internally context manager uses enter and exit method     



# Real life example db connection 

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = 'sqlite:///example.db'

engine =  create_engine(DATABASE_URL  , echo = True , future = True)

SessionLocal =  sessionmaker(bind=engine)

Base = declarative_base()

Base.metadata.create_all(engine)

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    
    
class DBSession:
    def __enter__(self):
        self.session = SessionLocal()
        print("Session Opened")
        return self.session
    
    def __exit__(self , exc_type , exc_val , exc_tb):
        if exc_type:
            self.session.rollback()
            print(f"Exception occured: {exc_val}. Rolling back Session")
        
        else:
            self.session.commit()
            print('Session commited')
            
         
        self.session.close()
        print("session closed")
        return True
    
    
    
    
with DBSession() as session:
    session.add(User(id = 1, name = ['Parveen']))
    
    users = session.query(User).all()
    
    for user in users:
        print(user.id , user.name)
                    

                
            
    
    


