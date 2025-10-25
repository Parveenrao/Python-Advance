import sqlalchemy

from sqlalchemy import Column , Integer , String , Table , create_engine , ForeignKey  , MetaData  

# engine 

engine = create_engine("sqlite:///my.db" , echo = True)

metadata = MetaData()


# user table 
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey

# Metadata
metadata = MetaData()

# Users table
users = Table("users", metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False, unique=True),
    Column("email", String, nullable=False, unique=True)
)

# Posts table
posts = Table("posts", metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String, nullable=False),
    Column("content", String, unique=True, nullable=False),
    Column("user_id", Integer, ForeignKey("users.id"))  # fixed foreign key
)



metadata.create_all(engine)

# insert data 

from sqlalchemy import insert , select

with engine.connect() as conn:
    
    #insert into user
    conn.execute(insert(users).values(name = "Alice" , email = "alice@example.com"))
    conn.execute(insert(users).values(name = "Bob" , email = "Bob@example.com"))
    
    #insert into posts
    
    conn.execute(insert(posts).values(title = "First post" , content = "Hello!" , user_id = 1))
    conn.execute(insert(posts).values(title = "Second post" , content = "I am Sqlalchemy" , user_id = 1))
    conn.execute(insert(posts).values(title = 'Bob post' , content  = "I am Bob" , user_id = 2))
    
    conn.commit()
    
with engine.connect() as conn:
    result = conn.execute(select(users))
    
    for row in result:
        print(row)