""" Global Intrepreter Lock is a mutex(mutual exclusion lock) used in cpython

1.  GIL ensure that only one thread is excute Python bytecode at a time even on multicore cpu 
    Means if you create multiple thread only one thread can excute python code at a time 
    
2. Why Python Need GIl
   GIL was introduced beacuse of memory management --- Cpython use refercence counting method for garbage collection 
   Reference counting is not thread safe beacuse if two thread update the reference count of an object at the same time 
   it can cause memory corruption 
   
   So even if you create multiple threads in Python, only one thread can run Python code at a time.
   
   So the GIL simplifies the implementation of CPython but limits multithreading performance.
   
   """  
   
   
""""In multiprocessing (using multiprocessing module), each process has its own Python interpreter and its own GIL.
    So true parallelism is possible.

    In C extensions (like NumPy, TensorFlow), the GIL can be released when performing heavy computations in C, 
    allowing real parallelism inside those libraries."""   