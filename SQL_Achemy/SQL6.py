# ORM SETUP MULTIPLE TABLES

from sqlalchemy import Column , create_engine , MetaData  , Integer , String , DateTime , func , ForeignKey , Text 

from sqlalchemy.orm import declarative_base , Session , relationship

Base = declarative_base()

#---------------------Models----------------#

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer  , primary_key= True)
    name = Column(String(50) , nullable= False , unique= True)
    email = Column(String(50) , nullable= False , unique=True)
    
    # One - to - many relationship (post) one user have many post 
    posts = relationship("Post" , back_populates='author' , cascade="all , delete-orphan")
    
    
    def __repr__(self):
        return f"<User(id = {self.id} , name = {self.name} , email = {self.email})"
    
    
class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer , primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(Text , nullable=False) 
    
    create_at = Column(DateTime , server_default=func.now())
    
    # Foreign key to user
    
    user_id = Column(Integer , ForeignKey("users.id") , nullable=False)
    
    # Relationship 
    
    author = relationship("User" , back_populates='posts')
    comments = relationship("Comment" , back_populates='post' , cascade="all, delete-orphan")
    
    
    def __repr__(self):
        return f"<Post(id={self.id}, title='{self.title}', user_id={self.user_id})>"
    
       

class Comment(Base):
    __tablename__ = 'comments'
    
    id = Column(Integer , primary_key=True)
    text = Column(Text , nullable=False)
    created_at = Column(DateTime , server_default=func.now())
    
    # foreign Key 
    post_id = Column(Integer , ForeignKey("posts.id") , nullable=False)
    
    # Relationship 
    post = relationship("Post" , back_populates = "comments")
    
    def __repr__(self):
        return f"<Comment(id={self.id}, post_id={self.post_id}, text='{self.text[:15]}...')>"
    
    
    
#------------DataBase Setup-------------#    
    
# SQLite in-memory for testing
engine = create_engine("sqlite:///:memory:", echo=True)      
Base.metadata.create_all(engine)    


#--------------------------------CRUD OPERATION---------------------# 

with Session(engine) as session:


    user1 = User(name = "ALice" , email = "Alice@exmample.com")
    user2 = User(name = "Bob" ,  email = "Bob@example.com")
    
    post1 = Post(title = "Alice first post" , content = "This is Alices first blog post" ,author = user1)
    post2 = Post(title = "Bob first posts" , content = "Bob is here with his post" , author = user2)
    
    comment1 = Comment(text = "Nice post Alice !" , post = post1)
    comment2 = Comment(text = "Thanks Bob" , post = post2)
    
    session.add_all([user1 , user2 , post1 , post2 , comment1 , comment2])
    
    session.commit() 
    


#-----------------READ------------------------#
all_users = session.query(User).all()
print("ALL Users " , all_users)

# get post of alice 

alice = session.query(User).filter_by(name = "ALice").first()
print("Alice's posts" , alice.posts)

# get comment of fist post

first_post = session.query(Post).first()

print(first_post.comments)

  # ---------------- UPDATE ----------------
    # Update Alice's email
alice.email = "alice_new@example.com"
session.commit()

print("Updated Alice:", alice)

    # ---------------- DELETE ----------------
    # Delete Bob (cascades to his posts and comments)
bob = session.query(User).filter_by(name="Bob").first()
session.delete(bob)
session.commit()

print("Remaining users:", session.query(User).all())