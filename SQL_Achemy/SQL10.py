# Operation in SQL-ALCHEMY -------> 


from sqlalchemy import (Column  , Integer , String , create_engine  , ForeignKey , func)

from sqlalchemy.orm  import declarative_base , relationship , Session


Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer , primary_key=True , autoincrement=True)
    name = Column(String , nullable  = False)
    
    posts = relationship("Post" , back_populates="author")
    
 
 
class Post(Base):
        __tablename__ = "posts"
        
        id = Column(Integer , primary_key=True , autoincrement=True)
        title = Column(String, nullable=False)
        
        content = Column(String)
        
        
        user_id = Column(Integer , ForeignKey("users.id"))
        
        comments = relationship("Comment" , back_populates="post")
        author = relationship("User" , back_populates="posts")
        
        

class Comment(Base):
    __tablename__ = "comments"
    
    id = Column(Integer , primary_key=True , autoincrement=True)
    text = Column(String)
    post_id = Column(Integer , ForeignKey("posts.id"))
    
    
    post = relationship("Post" , back_populates="comments")
    


# create db 

engine = create_engine("sqlite:///example5.db" , echo=True , future=True)

Base.metadata.create_all(engine)

session = Session(engine)

u1 = User(name = "alice") 
u2 = User(name  = "Bob")

p1 = Post(title = "Sql-alchemy basic" , content = "Intro" , author = u1)
p2 = Post(title = "Advance ORM" , content  = "Deep dive" , author = u1)
p3 = Post(title = "FastAPI With Sql-alchemy" , author=u2)

c1 = Comment(text="Great post!", post=p1)
c2 = Comment(text="Thanks for sharing", post=p1)
c3 = Comment(text="Very helpful", post=p2)
c4 = Comment(text="Cool", post=p3)
c5 = Comment(text="Nice example", post=p3)


session.add_all([u1,u2 , p1, p2, p3 , c1 , c2, c3 , c4 , c5])
session.commit()


# Limit  + Offset (Pagination)

page1 = session.query(Post).limit(2).offset(0).all()
print(page1 , [p.title for p in page1])

page2 = session.query(Post).limit(2).offset(2).all()
print(page2 , [p.title for p in page2])



# Group by Count comment per psot 

comment_post = (session.query(Post.title , func.count(Comment.id).label("total comments")).join(Comment , Post.id == Comment.post_id).group_by(Post.id).all() )

for title, total in comment_post:
    print(f"{title}: {total} comments")