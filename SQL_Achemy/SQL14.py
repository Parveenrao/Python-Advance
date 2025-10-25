""" Hybrid Property in SQL  ---> an hybrid propert is sql alchmey attribute that behvae like a normal pyhton  class and can also
    be used inside sql queries"""
    
    # At the instance level , it works like normal property decorator
    # At the class / instance level it translate into sql queries so you can used insdie filter order by
    
    
from sqlalchemy import Column , String , Integer , create_engine 
from  sqlalchemy.orm import declarative_base , sessionmaker
from sqlalchemy.ext.hybrid import hybrid_property


Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer , primary_key=True)
    first_name = Column(String) 
    last_name = Column(String)
    
    @hybrid_property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    # Expression version(for queries)
    
    @full_name.expression
    def full_name(cls):
        return cls.first_name + " " + cls.last_name
    
    
# Setup 


engine = create_engine("sqlite:///example6.db" , echo=True , future=True) 

Base.metadata.create_all(engine) 

Session = sessionmaker(bind = engine)

session = Session() 


#--------------------------Insert Data------------------------

session.add_all([
    User(first_name = "John" , last_name = "Doe"),
    User(first_name = "John" , last_name = "Smith")
]) 

session.commit()

#-------------------------------

u = session.query(User).first()

print(u.full_name)


users = session.query(User).filter(User.full_name == 'John Smith').all()
print(u.full_name for u in users)