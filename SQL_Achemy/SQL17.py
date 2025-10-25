# Repositry Pattern ------------------>

""" What is Repository Pattern?

A Repository is a layer between your business logic and the database.

Instead of directly writing session.query(User) everywhere in your code, you wrap that logic in a Repository class.

Separation of concerns → Business logic doesn't depend on database details.

Testability → You can mock repositories in unit tests.

Maintainability → Database code stays in one place:

Imagine your app as a restaurant:

Business logic (services) = Chef

Repository = Waiter (handles orders between chef and kitchen)

Database = Kitchen"""


#----------------Small E-commerce Sytem------------------------#


from sqlalchemy import Column , Float , String , Integer ,ForeignKey 
from sqlalchemy.orm import declarative_base , Session , relationship

Base = declarative_base()

# Define Models 

class User(Base):
    __tablename__ = "users"
    id = Column(Integer , primary_key=True)
    name = Column(String)
    email = Column(String , unique=True)
    orders = relationship("Order" , back_populates="user")
    


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer , primary_key=True)
    name = Column(String)
    price = Column(Float)
    stock = Column(Integer)
    
class Order(Base):
    __tablename__ = "orders"    
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer , ForeignKey("users.id"))
    product_id = Column(Integer , ForeignKey("products.id"))
    quantity = Column(Integer)
    
    user = relationship("User" , back_populates="orders")
    product = relationship("Product")
    
#-------------------------------------------------------------------------------------------------------------------------------    

# Generic Repo for CRUD Operation 

from sqlalchemy.orm import Session

class GenericRepository:
    def __init__(self,  session:Session , model):
        self.session = session
        self.model = model
        
    
    def add(self , entity):
        self.session.add(entity)
        
    
    def get_by_id(self , id_):
        return self.session.query(self.model).get(id_)
        
    
    def list_all(self):
        return self.session.query(self.model).all()          
    
    def delete(self , entity):
        self.session.delete(entity)
          
          
#-----------------------------------------------------------------------------------------------------------------------
          
# Specific Repository

class UserRespository(GenericRepository):
    def __init__(self , session:Session):
        super().__init__(session , User)
        
    
    def get_by_email(self , email:str):
        return self.session.query(User).filter(User.email == email).first()
    


class ProductRepository(GenericRepository):
    def __init__(self , session : Session):
        super().__init__(session ,Product)
        
    def get_available_products(self):
        return self.session.query(Product).filter(Product.stock > 0).all()
    
    
class orderRepository(GenericRepository):
    def __init__(self , session : Session):
        super().__init__(session , Order)
        
    def get_orders_by_user(self , user_id : int):
        return self.session.query(Order).filter(Order.user_id == user_id).all()


#------------------------------------------------------------------------------------

# Unit Work -------- Manage transaction across multiple Repo

class UnitOfWork:
    def __init__(self , session : Session):
        self.session = session 
        self.users = UserRespository(session)
        self.products = ProductRepository(session)
        self.orders = orderRepository(session)
        
    
    def __enter__(self):
        return self
    
    
    def __exit__(self , exc_type , ecx_val , ecx_tb):
        
        if exc_type:
            self.session.rollback()
            
        else:
            self.session.commit()
            
        
        self.session.close()                         



# ------------------------------------------------------------------------------------------------------

# Business Layer -------------------------------without touching SQL directly

class ECommerceService:
    def __init__(self , uow :UnitOfWork):
        self.uow = uow
    
    
    def place_order(self , user_email : str , product_id : int , quantity : int):
        
        user = self.uow.users.get_by_email(user_email)
        if not user:
            raise ValueError("User not Found")
        
        product = self.uow.products.get_by_id(product_id)
        
        if not product or product.stock < quantity:
            raise ValueError("Product is not available in sufficient quantity")
        
        
        # Reduce stock 
        product.stock -= quantity
        
        order =  Order(user_id=user.id, product_id=product.id, quantity=quantity)
        self.uow.orders.add(order)              
        
        
        

# Everything Together

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///ecommerce.db", echo=True)
SessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

# Example usage
session = SessionLocal()
with UnitOfWork(session) as uow:
    service = ECommerceService(uow)
    service.place_order("john@example.com", 1, 2)
        