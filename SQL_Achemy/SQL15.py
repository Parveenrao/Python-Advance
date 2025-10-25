# Salary Management System

from sqlalchemy import (Column , Integer , String , Date , create_engine , func , case , Float)

from sqlalchemy.orm import session , sessionmaker , declarative_base

from sqlalchemy.ext.hybrid import hybrid_method , hybrid_property

from datetime import time , date

Base = declarative_base()


class Employee(Base):
    __tablename__ = 'employees'
    
    id = Column(Integer , primary_key=True)
    name = Column(String)
    base_salary = Column(Float)
    bonus = Column(Float)
    tax = Column(Float)
    joining_date = Column(Date)
    
    #------------Hybrid Propert for net salary
    
    @hybrid_property
    def net_salary(self):
        return self.base_salary + self.bonus - self.tax
    
    @net_salary.expression
    def net_salary(cls):
        return cls.base_salary + cls.bonus - cls.tax
    
    #-------------Hybrid Property for tax percentage
    
    @hybrid_property
    def tax_percentage(self):
        return (self.tax / (self.base_salary + self.bonus)) * 100
    
    @tax_percentage.expression
    def tax_percentage(cls):
        return (cls.tax / (cls.base_salary + cls.bonus)) * 100
    
    
    #----------------Hybrid method for high earner
    
    @hybrid_method
    def is_high_earner(self ,threshold = 100000):
        return self.net_salary > threshold
    
    @is_high_earner.expression
    def is_high_earner(cls , threshold = 100000):
        return (cls.base_salary + cls.bonus - cls.tax)  > threshold
    
    
    #----------------Hybrid propertyh for year of experience
    
    @hybrid_property
    def years_experience(self):
        return (date.today().year - self.joining_date.year)
    
    
    @years_experience.expression
    def years_experience(cls):
        return func.strftime("%Y", func.current_date()) - func.strftime("%Y", cls.joining_date)
    
    
    
#---------------------------Setup

engine  = create_engine("sqlite:///example7.db" , echo=True , future=True)

Base.metadata.create_all(engine)

Session = sessionmaker(engine)

session = Session()


#-----------------------------Insert Employees

session.add_all([
     Employee(name="Alice", base_salary=90000, bonus=10000, tax=15000, joining_date=date(2018, 5, 1)),
    Employee(name="Bob", base_salary=120000, bonus=20000, tax=25000, joining_date=date(2015, 3, 15)),
    Employee(name="Charlie", base_salary=50000, bonus=5000, tax=8000, joining_date=date(2020, 7, 10)),
])
    
session.commit()


#---------------------Instance Level 

# --- Usage ---
# 1. Instance level
e = session.query(Employee).first()
print("Name:", e.name)
print("Net Salary:", e.net_salary)               # Python computation
print("Tax %:", round(e.tax_percentage, 2))
print("Experience:", e.years_experience, "years")
print("Is high earner:", e.is_high_earner(100000))

# 2. Sql query level 

# find all high earners 

high_earners = session.query(Employee).filter(Employee.is_high_earner(100000)).all()
print("\nHigh Earners:",[emp.name for emp in high_earners])

#Order employee by net salary 

ordered_employee = session.query(Employee).order_by(Employee.net_salary.desc()).all()
print("Ordered by Net Salary:", [(emp.name, emp.net_salary) for emp in ordered_employee])