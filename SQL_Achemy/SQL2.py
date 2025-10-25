# CRUD OPERation 

from sqlalchemy import insert , select , delete , update , Column , String , Integer , Table , MetaData , create_engine

# Create a engine(Database estalished / connection )

engine = create_engine("sqlite:///students.db" ,echo = True )

metadata = MetaData()


# create a teacher table 

teacher = Table("teachers" , metadata , 
                
                Column('id' , Integer , primary_key=True),
                Column('Name' , String , nullable=False),
                Column('Subject' , String , nullable=  False))


metadata.create_all(engine)


# Insert data into table 

with engine.connect() as conn:
    conn.execute(insert(teacher).values(Name = "Jyoti Bhardwaj" , Subject = "Deep Learning")),
    conn.execute(insert(teacher).values(Name = 'Devender Prasad' , Subject = 'Data Structure And Algorithms'))
    
    conn.commit()
    
# select the data

with engine.connect() as conn:
    result = conn.execute(select(teacher))
    
    for row in result:
        print(row)    
        
        
# update data

with engine.connect() as conn:
    smt = update(teacher).where(teacher.c.Name == "Jyoti Bhardwaj").values(Subject = "Machine Learning")
    conn.execute(smt)
    conn.commit()
    
    


# delete Data

with engine.connect() as conn:
    smt = delete(teacher).where(teacher.c.Name == "Devender Prasad")
    conn.execute(smt)
    conn.commit()
    
    
    
