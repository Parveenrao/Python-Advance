"""" Python Concurrent Features 
     Concurrent features is all about making parallelism and concurrency easier
     
     You have to create, start, and manage each Thread manually.

     If you have 100 tasks, you need to manage 100 threads. That’s messy.
     
     Thats why we need threadpoolexecutor and poolexeccutor 
     
     """
     
     
from concurrent.futures import ThreadPoolExecutor

def square(n):
    return n * n


with ThreadPoolExecutor(max_workers=3) as executor:
    future = executor.submit(square , 5) 
    print(future.result())    
     
#---------------------------------------------------------------------------
# map for multiple task at once

def square(n):
    return n * n
    
with ThreadPoolExecutor() as  executor:
    future = executor.map(square , [1, 2, 3, 4, 5])
    print(list(future))


#---------------------------------------------------------------------------

              
"""Asynchronous Task Handling

Use as_completed to process results as soon as they're done:"""


from concurrent.futures import ThreadPoolExecutor, as_completed
import time, random

def work(n):
    time.sleep(random.randint(1, 3))
    return n

with ThreadPoolExecutor() as executor:
    futures = [executor.submit(work, i) for i in range(5)]
    for future in as_completed(futures):
        print(f"Task completed with result {future.result()}")

              
              
              