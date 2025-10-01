# now we run multiple task and wait for all 


import asyncio

import time


async def worker(name, sec):
    print(f"{name} started")
    await asyncio.sleep(sec)
    print(f"{name} finished")
    return f"{name} result"



async def main_all():
    task = [
        asyncio.create_task(worker('task1' , 2)),
        asyncio.create_task(worker('task2' , 1)),
        asyncio.create_task(worker('task3' , 3))
        
    ]
    
    result = await asyncio.gather(*task)
    print("All results" , result)
    
    
 



# sometimes u dont need all the one u need the fastest one

async def main_first():
    tasks = [
           worker('fast' , 1),
           worker('medium' , 3),
           worker('fast' , 5),
    ]
    
    
    done , pending = await asyncio.wait(tasks , return_when = asyncio.FIRST_COMPLETED)
    
    for d in done:
        print('First done' , await d)
        
    
    for p in pending:
        p.cancel() 
        


   
asyncio.run(main_all())           
asyncio.run(main_first())        