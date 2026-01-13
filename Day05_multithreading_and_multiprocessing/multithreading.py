import threading
import time
from concurrent.futures import ThreadPoolExecutor


def task1():
    for i in range(5):
        print(f"task 1 is running.")
        time.sleep(2)

def task2():
    for i in range(5):
        print(f"task 2 is running.")
        time.sleep(3)


t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)


t1.start()
t2.start()

t1.join()
t2.join()

print("Both tasks are completed.")

def sqr(n):
    for i in range(3):
        print(f"The square of {n} is {n*n}")
        time.sleep(1)

def cube(n):
    for i in range(3):
         print(f"The cube of {n} is {n*n*n}")
         time.sleep(1)


t3 = threading.Thread(target=sqr , args=(5,))
t4 = threading.Thread(target=cube , args=(5,))

t3.start()
t4.start()

t3.join()
t4.join()

print("Square and Cube calculations are done.")


def sqr(n):
    return n*n


with ThreadPoolExecutor(max_workers=4) as executor:
    numbers = [1,2,3,4,5]
    results = list(executor.map(sqr , numbers))


for i in range(len(numbers)):
    print(f"The square of {numbers[i]} is {results[i]}")
