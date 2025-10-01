# Synchronization Primitive in asynchronous Programming

""" What are they and why we need them  
     In async program multiple coroutines run concurrently on the same thread.
     Synchronization primitive coordinate access to shared state , control concurrency and let corountine wait for signal
     so you avoid race conditions, lost update , deadlock and uncontrolled usage.)"""
     
     
     
# 1. async.lock()
# A mutual-exclusion lock only one task may hold in one time


import asyncio

lock = asyncio.Lock()

shared_counter = 0


async def increment():
    global shared_counter
    
    async with lock:            # safe atuotmatically release on cancel and exception                    
        tmp = shared_counter
        await asyncio.sleep(0)
        shared_counter = tmp+1
        
        
async def main():
    await asyncio.gather(*(increment() for _ in range(100)))
    print(shared_counter)
    
    
asyncio.run(main())    



"""Asyncio.Event
# event are simple signal that can wait on is has wait() set() and clear() mathods

# think like of traffic signl  where car is task and  cars can wait() at signal , when someone call set() signal turns green --> all waiting task move forward
# event stays green until someone says clear()

Key methods

event = asyncio.Event() → create an Event (initially red = not set).

await event.wait() → task will pause until the Event is set.

event.set() → turn signal green, wake up all waiting tasks.

event.clear() → turn signal red again.

event.is_set() → check if the Event is green."""

import asyncio 

event   = asyncio.Event()

async def worker(name):
    print(f"{name} is waiting")
    await event.wait()  # wait until event.set() is called
    print(f"{name} is finished") 
    


async def main():
    # starting two task that will wait
    asyncio.create_task(worker('TaksA'))
    asyncio.create_task(worker("TaskB"))
    
    print("Main is doing some work")
    
    await asyncio.sleep(2)
    
    print("Main sets the event(turn signal green)")
    
    event.set()
    
    
    
asyncio.run(main())    




# clear and reuse

import asyncio 
event = asyncio.Event()


async def worker():
    while True:
        print("Worker waiting....")
        await event.wait()
        print("Worker running...")
        await asyncio.sleep(1)
        event.clear()          # must wait again
        
        

async def main():
    asyncio.create_task(worker())
    await asyncio.sleep(1)
    
    print("Signal Green") 
    event.set()
    await asyncio.sleep(2)
    
    print("Signal Green Again")
    event.set()
    await asyncio.sleep(2)
    
    
asyncio.run(main())           
           
            
# Async.condition            

"""Imagine a canteen with food trays:

There is a door lock (🔒) — only one person can check the trays at a time.

If a consumer comes but no tray is available, they wait outside the canteen.

When a producer puts food on the tray, they shout “notify!” → a waiting person wakes up and enters.

That's exactly what Condition does:

It gives exclusive access (lock).

It lets consumers wait until the producer notifies them"""


import asyncio

con = asyncio.Condition()

buffer = []

async def consumer():
    async with con:                           #  acquire lock before waiting
        print("Consumer waitinfg for item")
        await con.wait()                      # release lock , waits for notify
        
        print("Consumer: got item" , buffer.pop())
        
        
async def producer():
    await asyncio.sleep(1)
    async with con:
        buffer.append("item")
        print("Producer adde item")
        con.notify()
        
async def main():
    await asyncio.gather(consumer() , producer())
    
    
asyncio.run(main())            
                