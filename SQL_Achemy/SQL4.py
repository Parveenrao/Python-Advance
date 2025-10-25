import sqlalchemy

from sqlalchemy import Column , Integer , String , Table , create_engine , ForeignKey  , MetaData  , Select

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


# joins 

smt = Select(users.c.name , posts.c.title).join(posts , users.c.id == posts.c.user_id)

with engine.connect() as conn:
    result = conn.execute(smt)
    for row in result:
        print(row)