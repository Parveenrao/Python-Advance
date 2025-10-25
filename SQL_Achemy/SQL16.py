# Window Function -----> Rank --- Row Number ---- Lag ----Lead

from sqlalchemy import(Column , String , Integer , create_engine , ForeignKey , func )
from sqlalchemy.orm import declarative_base , Session

Base = declarative_base()

class Sale(Base):
    __tablename__ = 'sales'
    
    id = Column(Integer , primary_key=True)
    employee = Column(String)
    region = Column(String)
    amount = Column(String)
    


engine = create_engine("sqlite:///example8.db" , echo=True , future=True)

Base.metadata.create_all(engine)

# Insert dummy data

with Session(engine) as session:
    session.add_all([
        Sale(employee="Alice", region="North", amount=500),
        Sale(employee="Bob", region="North", amount=300),
        Sale(employee="Charlie", region="North", amount=700),
        Sale(employee="Alice", region="South", amount=200),
        Sale(employee="Bob", region="South", amount=400),
    ])  
    
    
    session.commit()
    
# Row Number ---> Assign unique number per row in partition

from sqlalchemy import over

query = session.query(Sale.employee , Sale.region , Sale.amount , func.row_number().over(partition_by=Sale.region ,
        order_by=Sale.amount.desc()).label("row_num"))      
    
    
for row in query:
    print(row)    
    
    
#---------------rank()----Similar to row_number but ties get same rank    
with Session(engine) as session:
    query = session.query(
        Sale.employee,
        Sale.region,
        Sale.amount,
        func.rank().over(
            partition_by=Sale.region,
            order_by=Sale.amount.desc()
        ).label("rank")
    )
    for row in query:
        print(row)


""" lag() and lead()

lag() → look at the previous row.

lead() → look at the next row."""



with Session(engine) as session:
    query = session.query(
        Sale.employee,
        Sale.region,
        Sale.amount,
        func.lag(Sale.amount, 1).over(
            partition_by=Sale.region,
            order_by=Sale.amount
        ).label("prev_amount"),
        func.lead(Sale.amount, 1).over(
            partition_by=Sale.region,
            order_by=Sale.amount
        ).label("next_amount"),
    )

    for row in query:
        print(row)
