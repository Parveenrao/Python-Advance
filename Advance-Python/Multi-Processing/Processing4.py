#  Manager -----> In multi-processing each memory  have  its own memory and  space 
# Normal python objects like lst dict cant be shared between process 

# So Manager come into play ,,, create shared objects that can be shared accessed and modified by multiple processess

from multiprocessing import Pool , Process , Manager

def worker(shared_list , value):
    shared_list.append(value)
    
    
if __name__== "__main__": 
    manager = Manager()            # create list
    shared_list = manager.list()   # create a shared list      # manager.dict()   Create shared dictionary  , manager.value - single value
    
    
    processes = []
    
    for i in range(5):
        p = Process(target=worker , args=(shared_list , i))
        p.start()
        processes.append(p)
        
    
    for p in processes:    
        p.join()
        
    
    print(shared_list)   
    
#-----------------------------------------------------------------------------------------------------------------

def worker_dict(shared_dict, key, value):
    shared_dict[key] = value

if __name__ == "__main__":
    manager = Manager()
    shared_dict = manager.dict()

    processes = []
    for i in range(5):
        p = Process(target=worker_dict, args=(shared_dict, f'key{i}', i*10))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    print(shared_dict)
    # Output: {'key0': 0, 'key1': 10, 'key2': 20, 'key3': 30, 'key4': 40}
     