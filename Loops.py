# Python Loops
# Loops let you repeat code multiple times
'''
    Features:
	Repeat tasks -> Do something many times without writing duplicate code
	Process lists -> Go through each item in a collection
	Wait for conditions -> Keep running until something changes
	Create patterns -> Generate repeated structures
'''

# WHILE LOOP
# A while loop continues as long as the condition is True.

# Simple countdown
count = 5
while count > 0:
    print(count)
    count = count - 1
print("Blast off!")



# How while loop work
'''
1. Check condition
2. If True → execute code block
3. Go back to step 1
4. If False → exit loop
'''
x = 1
while x <= 3:
    print(f"x is {x}")
    x = x + 1
print("Loop ended.")


# Common while loop patterns
# Pattern 1: Count up
i = 1
while i <= 10:
    print(i,end=" ")
    i = i + 1

print() # new line

# Pattern 2: Count down
i = 10
while i >= 0:
    print(i,end=" ")
    i = i - 1
print("Start now\n")

# Pattern 3: Step by 2
i = 0
while i <= 10:
    print(i,end=" ")
    i = i + 2
print()



# FOR LOOP
# A for loop iterates over each item in a collection.

# loop through a list
fruits = ["apple","banana","cherry"]
for fruit in fruits:
    print(fruit)

# Loop through String
# String as collection of characters
name = "Mahesh Kumar"
for letter in name:
    print(letter)


# Loop through range of numbers
# range(n) generates numbers from 0 to n-1.
for i in range(6):
    print(i,end=" ")

# range() with Start and End
# range(start,end) ~ start to end - 1
for i in range(2,6):
    print(i)

# range(start, end , step)
for i in range(0,10,2):
    print(i)

# Count down with negative steps
for i in range(5,0,-1):
    print(i)


# LOOP CONTROL STATEMENTS
# break – Exit the Loop Immediately

# at 5 loop will stop
for i in range(10):
    if i == 5:
        break
    print(i)

# continue – Skip to Next Iteration
# Skip even numbers
for i in range(10):
    if i%2 == 0:
        continue
    print(i)


# else with Loops
# The else block runs if the loop completes normally (without break).

# with break else doesnot run
for i in range(5):
    if i == 3:
        break
        print(i)
    else:
        print("Loop completed.") # this won't print

# Without break - else run
for i in range(5):
    print(i)
else:
    print("Loop completed.") # this prints


# Common Loop Patterns
# Pattern 1: Sum of numbers

# While loop sum

total = 0
i = 1
while i <= 10:
    total = total + i
    i = i + 1
print(f"Sum: {total}")

# Sum with for loop
total = 0
for i in range(1,11):
    total = total + i
print(f"Sum: {total}")


# Pattern 2: Finding Items
# Find if item exists
sims = ["jazz","zong","ufone","telenor"]
search = "zong"

found = False
for sim in sims:
    if sim == search:
        found = True
        break
if found:
    print(f"Found: {search}")
else:
    print(f"{search} not found.")

# Pattern 3: User input untill valid
while True:
    user_input = input("Enter a number between 1 and 10: ")
    if user_input.isdigit():
        num = int(user_input)
        if 1 <= num <=10:
            print(f"Good! You entered {num}")
            break
        else:
            print("Numbers are out of range.")
    else:
        print("Please enter a valid number")

# Pattern 4: Menu System
while True:
    print("\n-----Menu System-----")
    print("1. Say Hello")
    print("2. Say GoodBye")
    print("3. Quit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Hello!")
    elif choice == "2":
        print("Goodbye!")
    elif choice == "3":
        print("Quiting.....")
        break
    else:
        print("Invalid choice.")


# NESTED LOOPS
# Loop inside loop

# Multiplication table
for i in range(1,11):
    for j in range(1,11):
        product = i * j
        print(f"{i} x {j} = {product}")
    print("--------")

# Creating Patterns
# Triangle Pattern
for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()
print()
print()


# Square pattern
size = 5
for i in range(size):
    for j in range(size):
        print("*",end=" ")
    print()


# LOOPS WITH LIST
mobiles = ["Infinix","Oppo","Vivo","IPhone"]

# Method 1: Direct Iteration
for mobile in mobiles:
    print(mobile)

# Method 2: With index (using range())
for i in range(len(mobiles)):
    print(f"{i}: {mobile[i]}")

# Method 3: With index (using enumerate())
for i,mobile in enumerate(mobiles):
    print(f"{i}: {mobile}")

# Modifying List While Looping

# WRONG  :  Modifying list while iterating (skips elements)
numbers = [1,2,3,4,5]
for n in numbers:
    if n % 2 == 0:
        numbers.remove(n)
print(numbers)

# CORRECT - Iterate over copy
numbers = [1,2,3,4,5]
for n in numbers[:]:  # Create a copy
    if n % 2 == 0:
        numbers.remove(n)
print(numbers)

# Best - Create a new list (List comprehension)
numbers = [1,2,3,4,5]
numbers = [n for n in numbers if n % 2 != 0]
print(numbers)

# LOOP WITH DICTIONARY
person = {"name": "Mahesh", "age": 20, "city":"Ghotki"}

# Loop through keys
for key in person:
    print(key)

# Loop through Values
for value in person.values():
    print(value)

# Loop through key:value pairs
for key,value in person.items():
    print(f"{key}: {value}")


# LIST COMPREHENSION
# A shorter way to create lists using a loop in one line

# traditional way
squares = []
for i in range(10):
    squares.append(i**2)
print(squares)

# List comprehension (same result)
squares = [n**2 for n in range(10) ]
print(squares)


# List comprehension with condition 
# traditional way
evens = []
for i in range(21):
    if i % 2 == 0:
        evens.append(i)
print(evens)

# List comprehension
evens = [n for n in range(21) if n % 2 == 0]
print(evens)

# More list comprehension examples
# Transform each item
names = ["mahesh","sajid","mehtab"]
capitalized = [name.title() for name in names]
print(capitalized)

# Filter and transform
numbers = [1,2,3,4,5,6]
even_squares = [n**2 for n in numbers if n%2 == 0]
print(even_squares)

# With if-else
parity = ["Even" if n%2 == 0 else  "Odd" for n in numbers]
print(parity)


# INFINITE LOOPS AND PREVENTION
# Infinite Loop
# A loop that never stops (condition never becomes False).


# How to avoid the infinite loop
# Always update the condition variable
count = 1
while count <= 5:
    print(count)
    count = count+ 1

# Use a counter for safety
'''max_attempts = 10
attempt = 0
while condition and attempt < max_attempts:
    # Do something
    attempt = attempt + 1
'''

# Use break for exit conditions
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == "quit":
        break
print(user_input)

# Practice Questions
# Factorial Calculator
n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n+1):
    factorial = factorial * i
print(f"{n}!: {factorial}")



# Guess the Number Game
import random

secret = random.randint(1,10)
attempts = 0

print("I'm thinking of numbers between 1 and 10.")

while True:
    guess = int(input("Your Guess: "))
    attempts = attempts + 1

    if guess < secret:
        print("Too low! Try again.")
    elif guess > secret:
        print("Too high! Try again.")
    else:
        print(f"Correct! You got it in {attempts} attempts.")
        break


# Shopping List Total
# Enter items and prices until 'done'
items = []
total = 0

while True:
    item = input("Enter item name (or done): ")
    if item.lower() == "done":
        break
    price = float(input(f"Enter price for {item}: $"))
    items.append((item,price))
    total = total + price

print("\n------Receipt--------")
for item,price in items:
    print(f"{item}: ${price:.2f}")

print(f"Total: ${total:.2f}")



# Password Validation
# Keep asking until password meets criteria

while True:
    password = input("Create password: ")
    
    errors = []
    
    if len(password) < 8:
        errors.append("At least 8 characters")
    if not any(c.isupper() for c in password):
        errors.append("At least one uppercase letter")
    if not any(c.islower() for c in password):
        errors.append("At least one lowercase letter")
    if not any(c.isdigit() for c in password):
        errors.append("At least one number")
    
    if errors:
        print("Password needs:")
        for error in errors:
            print(f"  - {error}")
        print("Try again.\n")
    else:
        print("Password accepted!")
        break


# Multiplication Table Generator
size = int(input("Enter table size: "))

print("\nMultiplication Table")

print(" ",end=" ")
for i in range(1, size + 1):
    print(f"{i:4}", end="")
print("\n   " + "-" * (size * 4))

for i in range(1, size + 1):
    print(f"{i:2} |", end="")
    for j in range(1, size + 1):
        print(f"{i * j:4}", end="")
    print()

# Print all even numbers
for even in range(2,21,2):
    print(even,end=" ")


# Calculate sum of all numbers between 1 and 100
total 
i = 1
while i <= 100:
    total = total + i
    i = i + 1
print(f"Sum: {total}")


# Print pattern of stars
for i in range(1,6):
    print("*" * i)


# Keep asking untill user enter 0 then print sum
sum_ = 0
while True:
    num = int(input("Enter a number (0 to quit): "))
    if num == 0:
        break
    sum_ = sum_ + num
print(f"Sum: {sum_}")


# Square list through list comprehension between 1 and 10
sqr = [n**2 for n in range(1,11)]
print(sqr)

