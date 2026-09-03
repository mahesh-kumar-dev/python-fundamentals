# Python Function
# A function is a reusable block of code that performs a specific task. 

'''
    Characteristics:
	Reuse code -> Write once, use many times
	Organize code -> Break large programs into smaller pieces
	Avoid repetition -> Don't copy-paste the same code
	Easier debugging -> Fix bugs in one place
	Share code -> Use functions across different programs
'''


# DEFINING AND CALLING FUNCTIONS

# Basic function definition

# Define a function (doesn't run yet)
def greet():
    print("Hello!")

# Call the function (Thats run now)
# You can call it many times
greet()
greet()


# Function naming rules:
'''
	Letters, numbers, underscore (can't start with number)
	No spaces
	Case-sensitive
	Use snake_case (lowercase with underscores)
'''

# Good function names
def calculate_average():
    pass

def get_user_name():
    pass

def is_valid():
    pass


# FUNCTION PARAMETER (INPUTS)

# Function with parameters
# Parameter let you pass data into function 

# Function with one parameter
def greet(name):
    print(f"Hello, {name}")

greet("Mahesh")
greet("Asma")


# Function with multiple parameters

def introduce(name,age):
    print(f"My name is {name} and I am {age} year old.")

introduce("Mahesh",20)
introduce("Fiza",19)

# How   Parameters works
def addition(a,b):
    result = a + b
    print(f"{a} + {b} = {result}")

addition(8,5)
addition(12,67)

# The parameters (a,b) are just the placeholders
# They got replaced with the values you pass


# Parameters Vs Arguments
# Parameters:  The variable name in the function definition
# Arguments: The actual value you pass into function while calling

def multiply(num1,num2):
    return num1 * num2

result = multiply(5,4)
print(result)


# RETURN VALUES
# The 'return' statement
# Function can send back a result using return 

# Function that return  a value

def subtract(num1, num2):
    return num1 - num2

# Store the returned value
result = subtract(24,12)
print(result)

# Use the returned value directly
print(subtract(34,10))


# FUNCTION WITHOUT RETURN 
# If you donot use return, the function will return None.

def say_hello(name):
    print(f"Hello, {name}")
    # No return statement

greet = say_hello("Payal")
print(greet) # None

# The function printed "Hello, Alice!" but returned nothing


# Return vs Print
# This function PRINTS  doesn't RETURN
def add_and_print(a,b):
    print(a+b)

# This function RETURNS doesn't PRINT
def add_add_retun(a,b):
    return a + b

# Using print function
add_and_print(5,3)
result = add_and_print(13,2)
print(result) # result is None

# Using return statement
value = add_add_retun(5,7)
print(value)


# MULTIPLE RETURN VALUES
# You can return multiple values as tuple.

def get_user():
    name = "Asma"
    age = 19
    city = "Thatta"
    return name,age,city

# Unpack the returned values
user_name , user_age, user_city = get_user()
print(f"{user_name} is {user_age} from {user_city}.")

# Or keep as tuple
user_info = get_user()
print(user_info)


# TYPES OF ARGUMENTS

# Positional Arguments (Order Matters)
def describe_pet(name, animal_type):
    print(f"I have a {animal_type} named {name}")

# Order matters - first name then animal_type
describe_pet("Max","Dog")
describe_pet("Whisker","Cat")

# Wrong order gives you wrong results
describe_pet("Dog","Motie")


# Keyword Argument (Order doesn't matters)
def describe_user(name,age):
    print(f"Myself {name}, I am {age} year old.")

# Using parameter names
describe_user(age=21,name="Komal")
describe_user(name="Sooraj",age=27)


# Default Parameters
# You can give parameter DEFAULT VALUES

def greetings(name,greet="Hello"):
    print(f"{greet}, {name}")

greetings("Payal")
greetings("Sonu","Hi")
greetings("Pardeep","Hey")


# Default parameters with multiple values
def create_user(name, age = 18, city = "Unknown", is_active = True):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
    print(f"Is Active: {is_active}")

create_user("Deepak")
create_user("Nirmala",23)
create_user("Rajesh",city="Boston")
create_user("Diana" , is_active=False)


# Default parameter trap
# WRONG - Mutable default (list) persist across calls

def add_items_bad(item, my_list = []):
    my_list.append(item)
    return my_list

print(add_items_bad(1)) # [1] 
print(add_items_bad(2)) # [1,2]

# CORRECT - Use None and create new list each time 

def add_list_good(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

print(add_list_good(2)) # [2]
print(add_list_good(3)) # [3]


# VARIABLE SCOPE
# LOCAL VS GLOBAL
# LOCAL:  Created inside a function, only exist there
# GLOBAL: Created outside, can be accessed anywhere

# Global variable
message = "Hello"

def greets():
    # Local variable
    local_msg = "Hi"
    print(message)
    print(local_msg)

greets()


# Modifying Global variable
# Use the global keyword to modify a global variable inside a function

count = 0 # global variable

def increment():
    global count
    count = count + 1

print(count)
increment()
print(count)
increment()
print(count)
increment()


# Local Variable shadows Global

name = "Global Gobind" # Global variable

def says():
    name = "Local Devi" # Local variable (doesn't change global)
    print(name)

says()
print(name)


# DOCSTRINGS (Documentation)
# Docstrings explain what your function does.

def calculate_area(length, width):
    """
    Calculate Area of a Rectangle

    Parameters:
        length: The length of rectangle.
        width: The width of rectangle.
    
    Returns:
        The area (length x width)

    Example: 
        >>> calculate_area(5,3)
        15        
    """
    return length * width

# View the docstrings
help(calculate_area)
print(calculate_area.__doc__)


# Practice Questions

# Temperature Converter
def celsius_to_fahrenheit(celsius):
    """ Convert Celsius to Fahrenheit """
    fahrenheit = (celsius*9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """ Convert Fahrenheit to Celsius"""
    celsius = (fahrenheit - 32)*5/9
    return celsius

# Use the functions
temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")

temp_f = 77
temp_c = fahrenheit_to_celsius(temp_f)
print(f"{temp_f}°F = {temp_c}°C")


# Shopping Cart Function

def add_item(cart , item, price):
    """ Add Item to Shopping Cart"""
    cart.append({"name": item, "price": price})
    print(f"Added: {item} (${price})")
    return cart

def calculate_total(cart):
    """ Calcuate Total price of All items"""
    total = 0
    for item in cart:
        total = total + item["price"]
    return total

def show_cart(cart):
    """ Display all items of Cart"""
    if not cart:
        print("Cart is empty.")
        return 
    print("\n-----Shopping Cart-----")
    for item in cart:
        print(f" {item['name']}: ${item['price']:.2f}")
    print(f"Total: ${calculate_total(cart):.2f}")

# Use Functions
my_cart = []
my_cart = add_item(my_cart,"Apple",0.50)
my_cart = add_item(my_cart,"Banana",0.30)
my_cart = add_item(my_cart,"Orange",0.75)
show_cart(my_cart)



# Password Validator
def is_strong_password(password):
    """ Check if password meets strength criteria"""

    if len(password) < 8:
        return False
    
    has_upper = False
    has_lower = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True

    return has_digit and has_lower and has_upper

def get_password_feedback(password):
    """Provide Feedback on Password"""
    feedback = []

    if len(password) < 8:
        feedback.append("At least 8 Characters.")
    if not any(c.islower() for c in password):
        feedback.append("At least one lowercase character.")
    if not any(c.isupper() for c in password):
        feedback.append("At least one uppercase character.")
    if not any(c.isdigit() for c in password):
        feedback.append("At least one digit.")

    return feedback

# Use function
password = input("Enter password: ")

if is_strong_password(password):
    print("Strong Password.")
else:
    print("Weak Password. It needs:")
    for issue in get_password_feedback(password):
        print(f" -{issue}")



# Number Guessing Game with Functions
import random

def get_random_number():
    """Generate random number between 1 and 10"""
    return random.randint(1, 10)

def get_user_guess():
    """Get valid guess from user"""
    while True:
        try:
            guess = int(input("Enter your guess (1-10): "))
            if 1 <= guess <= 10:
                return guess
            print("Please enter a number between 1 and 10")
        except ValueError:
            print("Please enter a valid number")

def check_guess(guess, secret):
    """Check guess against secret number"""
    if guess < secret:
        return "too low"
    elif guess > secret:
        return "too high"
    else:
        return "correct"

def play_game():
    """Main game function"""
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 10")
    
    secret = get_random_number()
    attempts = 0
    
    while True:
        guess = get_user_guess()
        attempts = attempts + 1
        result = check_guess(guess, secret)
        
        if result == "correct":
            print(f"Correct! You got it in {attempts} attempts!")
            break
        else:
            print(f"Too {result}! Try again.")

# Start the game
play_game()


# LAMBDA FUNCTION (Small Anonymous function)
# Lambda functions are one-line functions without a name

# Regular function
def square(x):
    return x**2

# lambda function 
square = lambda x : x**2 
print(square(5))


# When to Use lambda
# Lambda is useful for simple operations, especially with other functions.

# Sort a list of tuples by the second value
pairs = [(1, 3), (2, 1), (3, 2)]
pairs.sort(key=lambda pair: pair[1])
print(pairs)  


# Filter a list
numbers = [1,2,3,4,5,6]
evens = list(filter(lambda x : x % 2 == 0, numbers))
print(evens)

# Map (transform) a list
squares = list(map(lambda x: x ** 2, numbers))
print(squares) 


# Lambda Vs Regular Function 
# Use regular function for:
# - Complex logic (multiple lines)
# - Need documentation (docstring)
# - Reused many times
# - Debugging (stack traces are clearer)

# Use lambda for:
# - Simple one-line operations
# - One-time use (especially with map, filter, sort)
# - When function is short and obvious


# Average of list
def average(numbers):
    if not numbers:
        return 0
    return sum(numbers)/len(numbers)

print(average([1,2,3,4,5,6]))


# Prime Determination function
def is_prime(num):
    if num < 2:
        return False
    for i in range(2,int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print(is_prime(17))
print(is_prime(20))

# Min And Max Function of list
def min_max(numbers):
    return min(numbers), max(numbers)

lowest , highest = min_max([5,2,8,1,9])
print(f"Lowest: {lowest} , Highest: {highest}")

