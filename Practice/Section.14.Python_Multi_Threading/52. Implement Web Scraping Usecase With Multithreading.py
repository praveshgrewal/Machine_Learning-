'''
real world example: multithreading for I/O bound tasks
scenario: web scraping
web scraping often invloves making numerus network requestas to fetch web pages. these tasks are I/O bound 
because they spend a lot of time waiting for responses from the server. multithreading can significantly
improve the performance of these tasks.
'''

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