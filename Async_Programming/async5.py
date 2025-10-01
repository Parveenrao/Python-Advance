# sometimes when u cancel a parent task , the child task also cancelled

# but sometime we want to run child task to run if the parent task is cancelled

# If you don’t want a long-running operation to be cancelled just because a parent timed out.

import asyncio

async def worker():
    print('Worker started')
    await asyncio.sleep(5)
    print('Worker finished')
    return 'done'
    
    
    
async def main():
    try:
        result = await asyncio.wait_for(worker() , timeout=2)
        print(result)
        
    except asyncio.TimeoutError:
        print("Time Limit , Cancelled")
        
        
asyncio.run(main())


""" Worker finished never appear  , because it cancelled"""

# so to run the child task we use shield()




async def worker():
    print('Worker started')
    await asyncio.sleep(5)
    print('Woker finished')
    return "done"

async def main():
    try:
        result = await asyncio.wait_for(asyncio.shield(worker()) , timeout= 2)
    
        print(result)
    
    
    except asyncio.TimeoutError:
        print("Time Limit Exceed")    
        
        await asyncio.sleep(5)
        
        
        


asyncio.run(main())        