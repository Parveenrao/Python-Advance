from sqlalchemy import Column , Integer , String , ForeignKey  ,create_engine , Float , func
from sqlalchemy.orm import sessionmaker , relationship , declarative_base


# create in memory db 
engine = create_engine('sqlite:///:memory:', echo=True)

Base = declarative_base()

class Employee(Base):
    __tablename__ = "employees"
    id  = Column(Integer , primary_key=True)
    name = Column(String)
    department = Column(String)
    salary = Column(Float)
    
    
Base.metadata.create_all(engine)

Session = sessionmaker(bind  = engine)

session = Session()


# Insert some sample employees
employees = [
    Employee(name="Alice", department="IT", salary=70000),
    Employee(name="Bob", department="IT", salary=80000),
    Employee(name="Charlie", department="HR", salary=50000),
    Employee(name="David", department="HR", salary=60000),
    Employee(name="Eve", department="Finance", salary=90000)
]


session.add_all(employees)

session.commit()


# count no of emplolyes

n_employee = session.query(func.count(Employee.id)).scalar()
print(n_employee)

# sum of salaries 

sum_salary = session.query(func.sum(Employee.salary)).scalar()
print(sum_salary)


#Average Salary
avg_salary = session.query(func.avg(Employee.salary)).scalar()
print("Average salary:", avg_salary)

# Max and Min Salary
max_salary = session.query(func.max(Employee.salary)).scalar()
min_salary = session.query(func.min(Employee.salary)).scalar()
print("Max salary:", max_salary)
print("Min salary:", min_salary)


# Group  by department (sum salary per deptartment)


n_group = session.query(Employee.department , func.sum(Employee.salary).label('total salary')).group_by(Employee.department).all()

print(n_group)



# lets say we want sum of salary in it dept

it_salary = session.query(func.sum(Employee.salary).filter(Employee.department == "IT")).all()
print(it_salary)

# count employee greater than salary > 60000

n_greater = session.query(func.count(Employee.id).filter(Employee.salary > 60000)).scalar()
print(n_greater)

# Max salary in Hr deptartment 

n_max_hr = session.query(func.max(Employee.salary).filter(Employee.department == "HR")).scalar()
print(n_max_hr)

# average salary in it dept

n_average_it = session.query(func.avg(Employee.salary).filter(Employee.department == "IT")).scalar()
print(n_average_it)