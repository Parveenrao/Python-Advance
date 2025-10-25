# Lets start with create  a database connection 

from sqlalchemy import create_engine

# Sqlite database for file based 

# Option 1: File in current folder
engine = create_engine("sqlite:///students.db", echo=True)

# Option 2: File with absolute path
#engine = create_engine("sqlite:////C:/Users/Parveen/mydb.db", echo=True)

# Option 3: In-memory
#engine = create_engine("sqlite:///:memory:", echo=True)

# sqlite:///<path_to_file>

# Define A Tabel 


from sqlalchemy import Table , Column , Integer , String , MetaData

metadata = MetaData()

"""" SQLAlchemy, MetaData is like a "catalog" or "blueprint" that stores information about your database schema (tables, columns, constraints, relationships).

Think of it as a container that keeps track of all the tables you define."""


# Define a core table 

student = Table("students" , metadata , 
                
                Column("id" , Integer , primary_key=True),
                Column("name" , String , nullable=False),  # columns cannot store null values
                Column('age' , Integer))

# Create the tabel in database 

metadata.create_all(engine)


# Now table is crate in student database , so we insert the data inside tha table 

from sqlalchemy import insert

with engine.connect() as conn:
    conn.execute(insert(student).values(name = "Parveen" , age = 22)),
    conn.execute(insert(student).values(name = 'Nirmala' , age =26 ))
    conn.commit()
    
    
    
# select the data

from sqlalchemy import select

with engine.connect() as conn:
    result = conn.execute(select(student))    
    
    for row in result:
        print(row)
    