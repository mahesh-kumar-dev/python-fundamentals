# String Data Type Tutorial 
print("-------String Data Type tutorial-------")
# Use double quotes when string has apostrophe
text1 = "It's raining"        # No backslash needed

# Use single quotes when string has double quotes
text2 = 'He said "Hello"'     # No backslash needed

# Use triple quotes for multiple lines or long text
text3 = """
Dear Jai Kumar,
Thank you for your interest.

Sincerely,
Hari Lal
"""
print(text1)
print(text2)
print(text3)

empty = ""
print(len(empty))

print("\n-------String Operations------")
# + operator to join strings
first = "Mahesh"
last = "Kumar"
full = first + " " + last
print(full)

# Multiple Strings
greetings = "Hello" + " " + "World"+ "!"
print(greetings)

# Cannot combine the str and integer
age = 24
message = "Age: " + str(age) # correct age
print(message)

# Use * to repeat strings 
laugh = "Ha"*3
print(laugh)

line = '-'*20
print(line)

# Create pattern
pattern = ".*"*5
print(pattern)

# String length 
# Use len() to find how many characters are in a string
print("\n-----String Length------(.len())")
name = "Aeogon"
print(name, " length: ", len(name))

msg = 'Hello World'
print(msg, ' length: ', len(msg))

# Accessing Character through indexing 
print("\n----Accessing Characters----- string[inx]")
lan = "Python"
print("Word: ", lan)
print(lan[0])
print(lan[-1])
print(lan[-3])
'''
String: "Python"

Positive indices:   0    1    2    3    4    5
                  ┌────┬────┬────┬────┬────┬────┐
                  │ P  │ y  │ t  │ h  │ o  │ n  │
                  └────┴────┴────┴────┴────┴────┘
Negative indices:   -6   -5   -4   -3   -2   -1

name[0] = 'P'    # First character
name[5] = 'n'    # Last character
name[-1] = 'n'   # Last character (easier!)
name[-6] = 'P'   # First character

'''
ln = "Hello"
# ln[0] = "J"

# We can create new String 
ln = "J"+ ln[1:] # Join J with Hello ~ Jello
print(ln) # Jello

print("\n--------Slicing String------string[start:end]")
# •	start – where to begin (including this character)
# •	end – where to stop (NOT including this character)
text = "Python Programming"
print(text[0:6])
print(text[7:18])
print(text[:6])
print(text[7:])
print(text[:]) # Copy entire string

# Every Second Character
print(lan[::2])


print(text[1::3])

# Reverse String
print(lan[:: -1])

ms = "Hello World"

# First Five letters
print(ms[:5])

# Last Five letters
print(ms[-5:])

# Skip first and last letter]
print(ms[1:-1])

print("\n--------Common String Methods------")
print("------Case Conversion------")

# UpperCase
print(ms.upper())

# LowerCase
print(ms.lower())

# Title Case  (Each word Capitalized)
print(ms.title())

# capitalize() first letter only capital
print(ms.capitalize())

# swapcase
print(ms.swapcase())

print("\n-------Finding Text--------")
sentence = "The cat sit on the mat."

print(sentence)

# Find position of cat 
print("Find position of cat: ", sentence.find("cat"))

# Find the position of dog
print("Find position of dog: ", sentence.find("dog"))

# Count Occurence
print("Occurence of at: ", sentence.count("at"))

# Checks if starts or ends with something
print("Starts with The: ",sentence.startswith("The"))
print("Ends with mat: ",sentence.endswith("mat"))


print("\n------Removing Whitespaces------")
messy = "  Hello  "

# remove spaces from both ends
print(messy.strip())

# remove from left only
print(messy.lstrip())

# remove from right only
print(messy.rstrip())

print("\n------Replacing Parts-----")

# Replace World with Python
new_ms = ms.replace("World", "Python")
print(new_ms)

# Replace With limit
line1  = "cat cat cat"
print(line1.replace("cat","dog",2))

print("\n-------Splitting and Joining--------")

sentence1 = 'The quick brown fox'
print(sentence1.split()) # Split by spaces

# Split by specific characters
data =  "apple,banana,cherry"
fruits = data.split(",")
print(fruits) 

# Join list into Strings
words = ['Hello','World']
print(" ".join(words))

# Join with comma 
csv = ",".join(fruits)
print(csv)


print("\n-----Checking String Content-----")
print("Hello".isalpha()) 
print("Hello123".isalpha())
print("123".isdigit())
print("123abc".isdigit())
print("abc123".isalnum())
print("hello!".isalnum())
print(" ".isspace())
print("Hello".isupper())
print("HELLO".isupper())
print('hello'.islower())


print("\n-------String Formatting---------")
# Method 1 f-String
name = "Alice"
age = 19

# put variables directly inside {}
mes = f"Hello, {name}! You are {age} year old."
print(mes)

# Can Do calculations inside {}
price = 19.99
qty = 3
total = f"Total: ${price*qty}"
print(total)

# Format Numbers
pi = 3.14159
print(f"Pi to 2 decimals: {pi:.2f}")

# Call Methods 
print(f"Capitalized: {name.title()}")



# Method 2 Format Method
# .format() works in older python versions
mes = "Hello, {}! You are {} year old.".format(name,age)
print(mes)

# using number can rearrange
mes = "{1} is {0} year old".format(30,"Alice")
print(mes)

# using names
mes = "Hello, {name}! Age: {age}".format(name="Alina", age=23)
print(mes)

print("\n-----Format Specifiers Paddings and ALignments-----")
# Right align with width

print(f"|{name:10}|")  # |Alice     |
print(f"|{name:>10}|") # |     Alice|
print(f"|{name:<10}|") # |Alice     |
print(f"|{name:^10}|") # |  Alice   |

# Fill with characters
print(f"{name:*^10}")

# Number
num = 100000
print(f"{num:09d}")
print(f"{num:+d}")
print(f"{num:,d}")


print("\n-------Escape Characters--------")
# newline (\n)
print("Hello\nGoat")

# tab (\t)
print("Virat\tKohli")

# Backslash (\\) to print a single backslash
print("C:\\User\\Name")

# Quotes inside
print('It\'s Nice!')
print("She said, You are my \"Baba Janu\".")

print("\n------Raw String------")
# Use r before quotes to treat backslashes as normal characters.
# Without raw string we need escaping
path = "C:\\User\\Name\\Documents."

# with raw string
path = r"C:\Users\Name\Documents."
print(path)

print("\n\n-----Practice Questions--------")
# Ask users for name and age
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Clean up the name (Remove spaces and capitalize it)
name = name.strip().title()

next_age = age + 1
message =f"""
Hello, {name}!
You are currently {age} year old.
Next year you\'ll be {next_age} year old.
Nice to meet you
"""
print(message)

print("\n-----Password Strengthen-------")
password = input("Enter your password: ")

# Check Length
length_ok = len(password)>=8

# Check for number
has_number = any(char.isdigit()  for char in password)

# Check for upperCase
has_upperCase = any(char.isupper() for char in password)

# Create Feedback
feedback = f"""
Password: {password}
Length (8+ char): {length_ok}
Contains Number: {has_number}
Contains UpperCase: {has_upperCase}
"""
print(feedback)

if length_ok and has_number and has_upperCase:
    print("Strong Password.")
else: 
    print("Weak Password!!! Please improve.")


print("\n-----Email Formatter-----")
# Get User Informations
first = input("Enter your first name: ").strip().lower()
last = input("Enter your last name: ").strip().lower()
company = input("Company name: ").strip().lower()

# Generate Email
email = f"{first}.{last}@{company}.com"

print(f"\nSuggested Email: {email}")

display = f"{first.title()} {last.title()}"
print(f"Display name: {display}")

# Create Signature
signature = f"""
Best regards,
{display}
company: {company.title()}
Email: {email}
"""
print(signature)

'''
# CREATING STRINGS
"Hello"          # Double quotes
'Hello'          # Single quotes
"""Multi
line"""          # Triple quotes

# BASIC OPERATIONS
str1 + str2      # Concatenation (join)
str * 3          # Repetition
len(str)         # Length

# INDEXING
str[0]           # First character
str[-1]          # Last character

# SLICING
str[2:5]         # Characters 2-4
str[:5]          # First 5 characters
str[5:]          # Characters 5 to end
str[::-1]        # Reverse string

# CASE METHODS
str.upper()      # UPPERCASE
str.lower()      # lowercase
str.title()      # Title Case
str.capitalize() # First letter capital

# SEARCH METHODS
str.find("sub")  # Find position (-1 if not found)
str.count("sub") # Count occurrences
str.startswith("prefix")
str.endswith("suffix")

# CLEANING
str.strip()      # Remove whitespace from ends
str.lstrip()     # Remove from left
str.rstrip()     # Remove from right

# MODIFYING
str.replace("old", "new")
str.split(",")   # Split into list
",".join(list)   # Join list into string

# CHECKING
str.isalpha()    # Only letters?
str.isdigit()    # Only digits?
str.isalnum()    # Letters or digits?
str.isspace()    # Only spaces?

# FORMATTING (f-strings)
f"Hello {name}"
f"{num:.2f}"     # 2 decimal places
f"{num:05d}"     # Zero pad to 5 digits
f"{text:10}"     # Width 10
f"{text:<10}"    # Left align
f"{text:>10}"    # Right align
f"{text:^10}"    # Center

# ESCAPE CHARACTERS
\n    # Newline
\t    # Tab
\\    # Backslash
\'    # Single quote
\"    # Double quote
'''

print("\n-----Printing Intials of name-------")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

intials = first_name[0].upper() +"."+ last_name[0].upper()
print(f"Initials: {intials}")

print("\n------Palindrome-----")
word = input("Enter any word: ").lower()
if word == word[::-1]:
    print(f"'{word}' is palindrome.")
else:
    print(f"'{word}' is NOT palindrome!!!!")

print("\n---------Counts Vowels-------")
sentence = input("Enter any string: ").lower()
vowels = "aeiou"
count = 0
for char in sentence:
    if char in vowels:
        count +=1

print(f"Number of Vowels: {count}")

print("\n-------NameTag-----")
first = input("Enter your first name: ").strip().lower()
last = input("Enter your last name: ").strip().lower()

nameTag = f"{last} , {first}"
print(f"NameTag: {nameTag}")



