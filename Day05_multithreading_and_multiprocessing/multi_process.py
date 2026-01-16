import multiprocessing
import time

def compute_sum_of_squared_list(numbers , result):
    total = 0 
    for n in numbers:
        total += n*n
    result.put(total)

if __name__ == "__main__":
    numbers = list(range(1,10000))

    result = multiprocessing.Queue()
    
    p = multiprocessing.Process(target=compute_sum_of_squared_list , args=(numbers,result))

    p.start()

    p.join()

    output = result.get()   # receive data from child process
    print("Sum of squares:", output)

