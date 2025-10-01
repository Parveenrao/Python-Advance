# Condition lock in async programming

import asyncio

bread = []

con = asyncio.Condition()


async def customer(name : str):
    async with con:
        while not bread:      #  if no bread waiting
            print("f{name}: no bread yet , waiting....")
            await con.wait()
        item = bread.pop(0)
        print(f"{name} :  Got {item}" )





async def baker():
    for i in range(3):
        await asyncio.sleep(1)        # time to bake bread            
        
        async with con:
            bread.append(f"Bread #{i+1}")
            print(f"Baker: Baked bread # {i+1}")
            con.notify()
                
                
async def main():
    await asyncio.gather(customer("bob") , customer("alice") , customer("charlie") , baker())
    
    
asyncio.run(main())                   
            
            