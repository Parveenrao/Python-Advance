from sqlalchemy import Column , Integer , String , ForeignKey , create_engine
from sqlalchemy.orm import relationship , sessionmaker , declarative_base , Session

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer , primary_key = True)
    name = Column(String)
    age = Column(Integer)
    
    posts = relationship("Post" , back_populates="authors")
    

class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer , primary_key=True)
    title = Column(String)
    content = Column(String)
    user_id = Column(Integer , ForeignKey('users.id'))
    
    authors = relationship("User" , back_populates="posts")
    

    

engine = create_engine("sqlite:///parveen.db" , echo=True )

session = Session(bind=engine ,    future=True) 

Base.metadata.create_all(engine)

user1 = User(name = "Alice" , age = 25)
user2 = User(name = "bob" , age = 26)
user3 = User(name = "john" , age = 27)

session.add_all([user1 , user2 , user3])
session.commit()

   
    
    
hey = session.query(User).filter(User.age < 30).all()

for users in hey:
    print(users.age)
    