from sqlalchemy import create_engine , Column , Integer , String , MetaData , ForeignKey
from sqlalchemy.orm import relationship , declarative_base , Session

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer , primary_key=True)
    name = Column(String , nullable = False)
    
    posts = relationship("Post" , back_populates="author")
    


class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer , primary_key=True)
    title = Column(String , nullable=False)
    
    user_id = Column(Integer , ForeignKey("users.id"))
    
    author  = relationship("User" , back_populates="posts")    
    

engine = create_engine("sqlite:///example3.db" , echo=True , future=True)

Base.metadata.create_all(engine)

    
#---------------------------------------------------------------------------------

# Simple Join(inner join)

from sqlalchemy import select 

with Session(engine) as session:
    stmt = (select(User , Post).join(Post ,User.id == Post.user_id))    
    
    result = session.execute(stmt).all()
    
    
    for row in result:
        print(row.User.name , "->", row.Post.title)
        


#-------------------------------------------------------------------------

#Outer Join(Left Outer Join)

stmt1 = select(User.name , Post.title).join(Post , User.id == Post.user_id , isouter=True)


# Join Via relationship 


stmt2 = select(User).join(User.posts)



# Join with select_from


stmt = (
    select(Post.title, User.name)
    .select_from(Post)
    .join(User, Post.user_id == User.id)
)

        