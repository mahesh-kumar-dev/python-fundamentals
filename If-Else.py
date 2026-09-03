# Python If-Else (Decision Making)
# if-else allows your program to make decisions and choose different
#  paths based on conditions

'''
    Features: 
	Make choices -> Do different things based on conditions
	Validate input -> Check if user entered valid data
	Control flow -> Decide which code to run
	Handle errors -> Respond to different situations
'''

# Basic "if" Statement
temperature = 30
if temperature > 25:
    print("It's hot outside.")
    print("Stay Hydrated.")

# This runs always (outside the if block)
print("Good Bye")

# In Python, indentation (spaces) tells Python what's inside the if block.
age = 18
if age >= 18:
    print("You can Vote!")

temperature = 20
if temperature > 25:
    print("It's Hot day outside")
    print("Stay Hyderated.")
print("Bye!!!")

# Using pass for Empty if
# Sometimes you want an if statement that does nothing (placeholder).
age = 15
if age >= 18:
    pass  # add voting code later
else:
    print("Too young to vote.")


# Comparison Operators (The Conditions)
# These operators compare values and return True or False.
x = 10
y = 20
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# Comparing String
name = "Payal"
if name == "Payal":
    print("Hello, Payal!")
if name != "Karan":
    print("You are not Karan.")

# String comparison is case sensitive
print("hello" == "Hello")

# Case-sensitive comparison
user_inp = "YES"
if user_inp.lower() == "yes":
    print("User agreed.")


# The "else" Statement
# else runs when the if condition is False.
age = 16
if age >= 18:
    print("You can vote!")
else:
    print("You are too young to vote.")


# Multiple Statements in if-else
score = 85

if score >=60 :
    print("You passed!")
    print("Congratulations!")
    print("Keep it up Good work!")
else:
    print("You failed.")
    print("Study harder next time.")
    print("Don't give up.")


# The "elif" Statement (Else If)
# elif allows you to check multiple conditions in sequence
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")


# How elif works
# Python checks conditions from top to bottom. The first one that is 
# True runs, and the rest are skipped
z = 75

if z > 50:
    print("Greater than 50.")  # This runs
elif z > 70:
    print("Greater than 70.") # Skipped (already found True)
elif z > 80:
    print("Greater than 80.")
else:
    print("Other.")


# Multiple elifs
temp = 22

if temp > 35:
    print("Extreme Heat.")
elif temp > 25:
    print("Warm day.")
elif temp > 15:
    print("Pleasant day.")
elif temp > 5:
    print("Cold day.")
else:
    print("Freezing cold.")


# Logical Operators 
# and – Both conditions must be True
age = 25
has_license = True

if age >= 18 and has_license :
    print("You can drive.")
else:
    print("You cannot drive.")


# or – At least one condition must be True
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
else:
    print("It's weekday.")


# not – Reverses the condition
is_raining = False

if not is_raining:
    print("Umbrella needed.")


# Combining Multiple Conditions
age = 20
income = 45000
has_criminal_record =  False
has_permission = False

if age >= 18  and income >= 30000 and not has_criminal_record:
    print("Loan Approved.")
else:
    print("Loan denied.")


# Operator Precedence
# 'and' has higher precedence than 'or'
# This means 'and' is evaluated first

# Without parentheses
if age >= 18 and income > 30000 or has_permission:
    # This means: (age > 18 and income > 30000) or has_permission
    print("Access granted.")

# use parentheses to make it clear
if (age >= 18 and income > 30000) or has_permission:
    print("Access granted.")

# Different grouping gives different result
if age > 18 and (income > 30000 or has_permission):
    print("Access granted")


# Truthy and Falsy Values
# In Python, many values can be used as conditions (not just True/False).
# Falsy Value (Act like False)
'''
if None:
if False:
if 0:
if 0.0:
if "":
if []:
if ():
if set():
'''
name = ""
if name:
    print(f"Hello, {name}")
else:
    print("No name provided.")


# Truthy Values (Act like True)
'''
if True:
if 1:
if 4.9:
if -9:
if "Hi":
if [1,2]:
if {"a": 1}:

'''
name = "Komal"
if name:
    print(f"Hello, {name}")
else:
    print("No name provided.")


# Practical Use of Truthy and Falsy 
# Check if list is empty
shopping_cart = []
if shopping_cart:
    print(f"You have {len(shopping_cart)} items.")
else:
    print("Your cart is empty.")

# provide default values
user_input = input("Enter name: ")
if not user_input:
    user_input = "Anonymous"
print(f"Hello, {user_input}")

# Check if value exists
''' result = get_data()
if result:
    process(result)
'''

# Nested if Statements
# You can put if statements inside other if statements
age = 25
has_ticket = True

if age >= 18:
    print("Age check passed.")
    if has_ticket:
        print("Welcome to concert!")
    else:
        print("Please buy a ticket.")
else:
    print("Too young for this event.")


# Avoid too many nesting use 'and' tro combine different conditions
# Or use early return in functions

def process_data(data):
    if not data:
        return 
    if not data.is_valid():
        return
    if not data.has_permission():
        return


# Ternary Operator 
# A shorter way to write simple if-else statements.
# Syntax: value_if_true if condition else value_if_false
age = 21
status = "Adult" if age>= 18 else "Minor"
print(status)

# Get max of 2 numbers
a,b = 10,20
max_val = a if a > b else b
print(max_val)

# check even/odd numbers
num = 7
result = "Even" if num%2 == 0 else "Odd"
print(result)


# In print statement
x = 8
print("Positive" if x > 0 else "Non-Positive")



# Nested Ternary
a,b,c = 5,12,8
max_value = a if (a > b and a > c) else (b if b > c else c)
print(max_value)

# better to use if-else for complex logic
if a >  b and a > c:
    max_value = a
elif b > c:
    max_value = b
else:
    max_value = c

print(f"Maximum value: {max_value}")



# Common Pattern
# Pattern 1: User input Validation
# validate age input 
age_input = input("Enter your age: ")

if age_input.isdigit():
    age = int(age_input)
    if age >= 18:
        print("Access granted.")
    else:
        print("Access denied. too young")
else:
    print("Please enter valid number.")


# Pattern 2: Menu Selection
print("1. Start Game")
print("2. Load Game")
print("3. Settings")
print("4. Exit")

choice = input("Enter choice: ")
if choice == "1":
    print("Starting new game...")
elif choice == "2":
    print("Loading saved game...")
elif choice == "3":
    print("Opening setting...")
elif choice == "4":
    print("GoodBye!")
else:
    print("Invalid choice")



# Pattern 3: Range Checking
score = 84

if 90 <= score <= 100:
    grade = "A"
elif 80 <= score <= 90:
    grade = "B"
elif 70 <= score <= 80:
    grade = "C"
elif 60 <= score <= 70:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score} , Grade: {grade} ")



# Pattern 4: Multiple conditions
# Check if character is vowel
char = input("Enter a letter: ").lower()

if char in "aeiou":
    print(f"{char} is a vowel.")
elif char.isalpha():
    print(f"{char} is a consonant.") 
else: 
    print("Not a letter")


# Pattern 5: Guard Clauses
def calculate_discounts(price, customer_type, years):
    # Guard clauses - check invalid conditions first
    if price <= 0:
        return 0
    if customer_type not in ["regular", "premium", "vip"]:
        return 0
    if years < 0:
        return 0
    # Main logic (only runs if all guards pass)
    if customer_type == "vip":
        return price*0.2
    elif customer_type == "premium":
        return price*0.1
    else:
        return price*0.05

price = 45000
customer_type = "vip"
years = 3
discounts = calculate_discounts(price,customer_type,years)


print("\n----Customer Details-------")
print("Price: ",price)
print("Customer Type: ", customer_type)
print("Years: ",years)
print(f"Your discounts: {discounts}")


# Practice Questions
# Number Guessing Game
import random

secret = random.randint(1,10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == secret:
    print("Correct guess! You win")
elif guess < secret:
    print(f"Too Low! The number is {secret}")
else:
    print(f"Too High! The number is {secret}")



# Grade Calculator
# Get scores
math = float(input("Maths score: "))
science = float(input("Science score: "))
english = float(input("English score: "))

# Calculate average
average = (math + science + english)/3

# Determine grade
if average >= 90:
    grade = "A"
    message = "Excellent"
elif average >= 80:
    grade = "B"
    message = "Good job!"
elif average >= 70:
    grade = "C"
    message = "Fair"
elif average >= 60:
    grade = "D"
    message = "Need improvements"
else:
    grade = "F"
    message = "See teacher"

# Display results
print(f"\nAverage: {average}")
print(f"Grade: {grade}")
print(message)



# Ticket Price Calculator
age = int(input("Enter your age: ") )
is_student = input("Are you student? (yes/no): ").lower() == "yes"

# Calculate price

base_price = 900

if age < 12:
    price = base_price*0.5
elif age >= 65:
    price = base_price*0.7
elif is_student:
    price = base_price*0.8
else:
    price = base_price

print(f"Ticket Price: {price}")



# Simple Login System
# predefined credentials
valid_username = "admin"
valid_password = "secret123"

# Get user input
username = input("Username: ")
password = input("Password: ")

# Check Credentials
if username == valid_username and password == valid_password:
    print("Login Successful!")
    print("Welcome to System.")
else:
    print("Login Failed.")
    if username != valid_username:
        print("Incorrect Username.")
    if password != valid_password:
        print("Invalid Password.")


# Positive,Negative,Zero Number identifiers
num = float(input("Enter a number: "))

if num > 0:
    print(f"Positive: {num}")
elif num < 0:
    print(f"Negative: {num}")
else:
    print("Zero")


# Leap Year program
year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is NOT a leap year.")


# Largest Number among 3 numbers
a = float(input("First number: "))
b = float(input("Second number: "))
c = float(input("Third number: "))

if a >= b and a >= c:
    Largest = a
elif b >= c:
    Largest = b
else:
    Largest = c

print(f"The largest: {Largest}")



# Login program
username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "secret123":
    print("Access granted!")
else:
    print("Access denied.")

