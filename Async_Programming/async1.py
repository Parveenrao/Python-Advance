# first understand what is concurrency -----> concurrency means doing multiple things at same tine but in cooordinate way

""" For example you are cook 
    1. Boil water (10 mins)
    2. chopping water (5 mins)
    So instead of waiting 10 mins for the water to boil , chopping vegetables"""
    
# Concurrency != Parrallelism    

# If you had tow cooks one is boiling water and other  is chopping vegies at the same instant  , thats the parallelism


#Concurrency is about dealing with a lot of things at once.
#Parallelism is about doing a lot of things at the same time.


"""What is Async Programming?

Async = a way to write concurrent programs.

Instead of blocking (waiting) for one task to finish, async lets other tasks run while one is waiting.

It's especially useful for I/O-bound tasks (network requests, file read/write, database queries).

Async is not parallelism → It doesn't use multiple CPU cores. Instead, it uses a single thread + event loop."""

#async keyword

#Defines an asynchronous function (called a coroutine).


import asyncio

async def fetch_data():       # coroutine function 
    print("Fetching data...")


#await keyword

#Pauses the coroutine until the awaited task is done.

#While waiting, the event loop can switch to another task.


async def fetch_data():
    await asyncio.sleep(2)
    return "data"




import asyncio
import time

async def main():
    result = await fetch_data()
    print(result)

asyncio.run(main())




# now example Synchronous function

def download_file(file):
    print(f"Downloading {file}")
    time.sleep(2)
    print(f"{file} Downloaded")
    
    
    
def main():
    download_file("file1")
    download_file("file2")
    
main()        
    
    
# async function 

async def download_file(file):
    print(f"Downloading {file}")
    await asyncio.sleep(2)
    print(f"{file} Downloaded")
    
    
    
async def main():
    await asyncio.gather(
        download_file("file1"),
        download_file("file2")
    )    
        


asyncio.run(main())