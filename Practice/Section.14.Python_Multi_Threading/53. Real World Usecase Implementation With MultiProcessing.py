#real world example: multithreading for I/O bound tasks
#scenario: web scraping
#web scraping often invloves making numerus network requestas to fetch web pages. these tasks are I/O bound 
#because they spend a lot of time waiting for responses from the server. multithreading can significantly
#improve the performance of these tasks.


import multiprocessing
import math
import time
import sys

#increasing the max number of digit for interger converson
sys.set_int_max_str_digits(100000)

#create a function to calculate factorial
def factorial(number):
    print(f"Calculating factorial of {number}")
    result= math.factorial(number)
    print(f"Factorial of {number} is {result}")

    return result

if __name__=="__main__":
    numbers= [5000,6000,7000,8000]

    start_time= time.time()

    #create a pool of workers
    with multiprocessing.Pool() as pool:
        result= pool.map(factorial, numbers)

    end_time= time.time()

    print(f"Factorial of {numbers} is {result}")
    print(f"Time taken by the program is {time.time() - start_time} seconds")



