# LAZY LOADING VS EAGER LOADING

from sqlalchemy import Column , Integer , create_engine , String , ForeignKey 
from sqlalchemy.orm import declarative_base , Session , relationship , joinedload , subqueryload , selectinload

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer , primary_key=True)
    name = Column(String)
    
    posts = relationship("Post" , back_populates='author')
    
    
class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer , primary_key=True)
    title = Column(String , nullable=False)
    
    user_id = Column(Integer , ForeignKey("users.id"))
    
    author = relationship("User" , back_populates="posts") 
    


engine = create_engine("sqlite:///example4.db" , echo=True , future = True)

Base.metadata.create_all(engine)

#-----------------------------------------------------------------------------------------

# Insert data

with Session(engine) as session:
    
    u1 = User(name = "alice" , posts = [
         Post(title = "Post 1"),
         Post(title = "Post2")
    ])
    
    u2 = User(name = "Bob" , posts = [
        Post(title = "Post3")
    ])
    
    u3 = User(name = "Charlie")    #  no post 
    
    
    session.add_all([u1 , u2 , u3])
    
    session.commit()
    
    
# ---------------------------------Lazy Loading----------------------------

with Session(engine) as session:
    users = session.query(User).all()
    
    for u in users:
        print(u.name , [p.title for p in u.posts])      # trigger user query


#-------------------------------------------------------------------

#  joined Eager loading

with Session(User) as session:
    users = session.query(User).options(joinedload(User.posts)).all()
    
    for u in users:
        print(u.name , [p.title for p in u.posts])
        
    
# subquery

with Session(engine) as session:
    users = session.query(User).options(subqueryload(User.posts)).all()
    for u in users:
        print(u.name, [p.title for p in u.posts])
    

# selectin

with Session(engine) as session:
    users = session.query(User).options(selectinload(User.posts)).all()
    for u in users:
        print(u.name, [p.title for p in u.posts])
    