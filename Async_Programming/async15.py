# Semaphorre ---> allowing n request at a time 

# example limited databse connection 


import asyncio

sem = asyncio.Semaphore(2)


async def connection(name , delay):
    async with sem:
        print(f"{name} : connecting to DB")
        await asyncio.sleep(delay) # stimulate query
        print(f"{name} : done")
        
        
        
async def main():
    tasks = [
        (connection('query1' , 2)),
        (connection('query2' , 1)),
        (connection('query3' , 3)),
        (connection('query4' , 2))
    ]   
    
    await asyncio.gather(*tasks)
    
asyncio.run(main())    