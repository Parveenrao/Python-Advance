"""ProcessPoolExecutor?

It is part of concurrent.futures.

Runs tasks using a pool of worker processes (not threads).

Each process has its own Python interpreter and memory space.

This bypasses the GIL, making it ideal for CPU-bound tasks (e.g., image processing, ML training, simulations, heavy math)."""

import sys
sys.set_int_max_str_digits(0)  # 0 means "no limit"


from concurrent.futures import ProcessPoolExecutor
import math


def compute_factorial(n):
    return math.factorial(n)


if __name__=="__main__":
    numbers = [1000 , 2000 , 3000 , 4000]
    
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = executor.map(compute_factorial , numbers)
        print(list(results))
    
    
    
#--------------------------------------------------------------------------------------------------

from concurrent.futures import ProcessPoolExecutor, as_completed
import time

def work(n):
    time.sleep(2)
    return n * n

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(work, i) for i in range(5)]

        for future in as_completed(futures):
            print("Result:", future.result())
    
    