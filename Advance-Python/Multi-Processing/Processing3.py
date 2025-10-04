# Downloading multiple urls with multiprocesssing 


from multiprocessing import Pool , Process
import time
import requests

def download_url(url):
    response = requests.get(url)
    print(f"Downloaded {url} with length {len(response.text)}")
    return len(response.txt)


if __name__ == "__main__":
    
    urls = [
        "https://www.example.com",
        "https://www.python.org",
        "https://www.wikipedia.org",
        "https://www.openai.com"]
    
    
    start = time.time()
    
    # create pool of processes
    with Pool(processes=4) as pool:
        results = [pool.apply_async(download_url, args=(url,)) for url in urls]
        output = [r.get() for r in results]
            
    end = time.time()    
    
    print("Results:", output)
    print("Time taken:", end - start)
    
    
    
#----------------------------------------------------------------------------------------

 #with pool.imap_unordered  # -----------------------> when we dont care about order  
        


