#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")

greet("Guido")
    

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")


greet_with_default()





def add(num1, num2):
    add=num1 + num2
    return add
add(2,5)

def halve(number):
    halve=number/2
    return halve
halve(50)