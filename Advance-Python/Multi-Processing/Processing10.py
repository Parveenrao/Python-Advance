"""" Condition ----> allows processes to wait for a certain condition"""

from multiprocessing import Condition , Event , Process
import time

def worker(cond , name):
    with cond:
        print(f"{name} is waiting for conditon....")
        cond.wait()  # wait until notified
        print(f"{name} has been notified ! Now working.....")
        
 
if __name__=="__main__":
    cond = Condition()
    
     # Start 2 worker processes
    p1 = Process(target=worker, args=(cond, "Worker-1"))
    p2 = Process(target=worker, args=(cond, "Worker-2"))        
    
    
    
    p1.start()
    p2.start()

    time.sleep(2)
    with cond:  
        print("Main process notifying workers...")
        cond.notify_all()  # wake up all workers

    p1.join()
    p2.join()