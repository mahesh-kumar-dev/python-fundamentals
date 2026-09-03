# CREATING OWN MODULE
# Create python file
# my_module  -- This is my module

def greet(name):
    """Say Hello to Someone"""
    print(f"Hello, {name}")

def add(a,b):
    """Add two numbers"""
    return a+b

PI = 3.14159

class Calculator:
    def multiply(self, a , b):
        return a*b

# my_module.py
print(f"My Module name is: {__name__}")

def greets(name):
    return f"Hello, {name}"

# This code is runs when this file is executed directly
if __name__ == "__main__":
    print("This file is being run directly ")
    result = greets("Alice")
    print(result)

