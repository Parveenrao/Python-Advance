""" Problem 1 
    Write a corountine that stimulates downloading a file using asyncio.sleep 
    Run 5 downloads in parallel and print when each finish"""
    
    


import asyncio
import time 


async def downloading_file(file_id :int):
    print(f"Start Downloading File {file_id}")
    await asyncio.sleep(2)                           # stimulate download time
    print(f"Finish downloading file{file_id}")
    
    
async def main():
    tasks = [asyncio.create_task(downloading_file(i)) for i in range(1 , 6)]
    await asyncio.gather(*tasks)
    

asyncio.run(main())        