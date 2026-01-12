from my_package import Square as s
import time


def compute_square(sqr):
    def wrapper(*args , **kwargs):
        start_time = time.time()
        result = sqr(*args, **kwargs)
        end_time = time.time()
        time_taken = end_time - start_time
        return result, time_taken
    return wrapper


square = compute_square(s.sqr)  

"""
here ,when this line called it return wrapper function .so after execution , square = wrapper function . 
that's why when square(25) is called it calls wrapper function and it return tuple of result and time taken.
"""

result, time_taken = square(5)
print(f"Square: {result}, Time taken: {time_taken} seconds")
#print(square(25)) -> it actually means wrapper(25)
print("----------------------------------")
print()


def compute_sqrt(sqrt):
    def wrapper(*args , **kwargs):
        start_time = time.time()
        ans = sqrt(*args , **kwargs)
        end_time = time.time()
        time_taken = end_time - start_time
        return ans , time_taken
    return wrapper

sqrt = compute_sqrt(s.sqrt)
result , time_taken = sqrt(25)
print(f"Square root: {result} , Time taken: {time_taken} seconds")
print("----------------------------------")
print()

def my_decorator(add):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = add(*args, **kwargs)
        end_time = time.time()
        time_taken = end_time - start_time
        return result , time_taken
    return wrapper

@my_decorator
def add(a, b):
    return a + b

result , time_taken = add(3, 4)
print(f"Addition: {result} , Time taken: {time_taken} seconds")