# An overview of Python basics

# Basic python types - Integers, string, floats, booleans, variables

print("Hello World!")
print(type("Rock Paper Scissors Shoot!"))

print(777)
print(type(20))

print(0.75)
print(type(100.0))

print(10>5)
print(type(50<=20))

name, age = "Haroon", 26
numbers = [1, 2, 3, 4, 5, 6, 7]
print(name)
print(age)
print(numbers)
print(type(numbers))

# This is my first comment

"""
This is my second comment 
using triple quotations we can spread the comments over multiple lines
"""

# String manipulation

brand = "Adidas"
print(brand)
print(brand.upper())
print(brand.replace("A", "77"))
print(len(brand))
print(brand == "adidas")
print(brand != "adidas")
print("das" in brand)

# Multi-line strings

comment = "Hi my name is Haroon " \
    "I am 26 years old" \
        " This is not the layout intended"
print(comment)

# To avoid the layout of the string spanning over one line we use triple quotations

comment2 = f""" 
Hi my name is {name}.
I am {age} years old.
This is the layout I was looking for.
"""
print(comment2)

# Reserved keywords in Python

import keyword
print(keyword.kwlist)

