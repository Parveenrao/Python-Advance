# Barrier allows multiple process to wait unitl reach a certain point 

from multiprocessing import Process , Barrier
import time,  random

def worker(barrier , worker_id):
    print(f"Worker {worker_id} is preparing")
    time.sleep(random.randint(1, 4))
    print(f"WOrker {worker_id} reached the  barrier")
    
    barrier.wait()
    
    print(f"Worker {worker_id} start working after release the barrier")


if __name__=="__main__":
    num_workers = 3
    barrier = Barrier(3)
    
    processes = [Process(target=worker , args=(barrier , i)) for i in range(num_workers)]
    
    for p in processes : p.start()
    for p in processes : p.join()
    