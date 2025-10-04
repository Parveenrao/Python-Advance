""" Queue is FIFO Data structure that allows multiple process to safely exchange data 
    User for producer consumer data 
    No need for explicit lock"""



from multiprocessing import Process , Queue

def producer(q):
    for i in range(5):
        q.put(i) 
        print(f"Produced {i}") 

def consumer(q):
    while not q.empty():
        item = q.get()
        print(f"Consumed {item}")
        


if __name__ == "__main__":
    q = Queue()
    
    p1 = Process(target=producer , args=(q,))
    p2 = Process(target=consumer , args=(q,)) 
    
    p1.start()
    p1.join()
    
    p2.start()
    p2.join()       
