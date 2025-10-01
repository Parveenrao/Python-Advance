# Taskgroup is a way to run multiple async task togther in structured and safe manner

"""  It's a manager for your task 
     
     Start task together 
     Wait until all finish 
     Cancel the group if one fails 
     Prevent 'orphan' task from  hanging in the background"""
     
     
# without taskgroup , you will use use gather but this will not cancel the task if one task fails

# Imagine u want to send emails to 3 person at one time 
# one email to Alice
# one email to bob
# one eamil to charlie    


# If one email fails (e.g., server down), we want to stop the whole batch. That’s exactly what TaskGroup does.

import asyncio

async def send_email(person , delay , fail = False):
    print(f"Sending email to the ---{person}")
    
    await asyncio.sleep(delay)         # network delay
    
    if fail:
        raise RuntimeError(f"Failed to send email to ---{person}")
    
    
    print(f"Email sent to the --- {person}")
    
    
    
async def main():
    try:
        
        async with asyncio.TaskGroup() as tg:
            tg.create_task(send_email('Alice'  ,2))
            tg.create_task(send_email('Bob' , 3 , fail=True))   # bob fails
            tg.create_task(send_email('Charlie' , 1))
            
    except* RuntimeError as e:
        print("Error happend" , e) 
        
        
        
asyncio.run(main())        
               
            
            
    
    