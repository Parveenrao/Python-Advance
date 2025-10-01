import asyncio
import time
import random



async def background_task():
    print("Background task started")
    await asyncio.sleep(5)
    print("Background task finished")
    return "Done"





async def main():
    try:
        # cancel main early 2 sec , but shield keeep task running
        
        result = await asyncio.wait_for(asyncio.shield(background_task()) , timeout=2)
        print('Result' , result)
        
    except asyncio.TimeoutError:
        print("Main thread timeout , but background is still runing")
        await asyncio.sleep(5)   # wait we see background running 
        
        

asyncio.run(main())          
