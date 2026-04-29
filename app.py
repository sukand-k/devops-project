def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


def square(number):
    return number * number


def is_even(number):
    return number % 2 == 0


def find_biggest(a, b):
    if a > b:
        return a
    return b


def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)


def greet_user(name):
    return "Hello " + name + ", welcome to Jenkins Testing Project!"