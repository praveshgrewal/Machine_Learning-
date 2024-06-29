

import threading
import requests
from bs4 import BeautifulSoup

urls=[
    'https://python.langchain.com/v0.2/docs/introduction/',
    'https://python.langchain.com/v0.2/docs/concepts/',
    'https://python.langchain.com/v0.2/docs/tutorials/',
]

def fetch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f"Fetched {len(soup.text)} characters from {url}")


threads= []
for url in urls:
    t=threading.Thread(target=fetch_content,args=(url,))
 
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("data fetched successfully")  



# Trail Change to take care of my branch 