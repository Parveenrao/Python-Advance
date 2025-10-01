# Sometim you want to start the task , but want to stop before it finish 

# 1 Task cancellation example 

import asyncio
import time



async def long_task():
    try:
        print("Task Started")
        await asyncio.sleep(10)
        print("Task finished")
    
    except asyncio.CancelledError:
        print("Task was cancelled")
        
        
        
async def main():
    task = asyncio.create_task(long_task())
    await asyncio.sleep(2)
    task.cancel()
    await task
    


asyncio.run(main())                



# Time out example    --->

# example if api call takes very long time cancell it , web scrapping tookes long time to scrap , move on 

async def slow_task():
    print("Slow task started")
    await asyncio.sleep(10)
    print('Slow task finished')
    return "Done"



async def main():
    try:
        result = await asyncio.wait_for(slow_task() , timeout=2)
        print(result)
    
    
    except asyncio.TimeoutError:
        print("Time out")
        
        
asyncio.run(main())           
        
        
        
# Now combination of both timeout and cancellation 


async def job():
    try:
        print("Job Started")
        await asyncio.sleep(10)
        print("Job Finished")      
        
    except asyncio.CancelledError:
        print("Job Cancelled")
        
        
        
async def main():
    task = asyncio.create_task(job())
    try:
        await asyncio.wait_for(task , timeout=2)
    
    except asyncio.TimeoutError:
        print("Job Exceed time")
        


asyncio.run(main())            
                  