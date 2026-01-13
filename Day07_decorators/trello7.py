import time
from math import pow

def decorator(func):
    def wrapper(*args , **kwargs):
        print("Before calling the function")
        r = func(*args , **kwargs)
        print("After calling the function")
        return r
    return wrapper

def my_decorator(func):
    def wrapper(*args , **kwargs):
        start_time = time.time()
        res = func(*args , **kwargs)
        end_time = time.time()
        time_taken = end_time - start_time
        return res , time_taken
    return wrapper


@my_decorator
@decorator
def sqr(n):
    return n*n

@decorator
@my_decorator
def table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

@decorator
def greet():
    print("Hello, welcome to the decorated world!")
    

result, time_taken = sqr(5)
print(f"Square: {result}, Time taken: {time_taken} seconds")
print()

res , time_taken = table(7)
print(f"Time taken to print table: {time_taken} seconds")
print()

greet()
print()

#decorator for built in functions
power = my_decorator(pow)
result , time_taken = power(2,5)
print(f'2 raised to power 5 is : {result} , Time taken: {time_taken} seconds')
print()
print("----------------------------------")



#Abstractclass with deorator
from abc import ABC , abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):

    def __init__(self , length , width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    

class Circle(Shape):

    def __init__(self , radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    

r = Rectangle(5 , 10)
print(f"Area of Rectangle : {r.area()}")
print()

c = Circle(7)
print(f"Area of Circle : {c.area()}")
print()


