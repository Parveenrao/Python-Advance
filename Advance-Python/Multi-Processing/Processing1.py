import os 

print("cpu_count" , os.cpu_count())

#----------------------------------------------------------------------------------------

# lets start with a basic example which count number upto a given range 

import time

def count_number(n):
    for i in range(1 , n+1):
        pass
    
    
start = time.time()

count_number(10**7)
count_number(10**7)   

end = time.time()

print("Total Time Taken",  end-start)

#------------------------------------------------------------------------------------------

# Now same function with Multiprocessing

from multiprocessing import Process
import time 


def count1_number(n):
    for i in range(1 , n+1):
        pass
    
    
 
if __name__ == "__main__":
    
    # creat two process 
    p1 = Process(target=count1_number , args=(10**7 ,))
    p2 = Process(target=count1_number , args=(10**7,))
    
    start = time.time()
    
    # Start Processes
    
    p1.start()
    p2.start()
    
    # wait for processes to finish
    
    p1.join()
    p2.join()
    
    
    end = time.time()
    
    print("Total Time Taken" , end-start)
    
    

    