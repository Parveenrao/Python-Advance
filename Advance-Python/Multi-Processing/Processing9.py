# Event is a signal mechanism that is used between process

# event is a flag that can se set  or cleared

from multiprocessing import Event , Process
import time

def worker(e):
    print("Worker waiting for event")
    e.wait()    # waiting for event to be set
    print("Worker received event , Working now")
    

if __name__=="__main__":
    event = Event()
    process = Process(target=worker , args=(event,))
    
    process.start()
    
    time.sleep(2) 
    
    print("Main process setting event")
    
    event.set()
    
    process.join()  