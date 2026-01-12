def addition(*args):
    return sum(args)


def subtraction(a, b):
    return a - b


def multiplication(*args):
    result = 1
    for i in args:
        result *= i
    return result

def division(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def power(base, exponent):
    return base ** exponent

def modulo(a, b):
    return a % b

def table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")


def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def cube(n):
    return n ** 3

def cube_root(n):
    return n ** (1/3)