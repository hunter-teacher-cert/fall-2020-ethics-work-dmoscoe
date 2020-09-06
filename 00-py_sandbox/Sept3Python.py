# -*- coding: utf-8 -*-
# Clyde "Thluffy" Sinclair
# Aug 2020

"""
x    defining and using variables
x    defining and calling ("invoking") functions
x    Writing a "Hello, world!" script is a good first step...
x    arrays ("lists" in python)
    2D lists
    hashmaps ("dictionaries" in python)
"""

car = 10 #no type casting (mostly).

def factorial(n):
    n = int(n)
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return 

print("Good News Everyone!")
print(f"1! = {factorial(1)}" ) #notice how f, {} are used.
print(f"fib(1) = {fib(1)}" )

list = [3, 4, 6, 7.3]
print(list)

for i in range(len(list)):
    list[i] = 2*list[i]
print(list)

empty = [None, None, None, "None"]
print(empty)

dict = {"A":[1,2,5], "B":2, "C":3}
print(dict["A"])

print(factorial(5))

