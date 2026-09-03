# 🐍 Python Fundamentals

A structured learning repository containing my Python programs, exercises, examples, and small projects created while building a strong foundation in Python programming.

This repository documents my practical learning journey — from basic Python syntax and data types to control flow, collections, functions, modules, packages, file handling, JSON, exception handling, and basic projects.

> **Learn → Understand → Code → Practice → Improve**

---

## 📌 What Is This Repository?

This is my **Python learning repository**.

I use this repository to organize the Python programs and exercises I create while learning and practicing programming concepts. This repository is depicting my python journey from scratch, This repository shows what I have practiced and and continued to learning.

The main purpose of this repository is not only to store code, but also to:

- Practice Python programming consistently
- Improve programming logic
- Strengthen problem-solving skills
- Understand Python concepts through implementation
- Keep my learning work organized
- Track my progress over time
- Learn Git and GitHub through real code
- Build a public programming portfolio

This repository will continue to evolve as I learn more Python concepts and develop larger projects.

---

# 🎯 What Am I Learning?

The repository covers the fundamental building blocks of Python programming.

The main areas include:

- Python Basics
- Comments
- Variables and Data Types
- Numbers
- Strings
- String Methods
- Conditional Statements
- Loops
- Lists
- Tuples
- Sets
- Dictionaries
- Functions
- Modules
- Packages
- File Handling
- JSON
- CSV Data
- Date and Time
- Exception Handling
- Basic Projects

---

# 📚 Topics Covered

## 1. Python Basics

Learning the basic structure and syntax of Python programs.

Topics include:

- Python syntax
- Program structure
- Comments
- Printing output
- Variables
- Basic expressions
- User input
- Basic operations

Example:

```python
name = input("Enter your name: ")
print("Hello", name)

2. Data Types

Understanding the different types of data used in Python.

Topics include:

Integers
Floating-point numbers
Strings
Boolean values
Type checking
Type conversion
Basic data manipulation

Example:

age = 20
height = 5.8
name = "Mahesh"
is_student = True

print(type(age))
print(type(height))
print(type(name))
print(type(is_student))
3. Numbers

Practice with numerical values and arithmetic operations.

Topics include:

Integers
Floating-point numbers
Arithmetic operators
Mathematical expressions
Numerical calculations

Example:

a = 10
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
4. Conditional Statements

Learning how programs make decisions based on conditions.

Topics include:

if
if-else
elif
Nested conditions
Comparison operators
Logical operators

Example:

marks = 75

if marks >= 50:
    print("Pass")
else:
    print("Fail")
5. Loops

Learning how to repeat operations efficiently.

Topics include:

for loops
while loops
Iteration
Loop conditions
Repeated execution
Loop control

Example:

for number in range(1, 6):
    print(number)
6. Strings

Learning how to work with text data in Python.

Topics include:

Creating strings
String indexing
String slicing
String concatenation
String formatting
String operations

Example:

name = "Python"

print(name[0])
print(name[1:4])
print(name.upper())
7. String Methods

Practice using Python's built-in string methods.

Topics include:

upper()
lower()
strip()
replace()
split()
join()
find()
count()
String checking methods

Example:

text = "hello python"

print(text.upper())
print(text.replace("python", "world"))
8. Lists

Learning Python's mutable collection type.

Topics include:

Creating lists
Indexing
Slicing
Updating elements
Adding elements
Removing elements
List methods
Iterating through lists

Example:

numbers = [10, 20, 30, 40]

numbers.append(50)

print(numbers)
9. Tuples

Learning how to work with immutable collections.

Topics include:

Creating tuples
Tuple indexing
Tuple slicing
Tuple methods
Accessing tuple elements
Immutable data

Example:

student = ("Mahesh", 20, "Software Engineering")

print(student[0])
10. Sets

Learning how Python stores unique values.

Topics include:

Creating sets
Adding elements
Removing elements
Unique values
Set operations
Set methods

Example:

numbers = {1, 2, 3, 4, 4}

print(numbers)
11. Dictionaries

Learning key-value based data storage.

Topics include:

Creating dictionaries
Keys and values
Accessing values
Adding items
Updating items
Removing items
Dictionary methods
Iterating through dictionaries

Example:

student = {
    "name": "Mahesh",
    "age": 20,
    "program": "Software Engineering"
}

print(student["name"])
12. Functions

Learning how to create reusable blocks of code.

Topics include:

Function definition
Function calling
Parameters
Arguments
Return values
print() vs return
Reusable code
Basic function design

Example:

def add(a, b):
    return a + b

result = add(10, 20)

print(result)
13. Modules

Learning how Python programs can be divided into reusable modules.

Topics include:

Creating modules
Importing modules
Using imported functions
Organizing code
Code reuse

Example:

import math

print(math.sqrt(25))
14. Packages

Learning how related Python modules can be organized into packages.

Topics include:

Package structure
Modules inside packages
Importing from packages
Organizing related code
Reusable program components

The repository contains practice with directories such as:

module/
my_package/
parent/
15. File Handling

Learning how Python programs interact with files.

Topics include:

Opening files
Reading files
Writing files
Appending data
File modes
Closing files
Working with text files

Example:

file = open("data.txt", "r")

content = file.read()

print(content)

file.close()
16. JSON

Learning how to work with structured JSON data.

Topics include:

JSON structure
Reading JSON files
Writing JSON files
Python dictionaries and JSON
Loading JSON data
Saving JSON data

Example:

import json

data = {
    "name": "Mahesh",
    "age": 20
}

with open("student.json", "w") as file:
    json.dump(data, file, indent=4)
17. CSV

Learning how to work with comma-separated data.

Topics include:

CSV files
Reading CSV data
Writing CSV data
Processing tabular information
Working with structured data

The repository contains CSV practice files such as:

contacts.csv
person.csv
18. Date and Time

Learning how Python works with dates and time.

Topics include:

Date objects
Time objects
Date and time operations
Formatting date and time
Working with Python's date/time functionality
19. Exception Handling

Learning how to handle errors and exceptional situations.

Topics include:

Exceptions
try
except
else
finally
Runtime errors
Handling unexpected situations

Example:

try:
    number = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero.")

19. Simple Projects

This section contains small projects created to apply Python concepts in practical situations.

The purpose of these projects is to combine multiple concepts rather than practicing each concept independently.

📂 Repository Structure

The repository contains individual Python programs, supporting data files, modules, packages, and small projects.

python-fundamentals/
│
├── README.md
├── .gitignore
│
├── Python practice programs
│
├── module/
├── my_package/
├── parent/
│
├── Simple_Project/
│
├── .py files
├── .txt files
├── .csv files
└── .json files

The repository structure may evolve as my Python knowledge and project organization improve.

🛠️ Tools & Technologies
Python
Git
GitHub
VS Code / Python development environment
📈 Learning Progress

My learning approach follows a gradual progression:

Python Basics
      ↓
Data Types
      ↓
Conditional Statements
      ↓
Loops
      ↓
Strings & Collections
      ↓
Functions
      ↓
Modules & Packages
      ↓
File Handling
      ↓
JSON & CSV
      ↓
Exception Handling
      ↓
Projects
      ↓
Advanced Python
🚀 Future Learning

Planned areas of further study include:

Object-Oriented Programming
Advanced functions
Iterators and generators
List/dictionary/set comprehensions
Decorators
Advanced exception handling
Virtual environments
Python libraries
Data Structures and Algorithms
Automation
Data analysis
APIs
Larger Python projects
📚 Learning Philosophy

I believe programming is learned through consistent practice and implementation.

My approach is:

Learn the concept
       ↓
Understand the concept
       ↓
Write the code
       ↓
Test the code
       ↓
Fix errors
       ↓
Practice variations
       ↓
Build projects
       ↓
Improve the code

This repository represents that learning process.

👨‍💻 Author

Mahesh Kumar

Computer Science / Software Engineering Student

GitHub: @mahesh-kumar-dev

⭐ Repository Status

This repository is actively evolving as I continue learning and practicing Python.

New programs, exercises, concepts, and projects will be added over time.

Consistency → Practice → Problem Solving → Projects → Growth

