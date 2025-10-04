# Semaphore ----> allow a fixed no of process to access a resource simultaneously

from multiprocessing import Process , Semaphore
import time 

def worker(sem , i):
    print(f"Process {i} waiting for semaphore")
    with sem:
        print(f"Process {i} entered")
        time.sleep(1)
        print(f"Process {i} leaving")


if __name__=="__main__":
    sem = Semaphore(2)
    
    processes = [Process(target=worker , args=(sem , i)) for i in range(5)]
    
    for p in processes:
        p.start()
    
    for p in processes:
        p.join()            
        
        
"""  What is a BoundedSemaphore?

A BoundedSemaphore is like a Semaphore, but with a safety check:

You can acquire it up to a maximum count.

You cannot release it more times than it was acquired."""        