# random_buggy_script.py

import math
import random

def calculate_area(radius):
    return math.pi * radius ** 2

def greet(name):
    print("Hello " + name)

def divide(a, b):
    return a / b

numbers = [1, 2, 3, 4, 5]

for i in range(0, len(numbers)):
    print("Number:", numbers[i])

user_input = input("Enter a number: ")

if user_input > 10:
    print("Greater than 10")
else
    print("Less or equal to 10")

result = divide(10, 2)  # Use a non-zero divisor
print("Result:", result)

data = {"name": "John", "age": 25, "address": "123 Main St"}

print(data["address"])

for i in range(5)
    print(i)

x = 5
y = 10
print(x + y)

def random_func():
    return random.randint(1, 10)

print(random_func)
