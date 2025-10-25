# Alembic ----> A data migration tool for sqlalchemy
# Manage change in your database schema over time , safely 

# Think Git for your database


from sqlalchemy import Integer , String , Float

from sqlalchemy.orm import DeclarativeBase , mapped_column

class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    
    id: int = mapped_column(Integer , primary_key=True)
    name : str = mapped_column(String)
    email : str = mapped_column(String)
    

class Product(Base):
    __tablename__ = "products"
    
    id : int = mapped_column(Integer , primary_key=True)
    name : str = mapped_column(String)
    price : str = mapped_column(Float)
    
    
from alembic import op
import sqlalchemy as sa
    
        
        
def upgrade():
    op.add_column("users" , sa.Column())  