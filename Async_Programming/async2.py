# gather and # create_task functio in async.io

# gather ---> runs multiple  coroutine cocurrentlt and wait until all finish , Return result in the same order as input


import asyncio


"""async def task(name, sec):
    print(f"{name} started")
    await asyncio.sleep(sec)
    print(f"{name} finished")
    print(f"{name} result")
    
    
async def main():
    result =await asyncio.gather(
        task("task1" , 2),
        task("task2" , 1),
        task("task3" , 3)
        
    )
    
    print(f"results{result}")
    

asyncio.run(main())"""





"""asyncio.create_task()

Schedules a coroutine to run “in the background”.

Immediately returns a Task object (like a future/promise).

You can await it later or run other code while it works.

Useful when you don't want to wait for tasks immediately."""



async def task(name , sec):
    print(f"{name} started")
    await asyncio.sleep(sec)
    print(f"{name} finished")
    return f"{name} result"





async def main():
    t1 = asyncio.create_task(task('task1' , 2))
    t2 = asyncio.create_task(task('task2' , 1))
    
    
    print("Doing Something else")
    
    await t1
    await t2 
    


asyncio.run(main())    
    
                             
