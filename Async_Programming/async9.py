# Real time Stock Price Monitor 

"""You're tracking stock prices from multiple APIs.

Each API call might be slow or fail.

You want to:

Fetch all prices concurrently.

Retry failed requests.

Cancel requests if they take too long.

Put results into a queue for further processing (e.g., storing in DB)."""

import asyncio

import random

async def fetch_stock_price(stock):
    await asyncio.sleep(random.uniform(0.5 , 2.0))             # network delay
    
    
    if random.random() < 0.2:                   # twenty chance of failur
    
    
        raise ConnectionError(f"API error fetching {stock}")

    price = round(random.uniform(100 , 500),2)
    
    return f"{stock}: $ {price}"




# retry wrapper with timeout 

async def fetch_with_retry(stock , retries = 3  , timeout = 3):
    
    for attempt in range(1 , retries+1):
        try:
            
            return await asyncio.wait_for(fetch_stock_price(stock) , timeout=timeout)
        
        except (asyncio.TimeoutError, ConnectionError) as e:
            print(f"⚠️ {stock} attempt {attempt} failed: {e}")
            if attempt == retries:
                return f"❌ Could not fetch {stock}"
            await asyncio.sleep(2**(attempt-1))  # exponential backoff
            
            
            


# Producer puts stocks into queue

async def producer(queue , stocks):
    for stock in stocks:
        await queue.put(stocks)
        
    await queue.put(None) 
    
    
    


# consumer fetch data 


async def consumer(queue , worker_id):
    
    while True:
        
        stock = await queue.get()
        
        if stock is None:
            break
        
        result = await fetch_with_retry(stock)
        print(f"👨‍💻 Worker-{worker_id}: {result}")
        
        
        
        
async def main():
    queue = asyncio.Queue()
    
    stocks = ['AAP' , 'GGL' , 'TSLA' , 'AMZN' ,'MSFT']
    
    async with asyncio.TaskGroup() as tg:
        tg.create_task(producer(queue , stocks))
        tg.create_task(consumer(queue , 1))
        tg.create_task(consumer(queue, 2))
        
        


asyncio.run(main())                

        
                          



    
    