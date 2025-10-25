from sqlalchemy import create_engine, Column, Integer, String, Float, func
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    department = Column(String)
    city = Column(String)
    salary = Column(Float)
    bonus = Column(Float)
    experience = Column(Integer)


engine = create_engine("sqlite:///company1.db", echo=False)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

employees = [
    Employee(name="Alice", department="HR", city="Delhi", salary=60000, bonus=5000, experience=3),
    Employee(name="Bob", department="IT", city="Delhi", salary=80000, bonus=8000, experience=5),
    Employee(name="Charlie", department="IT", city="Mumbai", salary=95000, bonus=12000, experience=6),
    Employee(name="David", department="Finance", city="Mumbai", salary=88000, bonus=7000, experience=4),
    Employee(name="Emma", department="HR", city="Delhi", salary=70000, bonus=6000, experience=4),
    Employee(name="Frank", department="Finance", city="Pune", salary=76000, bonus=6500, experience=5),
]
session.add_all(employees)
session.commit()


# we have query avergae salary , total bonus , employee count and average experience  
# group by both dept and city and salary where > 7000


"""query = session.query(Employee.department , Employee.city , func.avg(Employee.salary).label('Avg_Salary'), 
                      func.sum(Employee.bonus).label('Total_bonus') , 
                      func.count(Employee.id).label("Emp_count"),
                      func.avg(Employee.experience).label("Avg_Exp")).group_by(Employee.department , Employee.city).having(
                        func.avg(Employee.salary) > 70000
                      ).order_by(func.avg(Employee.salary).desc()).all()
                      
print(query)"""                  




# find the total no of employee in each dept


query1 = session.query(Employee.department , func.count(Employee.id).label("No_Emp")).group_by(Employee.department).all()

print(query1)


# Average salary grouped by city 

query2 = session.query(Employee.city , func.avg(Employee.salary).label("Avg_Salary_City")).group_by(Employee.city).all()
print(query2)

# Max and Min Salary per dept 

query3 = session.query(Employee.city , func.max(Employee.salary).label("Maximum Salary"),
                       func.min(Employee.salary).label("Minimum_Salary")).group_by(Employee.city).all()

print(query3)


# Department having salary hinger than 70000

query4 = session.query(Employee.department , func.avg(Employee.salary).label("Avg_Salary")).group_by(Employee.department).having(
    func.avg(Employee.salary > 70000)
).all()

print(query4)


# avg bonus , experience  and no of emp per dept and city

query5 = session.query(Employee.department , Employee.city , func.count(Employee.id).label("Total_emp"),
                       func.avg(Employee.bonus).label("Avg_bonus"),
                       func.avg(Employee.experience).label("Total_Experience")).group_by(Employee.department , Employee.city).order_by(
                           func.avg(Employee.experience).desc()
                       ).all()
                       
print(query5)                       
                       
                       
                       
                       
# Find all the cities where total bonus > 10000


query6  = session.query(Employee.city , func.sum(Employee.bonus).label("Total_Bonus_Per_city")).group_by(Employee.city).having(
                  func.sum(Employee.bonus) > 10000
    
).all()


print(query6)                      




# Dept - city pair where more than one emp and avg salary > 7000

query7 = session.query(Employee.department, Employee.city ,
                       func.count(Employee.id).label("emp_count"),
                       func.avg(Employee.salary).label("avg_salary")).group_by(Employee.department , Employee.city).having(
                           func.count(Employee.id) > 1
                           
                       ).having(func.avg(Employee.salary) > 70000).all()


print(query7)                       



# Top two dept by total salary pay out 

query8 = session.query(Employee.department , func.sum(Employee.salary).label("total_sal_by_dept")).group_by(
    Employee.department).order_by(func.sum(Employee.salary).desc()).limit(2).all()

print(query8)


# Dept with maximum average experience


query9 = session.query(Employee.department , func.avg(Employee.experience)).group_by(Employee.department).order_by(
    func.avg(Employee.experience).desc()
).limit(1).first()

print(query9)





# Department total performance and sorted  by total  bomus and empoloye > 2

query10 = session.query(Employee.department , 
                        func.count(Employee.id).label("emp_count") , 
                        func.avg(Employee.salary).label("Avg_salar"),
                        func.sum(Employee.bonus).label("Total Bonus"),
                        func.avg(Employee.experience).label("Avg_Experience")).group_by(Employee.department).having(
                            func.count(Employee.id > 2)
                        ).order_by(func.sum(Employee.bonus).desc()).all()
                        
                        
print(query10)                        


# city with highest no of deptarment 

query11 = session.query(Employee.city , func.count(func.distinct(Employee.department))).group_by(
    Employee.city
).order_by(func.count(func.distinct(Employee.department)).desc()).limit(1).first()

print(query11)