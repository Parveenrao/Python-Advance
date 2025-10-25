from sqlalchemy import create_engine, Column, Integer, String, ForeignKey , func
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# Base
Base = declarative_base()

# Department Table
class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=False, nullable=False)

    # One-to-many relationship: A department has many employees
    employees = relationship("Employee", back_populates="department")

# Employee Table
class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    salary = Column(Integer)
    department_id = Column(Integer, ForeignKey('departments.id'))

    # Relationship back to department
    department = relationship("Department", back_populates="employees")



engine = create_engine('sqlite:///company2.db', echo=True)
Base.metadata.create_all(engine)

# Session
Session = sessionmaker(bind=engine)
session = Session()


# Create Departments
dept1 = Department(name="HR")
dept2 = Department(name="Engineering")

# Create Employees
emp1 = Employee(name="Alice", salary=50000, department=dept1)
emp2 = Employee(name="Bob", salary=60000, department=dept2)
emp3 = Employee(name="Charlie", salary=55000, department=dept2)

# Add to session
session.add_all([dept1, dept2, emp1, emp2, emp3])
session.commit()



# Get Employee with Dept Names 


query1 = session.query(Employee.name , Employee.salary , Department.name.label("dept_name")).join(Department, 
                     Employee.department_id == Department.id).all()


print(query1)


# Get all the employee who is working on engineering dept

query2 = session.query(Employee.name , Department.name).join(Department , Employee.department_id == Department.id).filter(
    Department.name == "Engineering"
).all()

print(query2)


# Employyee earning more than 50000

query3 = session.query(Employee.name , Employee.salary).filter(Employee.salary > 5000).all()

print(query3)


# get the no of employee in each department 

query4 = session.query(Department.name , func.count(Employee.id)).join(Employee).group_by(Department.id).all()
print(query4)

# find max salary in each department 

query5 = session.query(Department.name , func.max(Employee.salary)).join(Employee).group_by(Department.id).all()

print(query5)

# Get Deptartment with more than one employeee

query6 = session.query(Department.name  , func.count(Employee.id)).join(Employee).group_by(Department.id).having(
                         func.count(Employee.id) > 1).all()

print(query6)


# Sum of salaries per dept

query7 = session.query(Department.name , func.sum(Employee.salary)).join(Employee).group_by(Department.id).all()

print(query7)