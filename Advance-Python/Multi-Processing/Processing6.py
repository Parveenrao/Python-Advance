""" Pipe ---> Is a direct communication between two processes 
    Can be duplex and half way 
    Used to send and recieve data
    Fastet than queue"""
    

from multiprocessing import Process , Pipe

# Basic Example two way communicaton 

def worker(conn):
    # Recieve msg from parent
    msg = conn.recv()
    print(f"Worker received {msg}") 
    
    # Send reply back
    
    conn.send("Hello from worker")
    conn.close()
    

if __name__ == "__main__":
    parent_conn, child_conn = Pipe()
    p = Process(target=worker, args=(child_conn,))
    p.start()

    # Send message to child
    parent_conn.send("Hello from parent")

    # Receive reply from child
    print(f"Parent received: {parent_conn.recv()}")

    p.join()
    
#--------------------------------------------------------------------------------------------------------------

# One way communication only parent can send msg

from multiprocessing import Process, Pipe

def worker(conn):
    msg = conn.recv()
    print(f"Worker received: {msg}")

if __name__ == "__main__":
    parent_conn, child_conn = Pipe(duplex=False)  # only parent can send
    p = Process(target=worker, args=(child_conn,))
    p.start()

    parent_conn.send("Message to worker")
    p.join()
    
           