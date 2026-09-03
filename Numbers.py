
# Integers
print("-------Integer-------")
'''
	Counting things (3 apples, 5 people)
	Ages (25 years old)
	Index positions (item #1, #2, #3)
	Loop counters (repeat 10 times)

'''

a = 15
b = 4
print("a: ", a , "  ", "b: ",b)
# Addition 
sum_result = a +  b
print("Addition: ", sum_result)

# Subtraction
diff_result = a - b
print("Subtraction: ", diff_result)

# Product 
product_result = a * b
print("Multiplication: ", product_result)

# Division
div_result = a / b
print("Division: ", div_result)

# Floor Division
fDiv_result = a // b
print("Floor Division: ", fDiv_result)

# Modulus 
modulus_result = a % b
print("Modulus (Remainder): ", modulus_result)

# Exponent
power_result = a ** b
print("Exponent: ", power_result)


# Special Integer form 
big_number = 999999999999999999999
print(big_number + 1)

# underscore for readability 
million = 1_000_000
billion = 1_000_000_000
print("Million: ", million)
print("Billion: ", billion)

# Different number bases 
binary =    0b1010
octal = 0o15
hexadecimal = 0xB
print(binary, octal , hexadecimal)

'''
	Money and prices ($19.99)
	Measurements (3.14 meters)
	Scientific calculations (π = 3.14159...)
	Percentages (0.75 = 75%)

'''
print("\n-------Float-------")

# Basic math works the same
x = 5.5
y = 2.0

print(x + y)   # 7.5
print(x - y)   # 3.5
print(x * y)   # 11.0
print(x / y)   # 2.75

# Floor division with floats still gives float
print(x // y)  # 2.0

# Modulus works with floats
print(x % y)   # 1.5
# Watch out for this!
print(0.1 + 0.2)        # 0.30000000000000004 (not 0.3!)
print(0.1 + 0.2 == 0.3) # False (because of tiny difference)

# More examples
print(1.1 * 3)          # 3.3000000000000003
print(0.1 * 10)         # 1.0 (sometimes it's exact)

# How to compare floats safely
result = 0.1 + 0.2
expected = 0.3
difference = abs(result - expected)  # Absolute difference
print(difference < 0.0000001)        # True (close enough)

infinity = float('inf')
print(infinity > 999999923)
print(infinity +899)

neg_infinity = float('-inf')
print(neg_infinity)

not_a_number = float('nan')
print(not_a_number == not_a_number)


num_str = "23"
num_int = int(num_str)
print(num_int)
print(type(num_int))

price_str = "19.99"
price_float = float(price_str)
print(price_float)

print()
# convert to float for decimals
price_input = input("Enter the price $: ")
price = float(price_input)
total = price*1.08
print("Total with tax $: ", total)



import math
print("\n-----Built in function------")
# abs() - absolute value (removes negative sign)
print(abs(-6))
print(abs(7))
print(abs(-3.143))
print(pow(2,3))
print(3**3)

# advance pow 3 arguments
print(pow(2,10,100)) # 24 (2¹⁰ % 100)

# round() - round to nearest integer or decimal places
print(round(3.124))
print(round(3.1783, 2)) # 3.14 (2 decimal places)
print(round(2.675, 2))  # 2.67 (precision quirk)

# min() and max() - smallest/largest
print(min(5, 2, 8, 1, 9))  # 1
print(max(5, 2, 8, 1, 9))  # 9


# sum() - add all numbers in a list (more on lists later)
numbers = [1,2,3,4,5,6]
print(numbers)
print("Sum: ", sum(numbers))

# Square Root
print("Square root of 16: ", math.sqrt(16))
print("Square root of 2: ", math.sqrt(2))

# Pi (π)
print("Value of Pi: ",math.pi)

# Ceil (round UP) and Floor (round DOWN)
print(math.ceil(3.2))
print(math.floor(3.9))

# Factorial (5! = 5×4×3×2×1)
print("Factorial of 5: ", math.factorial(5))

# Trigonometry (angles in radians)
print(math.sin(math.pi/2))

import random
print("-----Random Numbers-----")
# Random float between 0.0 and 1.0
print(random.random())

# Random integer between 1 and 10 (inclusive)
print(random.randint(1,10))

# Random float between 1 and 10
print(random.uniform(1,10))

# Random choice from a list
colors = ["reds", "green", "blue"]
print(random.choice(colors))

# Roll a six-sided die
dice_roll = random.randint(1,6)
print("you rolled a dice: ", dice_roll)

# roll multiple dice
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
total = dice1 + dice2
print("You rolled ", dice1 , " and ", dice2, " = ",total)

print("\n-----Simple Calculator------")
num1 = input("Enter your first number: ")
num2 = input("Enter your second number: ")

num_float1 = float(num1)
num_float2 = float(num2)

sum_ = num_float1 + num_float2
diff_ = num_float1 - num_float2
multi_ = num_float1 * num_float2
div_ = num_float1 /  num_float2

print("\n-----Results-----")
print(num_float1 , " + ",num_float2 ," = ", sum_)
print(num_float1 , " - ",num_float2 ," = ",diff_)
print(num_float1 , " * ",num_float2 ," = ", multi_)
print(num_float1 , " / ",num_float2 ," = ", div_)


print("\n----Temperature Converter------")
# Convert Celsius to Fahrenheit

celsius = float(input("Enter temperature in celsius: "))
fahrenheit = (celsius*9/5) + 32

print(celsius, "°C =", fahrenheit , "°F")

# Convert Fahrenheit to Celsius

fahrenheit1 = float(input("Enter temperature in fahrenheit: "))
celsius1 = (fahrenheit1 - 32)*5/9

print(fahrenheit1 , "°F = ",celsius1, "°C")


print("\n------Shopping Cart--------")
item1 = float(input("Enter the price of item 1 $: "))
item2 = float(input("Enter the price of item 2 $: "))
item3 = float(input("Enter the price of item 3 $: "))

# Total price of 3 items 
sub_total = item1 + item2 + item3

# tax rate on each item 
tax_rate = 0.08

# Calculate tax on 3 items
tax = sub_total * tax_rate

# Calculate total price including taxes
total_price = tax + sub_total

# Displaying Results
print("\n-------Receipt---------")
print("SubTotal $: ", round(sub_total,2))
print("Tax (8%) $: ", round(tax, 2))
print("Total price $: ", round(total_price,2))


print("\n-----Practice Questions-------")
print("\n------Calculate Area Of Circle------")
# Taking radius input from user & converting to float
radius = float(input("Enter the radius of circle: "))

# Area = π × radius² using math library
area = round((math.pi * math.pow(radius,2)), 2)


# Displaying results
print("Radius: ", radius)
print("Area: ",area)

print("\n-----Even Odd Program------")
inp = int(input("Enter number: "))
if inp % 2 == 0 : 
    print(inp," number is Even.")
else:
    print(inp, " number is Odd.") 
    
print("\n-----Simple Interest Calculator-----")
principal = float(input("Enter your amount: "))
interest_rate = float(input("Enter interest rate (in decimals like 0.05 for 5%: )"))
time = int(input("Enter number of year: "))


# Interest formula  I = PRT
interest = principal * time * interest_rate

total_amount = interest + principal

# Displaying Results
print("Amount: ", principal)
print("Interest rate: ", interest_rate)
print("Time (years): ", time)
print("Interest Amount: ", round(interest,2))
print("Total Amount: ",round(total_amount,2))


print("\n-------Number Guessing Game-----")
guess = int(input("Enter your guess in between 1 & 10: "))
secret = random.randint(1,10)

if guess == secret:
    print("You win correct guess: ")
else: 
    print("You lose !!! Correct guess was ", secret)



