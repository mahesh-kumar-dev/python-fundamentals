🐍 Python Fundamentals

A structured learning repository documenting my journey of learning Python from the fundamentals to practical programming.

This repository contains the Python programs, exercises, examples, practice files, modules, packages, and small projects that I create while developing my programming skills.

Learn → Understand → Code → Practice → Improve

📌 About This Repository

This is my Python learning repository, created to organize and document my practical programming journey.

The main purpose of this repository is not simply to store code. It is also a record of what I have learned, practiced, tested, and improved over time.

Through this repository, I aim to:

Practice Python programming consistently

Build strong programming fundamentals

Improve logical and problem-solving skills

Understand concepts through implementation

Organize my programs and learning material

Track my progress over time

Learn Git and GitHub through real projects

Build a public programming portfolio

Apply Python concepts through practical projects

The repository will continue to evolve as I learn new concepts and develop more advanced programs.

📚 Topics Covered

The repository currently focuses on the following Python fundamentals:

#

Topic

What I Practice

01

Python Basics

Syntax, output, input, expressions

02

Comments

Single-line and multi-line comments

03

Variables & Data Types

Variables, integers, floats, strings, booleans

04

Numbers

Arithmetic operations and numerical calculations

05

Conditional Statements

if, elif, else, nested conditions

06

Loops

for, while, iteration and loop control

07

Strings

Indexing, slicing, concatenation and formatting

08

String Methods

upper(), lower(), strip(), replace(), split() and more

09

Lists

Indexing, slicing, updating and list methods

10

Tuples

Immutable collections and tuple operations

11

Sets

Unique values and set operations

12

Dictionaries

Key-value data and dictionary methods

13

Functions

Parameters, arguments, return values and reusable code

14

Modules

Imports, reusable modules and code organization

15

Packages

Package structure and related modules

16

File Handling

Reading, writing, appending and file modes

17

JSON

Loading, writing and processing JSON data

18

CSV

Reading, writing and processing tabular data

19

Date & Time

Dates, times and formatting

20

Exception Handling

try, except, else, finally and errors

21

Simple Projects

Combining multiple concepts into practical programs

🧠 Learning Roadmap

My Python learning progression follows this path:

Python Basics
      ↓
Variables & Data Types
      ↓
Numbers & Operators
      ↓
Conditional Statements
      ↓
Loops
      ↓
Strings
      ↓
Lists, Tuples, Sets & Dictionaries
      ↓
Functions
      ↓
Modules & Packages
      ↓
File Handling
      ↓
JSON & CSV
      ↓
Date & Time
      ↓
Exception Handling
      ↓
Simple Projects
      ↓
Advanced Python

📖 Concepts Practiced

1. Python Basics

Learning the basic structure and syntax used to write Python programs.

Topics

Python syntax

Program structure

Comments

Printing output

User input

Variables

Expressions

Basic operators

Example

name = input("Enter your name: ")
print("Hello", name)

2. Variables & Data Types

Learning how Python stores and represents different types of information.

Topics

Variables

Integers

Floating-point numbers

Strings

Boolean values

type()

Type conversion

Example

age = 20
height = 5.8
name = "Mahesh"
is_student = True

print(type(age))
print(type(height))
print(type(name))
print(type(is_student))

3. Numbers

Practicing numerical values and arithmetic operations.

Topics

Integers

Floating-point numbers

Addition

Subtraction

Multiplication

Division

Modulus

Exponents

Mathematical expressions

Example

a = 10
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)

4. Conditional Statements

Learning how programs make decisions based on conditions.

Topics

if

elif

else

Nested conditions

Comparison operators

Logical operators

Example

marks = 75

if marks >= 50:
    print("Pass")
else:
    print("Fail")

5. Loops

Learning how to repeat instructions efficiently.

Topics

for loops

while loops

range()

Iteration

Loop conditions

break

continue

Example

for number in range(1, 6):
    print(number)

6. Strings

Learning how to work with text data.

Topics

Creating strings

Indexing

Slicing

Concatenation

String formatting

String operations

Example

name = "Python"

print(name[0])
print(name[1:4])
print(name.upper())

7. String Methods

Practicing Python's built-in methods for manipulating text.

Topics

upper()

lower()

strip()

replace()

split()

join()

find()

count()

String checking methods

Example

text = "hello python"

print(text.upper())
print(text.replace("python", "world"))

8. Lists

Learning Python's mutable collection type.

Topics

Creating lists

Indexing

Slicing

Updating elements

Adding elements

Removing elements

List methods

Iterating through lists

Example

numbers = [10, 20, 30, 40]

numbers.append(50)

print(numbers)

9. Tuples

Learning how to work with immutable collections.

Topics

Creating tuples

Indexing

Slicing

Tuple methods

Accessing elements

Immutability

Example

student = ("Mahesh", 20, "Software Engineering")

print(student[0])

10. Sets

Learning how Python stores collections of unique values.

Topics

Creating sets

Adding elements

Removing elements

Unique values

Set operations

Set methods

Example

numbers = {1, 2, 3, 4, 4}

print(numbers)

11. Dictionaries

Learning key-value based data storage.

Topics

Creating dictionaries

Keys and values

Accessing values

Adding items

Updating items

Removing items

Dictionary methods

Iterating through dictionaries

Example

student = {
    "name": "Mahesh",
    "age": 20,
    "program": "Software Engineering"
}

print(student["name"])

12. Functions

Learning how to create reusable blocks of code.

Topics

Function definition

Function calling

Parameters

Arguments

Return values

print() vs return

Reusable code

Basic function design

Example

def add(a, b):
    return a + b

result = add(10, 20)

print(result)

13. Modules

Learning how Python programs can be divided into reusable modules.

Topics

Creating modules

Importing modules

Using imported functions

Code reuse

Organizing programs

Example

import math

print(math.sqrt(25))

14. Packages

Learning how related Python modules can be organized into packages.

Topics

Package structure

Modules inside packages

Importing from packages

Organizing related code

Reusable program components

Practice directories include:

module/
my_package/
parent/

15. File Handling

Learning how Python programs interact with files.

Topics

Opening files

Reading files

Writing files

Appending data

File modes

Closing files

Working with text files

Example

with open("data.txt", "r") as file:
    content = file.read()

print(content)

16. JSON

Learning how to work with structured JSON data.

Topics

JSON structure

Python dictionaries and JSON

Reading JSON files

Writing JSON files

Loading JSON data

Saving JSON data

Example

import json

data = {
    "name": "Mahesh",
    "age": 20
}

with open("student.json", "w") as file:
    json.dump(data, file, indent=4)

17. CSV

Learning how to work with comma-separated data.

Topics

CSV files

Reading CSV data

Writing CSV data

Processing tabular information

Working with structured data

Practice files include:

contacts.csv
person.csv

18. Date & Time

Learning how Python works with dates and time.

Topics

Date objects

Time objects

Date and time operations

Formatting dates and times

Python date/time functionality

19. Exception Handling

Learning how to handle errors and unexpected situations.

Topics

Exceptions

try

except

else

finally

Runtime errors

Error handling

Example

try:
    number = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero.")

🚀 Simple Projects

This section contains small projects created to apply multiple Python concepts together.

The purpose of these projects is to move beyond individual exercises and practice building complete programs.

Simple_Project/

As my skills improve, more projects will be added to this section.

📂 Repository Structure

The repository contains Python programs, supporting files, modules, packages, and projects.

python-fundamentals/
│
├── README.md
├── .gitignore
│
├── Python Practice Programs
│   ├── Basics/
│   ├── Data_Types/
│   ├── Conditional_Statements/
│   ├── Loops/
│   ├── Strings/
│   ├── Lists/
│   ├── Tuples/
│   ├── Sets/
│   ├── Dictionaries/
│   └── Functions/
│
├── module/
├── my_package/
├── parent/
│
├── Simple_Project/
│
├── *.py
├── *.txt
├── *.csv
└── *.json

The actual repository structure may evolve as the collection of programs grows.

🛠️ Technologies & Tools

Tool / Technology

Purpose

Python

Programming language

Python Interpreter

Running Python programs

VS Code

Writing and managing code

Git

Version control

GitHub

Repository hosting and code management

Command Line / Terminal

Running programs and Git commands

▶️ How to Run

1. Check Python Installation

Open a terminal or command prompt and run:

python --version

If that does not work, try:

python3 --version

2. Clone the Repository

git clone https://github.com/mahesh-kumar-dev/python-fundamentals.git

3. Open the Repository

cd python-fundamentals

4. Run a Python Program

For example:

python filename.py

Or:

python3 filename.py

Replace filename.py with the Python file you want to execute.

🧠 Learning Approach

For every topic, I try to follow this process:

Learn the Concept
       ↓
Understand the Theory
       ↓
Write the Program
       ↓
Run and Test
       ↓
Find Errors
       ↓
Debug
       ↓
Practice Variations
       ↓
Improve the Code
       ↓
Commit to GitHub

The goal is not simply to copy or memorize code.

The goal is to understand:

What the code does

How the code works

Why the code works

How to modify it

How to solve similar problems independently

📈 Learning Progress

My current learning journey is progressing from fundamentals toward more advanced Python development.

[████████░░░░░░░░░░░░] Python Fundamentals

Completed / Practicing
├── Python Basics
├── Variables & Data Types
├── Conditional Statements
├── Loops
├── Strings
├── Collections
├── Functions
├── Modules
├── Packages
├── File Handling
├── JSON
├── CSV
├── Date & Time
└── Exception Handling

Next
├── Object-Oriented Programming
├── Advanced Functions
├── Iterators & Generators
├── Comprehensions
├── Decorators
├── Virtual Environments
└── Larger Python Projects

🚀 Future Learning

After strengthening the fundamentals, I plan to explore:

Object-Oriented Programming

Advanced functions

List, dictionary and set comprehensions

Iterators and generators

Decorators

Virtual environments

Python libraries

Data Structures & Algorithms

Automation

APIs

Data analysis

Testing

Larger Python projects

📚 Learning Philosophy

I believe programming is learned through consistent practice, experimentation, problem-solving, and implementation.

My approach is:

Learn
  ↓
Understand
  ↓
Code
  ↓
Test
  ↓
Debug
  ↓
Practice
  ↓
Build
  ↓
Improve

This repository represents that learning process.

Every program added here is part of my journey toward becoming a stronger programmer.

📌 Repository Status

🟢 Actively Learning & Updating

This repository is continuously evolving as I learn and practice Python.

New:

Programs

Exercises

Concepts

Practice files

Modules

Packages

Projects

will be added over time.

Consistency → Practice → Problem Solving → Projects → Growth

👨‍💻 Author

Mahesh Kumar

Software Engineering Student

GitHub: @mahesh-kumar-dev

⭐ Support

If you find this learning journey useful, you can ⭐ star this repository and follow along as I continue learning Python.
