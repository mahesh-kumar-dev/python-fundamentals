# Python Module 
# A Module is Python file that contains code you can use in other programs

'''
    Feature:
	Reuse code -> Use someone else's code without rewriting
	Organize code -> Split large programs into multiple files
	Share code -> Give your functions to others
	Standard library -> Python comes with many useful modules
	Third-party modules -> Millions of modules available online
'''

# Using Built in Modules

# Importing Module
# Method 1: Importing whole module
import math
print(math.sqrt(196))
print(math.factorial(4))

# Method 2: Import Specific Item
from math import sqrt, pi
print(sqrt(25)) # donot need math.sqrt
print(pi)

# Method 3: Import with alias (short Nickname)
import math as m
print(m.sqrt(81))

# Method 3: Import everything not recommended
from math import *
print(sin(pi/2))

# COMMON BUILT IN MODULES
'''
Module       Purpose         	        Example
math	     Mathematical functions	    math.sqrt(16)
random	     Random numbers	            random.randint(1,10)
datetime	 Dates and times	        datetime.now()
os	         Operating system	        os.getcwd()
sys	         System info	            sys.version
json	     JSON data	                json.loads()
re	         Regular expressions	    re.search()
time	     Time functions	            time.sleep(1)
'''


# CREATING OWN MODULE

# Import and use your module
from module import my_module

# Use functions from my_module
print(my_module.greet("Roshni"))
print(my_module.add(8,6))
print(my_module.PI)

# Use Class from module
calc = my_module.Calculator()
print(calc.multiply(3,7))


# Alternative import Sytle
# Import the exact functions from the modules inside the 'module' folder
from module.my_module import greet
from module.calculator import add

print(greet("Raghav"))
print(add(9,5))

# Import with alias from the correct folder path
from module import my_module as mm 
print(mm.greet("Shakira"))

# Import everything using the correct sub-module path
from module.my_module import *
print(greet("Jon Snow"))
print(add(4,5))
print(PI)


# MODULE SEARCH PATH
# Where does python look for modules
'''
1.	Current directory (where your script is)
2.	Directories in PYTHONPATH environment variable
3.	Standard library directories
4.	Site-packages (where pip installs packages)
    python
'''
import sys

# See all directories where python looks for modules
for path in sys.path:
    print(path)

# Add a custom directory (temporary)
# sys.path.append("/my/custom/path")

# Now Python will also look in /my/custom/path


# The __name__ Variable
# Every module has a __name__ variable. When you run a script directly, 
# __name__ is "__main__". When imported, it's the module's name.


# Practical Use: Testing code
from module import calculator

sum_ = add(23,56)
print(sum_)

# PACKAGES (MODULES IN FOLDER)
# A package is a folder containing modules. 
# It allows you to organize modules into groups.


'''
Package Structure
text
my_package/              # Main package folder
├── __init__.py          # Required (can be empty)
├── math_utils.py        # Module 1
├── string_utils.py      # Module 2
└── advanced/            # Sub-package
    ├── __init__.py
    └── calc.py
'''

# Import from package
from my_package import string_utils, math_utils, __init__

# math_utils module
print("Double of 6: ",math_utils.double(6))
print("Cube of 5: ",math_utils.cube(5))
print("Is 8 prime: ",math_utils.is_prime(8))
print("Square of 6: ",math_utils.sqr(6))
print("factorial of 5: ",math_utils.factorial(5))
print("first 10 Fibonacci: ",math_utils.fibonacci(10))


# string_utils module
print("Greetings: ",string_utils.greets("Alia"))
print("Capitalized: ",string_utils.whisper("WHAT ARE YOU DOING"))
print("Lowercase: ",string_utils.shout("Hey, jon!!!"))
print("Uppercase: ",string_utils.is_uppercase("Hi"))
print("Is number: ",string_utils.is_number("8"))



'''
import requests

# Make a web request
response = requests.get("https://api.github.com/users/octocat")

# Get the data
data = response.json()
print(f"Name: {data['name']}")
print(f"Location: {data['location']}")

'''

from my_package import text_utils

counts = text_utils.count_words("Air Conditioner")
reverse = text_utils.reverse_string("Payal")
palindrome = text_utils.is_palindrome("mom")

print("Word count: ",counts)
print("Reverse String: ",reverse)
print("Palindrome: ",palindrome)


from my_package import circle , rectangle 

print(f"Circle area: {circle.area(5):1f}")
print(f"Circle's circumference: {circle.circumference(7):1f}")
print(f"Rectangle area: {rectangle.area(6,7)}")
print(f"Rectangle perimeter: {rectangle.perimeter(8,7)}")