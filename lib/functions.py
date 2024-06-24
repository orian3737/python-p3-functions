#!/usr/bin/env python3

def greet_programmer():
    print("Hello Programmer")

def greet(name):
    print(f"Hi there, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hi there, {name}!")

def add(num1, num2):
    print(num1 + num2)

def halve(number):
    result = number / 2
    return result


greet_programmer()
greet("Ryan")
greet_with_default()
greet_with_default("joe")
add(1, 2)
halve(8)