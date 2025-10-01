# queue in async programming  

"""Async.queue is a thread safe pipeline between consumer and producer

Producer --> add items into the queue await quque.put(item)

Consumer --> take order from the queue   await queu.get(item)

This queue make sure that data is processed in order of FIFO


If queue is empty , consumer wait automatically unttil something arrives """


""" Real life example --- Imagine a restaurant kitchen
    
Customers place orders (producers).

Orders are put into the order board (queue).

Chefs pick orders one by one and cook (consumers).

If no orders are there, chefs wait.

If too many orders pile up, new orders may have to wait (bounded queue).  """

import asyncio
import random

async def producer(queue , n):
    for i in range(1 , n+1):
        order = f"Order - {i}"
        await queue.put(order)
        print(f"Producer placed -- {order}")
        
        await asyncio.sleep(random.uniform(0.5 , 1.5))      # order time , some take time to place 0.5 sec some 1.5 sec
        
    await queue.put(None)     # signal consumer to stop
    
    
    

async def consumer(queue):
    while True:
        order = await queue.get()
        
        if order is None:
            break
        print(f"Cosumer started -- {order}")    
        
        await asyncio.sleep(random.uniform(1 ,2))    # cooking time
        
        
        print(f"Consumer finished --- {order}")
        
        
        
async def main():
    queue = asyncio.Queue()
    
    await asyncio.gather(
           producer(queue , 5),
           consumer(queue)
    )
    
    
    
asyncio.run(main())    
    
    


    
        
       
    