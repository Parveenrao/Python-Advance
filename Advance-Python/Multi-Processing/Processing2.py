# Pool , Map , IMAP , Apply_async

# 1. Pool ---> instead of creating processing manually we can use pool which manage pool of workers(with pool(process =4)

# Map --> Return a list of results  , maintain order of the input

# IMAP -->  Return an intertor instead of result , maintain order of input


#-----------------------------------------------------------------------------------------------------------

#MAP

from multiprocessing import Process , Pool
import time 


def square(x):
    time.sleep(1)
    return x * x


if __name__ == "__main__":
    numbers = [1,2,3,4,5]
    
    with Pool(processes=3) as pool:
        results = pool.map(square , numbers)
        
    
    print("Results" , results)    
    
#------------------------------------------------------------------------------------------------------------

#  IMAP  

from multiprocessing import Process , Pool
import time 


def square(x):
    time.sleep(1)
    return x * x


if __name__ == "__main__":
    numbers = [1,2,3,4,5]
    
    with Pool(processes=3) as pool:
        for results in pool.imap(square , numbers):
        
    
            print("Results" , results)    
            
#---------------------------------------------------------------------------------------------------------------------

# Apply Async 

from multiprocessing import Pool
import time 

def square(x):
    time.sleep(1)
    return x * x


if __name__=="__main__":
    numbers = [1 , 2, 3, 5, 4] 
    results = []
    
    
    with Pool(processes=3) as pool:
        for n in numbers:
            r = pool.apply_async(square , args=(n,)) 
            results.append(r) 
            
            
            
        output = [r.get() for r in results]
    
    
    print("Results" , output)                 