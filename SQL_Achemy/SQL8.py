# Objects States in SQL-ALCHEMY
"""
1.  Transient --> Not in db or not in session just define , user1 = User(Id , name)
2 . Pending --> adding in session , not commited yet , (session.add())
3. Persistent --> in session and db (session.commit() / session.query)
4 . Detched --> no linger linked to the sesssion(session.close)

"""

# Expire()
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)

engine = create_engine("sqlite:///example1.db", echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# 1. Insert user
new_user = User(name="Alice")
session.add(new_user)
session.commit()

# 2. Query user (value is cached in memory)
user = session.query(User).first()
print("Before expire:", user.name)   # Alice (from memory)

# 3. Expire user
session.expire(user)   # mark data as "stale"

# 4. Access again → triggers a DB query to reload fresh value
print("After expire:", user.name)


# Refersh()

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)

engine = create_engine("sqlite:///example.db", echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# 1. Insert user
new_user = User(name="Alice")
session.add(new_user)
session.commit()

# 2. Query user (cached in memory as "Alice")
user = session.query(User).first()
print("Before refresh:", user.name)   # Alice

# ---- Imagine someone else updates DB directly here ----
session.execute("UPDATE users SET name='Alicia' WHERE id=:id", {"id": user.id})
session.commit()

# At this point, user object in memory is still "Alice"

# 3. Refresh → force reload from DB immediately
session.refresh(user)
print("After refresh:", user.name)    # Alicia (fresh from DB)



# Deteched Object

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.orm.exc import DetachedInstanceError

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)

engine = create_engine("sqlite:///example.db", echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Insert a user
new_user = User(name="Alice")
session.add(new_user)
session.commit()

# Query user
user = session.query(User).first()
print("Before detach:", user.name)   # works

# Close session → user is detached
session.close()

# Try to access attribute
try:
    print("After detach:", user.name)   # DetachedInstanceError if lazy-loaded
except DetachedInstanceError as e:
    print("Error:", e)
