# Hotel Booking System

from sqlalchemy import Float , String , Column , Date , Integer , create_engine , ForeignKey
from sqlalchemy.orm import declarative_base , relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer , primary_key=True)
    name = Column(String)
    email = Column(String , unique=True)
    
    bookings = relationship("User" , back_populates='user')
    
class Hotel(Base):
    __tablename__ = "hotels"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    rooms = relationship("Room", back_populates="hotel")
    
    

class Room(Base):
    __tablename__ = "rooms"
    id = Column(Integer , primary_key=True)
    hotel_id = Column(Integer , ForeignKey("users.id"))
    room_number = Column(String)
    price = Column(Float)
    capacity = Column(Integer)
    hotel = relationship("Hotel" , back_populates='rooms')
    bookings = relationship("Booking" , back_populates="room")
    

class Booking(Base):
    __tablename__= "bookings"
    
    id = Column(Integer , primary_key=True)
    user_id = Column(Integer , ForeignKey("user.id"))
    room_id = Column(Integer , ForeignKey("rooms.id"))
    start_date = Column(Date)
    end_date = Column(Date)
    
    user = relationship("User", back_populates="bookings")
    room = relationship("Room" , back_populates="rooms")
    
#------------------------------------------------------------------------------------------------------------------------

# Generic Repo

from sqlalchemy.orm import Session

class GenericRepository:
    def __init__(self , session:Session , model):
        self.session = session
        self.model = model
    
    
    def add(self, entity):
        self.session.add(entity)
        
    
    def get_by_id(self, id_):
        return self.session.query(self.model).get(id_)
    
    def list_all(self):
        return self.session.query(self.model).all
    
    
    def delete(self , entity):
        return self.session.delete(entity)
    
    
#------------------------------------------------------------------------------------------------

# Specific Repository


class UserRepository(GenericRepository):
    def __init__(self , session):
        super().__init__(session , User) 
        
    def get_by_email(self , email : str):
        return self.session.query(self.model).filter(self.model.email == email).first()
    


class HotelRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session , Hotel)


class RoomRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(self , Room)
        
    
    def get_available_rooms(self, hotel_id : str , start_date , end_date):
        
        booked_rooms = self.session.query(Booking.room_id)\
            .filter(Booking.start_date <= end_date, Booking.end_date >= start_date)
        return self.session.query(Room)\
            .filter(Room.hotel_id == hotel_id, ~Room.id.in_(booked_rooms)).all()
            
            
            


class BookingRepository(GenericRepository):
    def __init__(self , session):
        super().__init__(session , Booking)
        
    
    
    def get_booking_by_user(self , user_id : str):
        return self.session.query(Booking).filter(Booking.user_id == user_id).all()    
    





#---------------------------------------------------------------------------------------------------------------

# Unit Of Work

class UnitOfWOrk:
    def __init__(self, session):
        self.session  = session
        self.users = UserRepository(session)
        self.hotels = HotelRepository(session)
        self.rooms = RoomRepository(session)
        self.bookings = BookingRepository(session)
        
        
        
        
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.session.rollback()
        else:
            self.session.commit()
        self.session.close()    
        



#------------------------------------------------------------Business Logic 

class BookingService:
    def __init__(self , uow:UnitOfWOrk):
        self.uow = uow
        
        
    def book_now(self, user_email :str , hotel_id : int , room_id : int , start_date , end_date):
        user = self.uow.users.get_by_email(user_email)
        
        if not user:
            raise ValueError("User not Found")
        
        room = self.uow.rooms.get_by_id(room_id)
        
        if not room or room.hotel_id != hotel_id:
            raise ValueError("Invalid Room or Hotel")
        
        available_rooms = self.uow.rooms.get_available_rooms(hotel_id, start_date, end_date)
        if room not in available_rooms:
            raise ValueError("Room not available for given dates")

        booking = Booking(user_id=user.id, room_id=room.id, start_date=start_date, end_date=end_date)
        self.uow.bookings.add(booking)
        return booking
        
        
        


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date

engine = create_engine("sqlite:///hotel_booking.db", echo=True)
SessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

# Create a user, hotel, room first
session = SessionLocal()
user = User(name="Alice", email="alice@example.com")
hotel = Hotel(name="Sea View", location="Goa")
room = Room(hotel=hotel, room_number="101", price=200, capacity=2)
session.add_all([user, hotel, room])
session.commit()
session.close()

# Booking
session = SessionLocal()
with UnitOfWOrk(session) as uow:
    service = BookingService(uow)
    booking = service.book_room("alice@example.com", hotel.id, room.id, date(2025,9,20), date(2025,9,22))
    print("Booking Successful:", booking.id)
        
            
                    
        
                                    
                          

        
        
    