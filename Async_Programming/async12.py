# Producer - Consumer 

"""Producer puts 10 items into a queue.

3 Consumers process items concurrently.

Each consumer should log which item it processed."""


import asyncio
import random


async def producer(queue :asyncio.Queue):
    for i in range(10):  # puts 10 items in the queue
        await asyncio.sleep(random.uniform(0.1 , 0.5)) # network delay 
        await queue.put(i)
        
        print(f"Produced items{i}")
        
        
        # signal to stop producer
        
    for _ in range(3):
        await queue.put(None) 
        
        
        
async def worker(queue:asyncio.Queue , name:str):
    while True:
        item = await queue.get()
        if item is None:
            break
        
        
        
        await asyncio.sleep(random.uniform(0.5, 1.5))
        print(f"Consumer{name} processed item{item}")
        
        
        


async def main():
    queue = asyncio.Queue()
    
    producers = asyncio.create_task(producer(queue))
    consumers = [asyncio.create_task(worker(queue , f"C{i}")) for i in range(3)]
    
    
    await producers
    await asyncio.gather(*producers , *consumers)
    
    
    
asyncio.run(main())    
    
                       
    