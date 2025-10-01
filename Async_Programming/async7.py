# Producer - Concumer Example E-commerce Order Processing

import asyncio
import random


async def customer(queue , customer_id):
    for i in range(2):                   #-----> each customer place two order
         order =  f"Customer -{customer_id} --->Order{i+1}"
         print(f'{customer_id} placed order')
         await queue.put(order)
         print(f"{customer_id}--placed--{order}")
         await asyncio.sleep(random.uniform(0.5 ,1.0))    # time between orders
         
    await queue.put(None)     
          
          

async def warehouse_worker(queue , worker_id):
    while True:          
        
        order = await queue.get()
        
        if order is None:
            break
        
        
        print(f"Worker---{worker_id} start processing --{order}")
        
        await asyncio.sleep(random.uniform(1 ,2)) # Time to pack order
        
        
        print(f"Worker---{worker_id} finishes---{order}")
        
        
        


async def main():
    queue = asyncio.Queue()
    
    producers = [customer(queue , i) for i in range(1 , 3)]
    consumers = [warehouse_worker(queue , i) for i in range(1 ,3)]
    
    
    await asyncio.gather(*producers , *consumers)
    

asyncio.run(main())    
    
    
    
    
            
            