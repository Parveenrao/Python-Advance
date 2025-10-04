"""Lock-  ---> Lock is a synchronization primitve that prevent mulitple process accessing shared data at the same  time

  Only one process can hold lock at  at time , others must wait unitl lock is released"""
  
from multiprocessing import Lock , Process , Value
import time

def worker(lock , counter):
    for _ in range(5):
        time.sleep(0.1)
        with lock:
            counter.value += 1
        
            print(f"Counter value: {counter.value}") 
 

if __name__ =="__main":
    lock = Lock()
    counter = Value('i' , 0) 
    
    processes = [Process(target=worker , args=(lock , counter)) for _ in range(3)]
    
    for p in processes:
        p.start()
    
    for p in processes:
        p.join()    
        
        
    print(f"Final counter value: {counter.value}")              