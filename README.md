# 🐍 Python Fundamentals

A structured learning repository containing my Python programs, exercises, examples, and small projects created while building a strong foundation in Python programming.

This repository documents my practical learning journey — from basic Python syntax and data types to control flow, collections, functions, modules, packages, file handling, JSON, exception handling, and basic projects.

> **Learn → Understand → Code → Practice → Improve**

---

## 📌 What Is This Repository?

This is my **Python learning repository**.

I use this repository to organize the Python programs and exercises I create while learning and practicing programming concepts. This repository represents my Python journey from scratch and shows what I have practiced, understood, and continued to learn.

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
- Simple Projects

---

# 📚 Topics Covered

## 1. Python Basics

Learning the basic structure and syntax of Python programs.

### Topics Include

- Python syntax
- Program structure
- Comments
- Printing output
- Variables
- Basic expressions
- User input
- Basic operations

### Example

```python
name = input("Enter your name: ")
print("Hello", name)
```

---

## 2. Data Types

Understanding the different types of data used in Python.

### Topics Include

- Integers
- Floating-point numbers
- Strings
- Boolean values
- Type checking
- Type conversion
- Basic data manipulation

### Example

```python
age = 20
height = 5.8
name = "Mahesh"
is_student = True

print(type(age))
print(type(height))
print(type(name))
print(type(is_student))
```

---

## 3. Numbers

Practice with numerical values and arithmetic operations.

### Topics Include

- Integers
- Floating-point numbers
- Arithmetic operators
- Mathematical expressions
- Numerical calculations

### Example

```python
a = 10
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

---

## 4. Conditional Statements

Learning how programs make decisions based on conditions.

### Topics Include

- `if`
- `if-else`
- `elif`
- Nested conditions
- Comparison operators
- Logical operators

### Example

```python
marks = 75

if marks >= 50:
    print("Pass")
else:
    print("Fail")
```

---

## 5. Loops

Learning how to repeat operations efficiently.

### Topics Include

- `for` loops
- `while` loops
- Iteration
- Loop conditions
- Repeated execution
- Loop control

### Example

```python
for number in range(1, 6):
    print(number)
```

---

## 6. Strings

Learning how to work with text data in Python.

### Topics Include

- Creating strings
- String indexing
- String slicing
- String concatenation
- String formatting
- String operations

### Example

```python
name = "Python"

print(name[0])
print(name[1:4])
print(name.upper())
```

---

## 7. String Methods

Practice using Python's built-in string methods.

### Topics Include

- `upper()`
- `lower()`
- `strip()`
- `replace()`
- `split()`
- `join()`
- `find()`
- `count()`
- String checking methods

### Example

```python
text = "hello python"

print(text.upper())
print(text.replace("python", "world"))
```

---

## 8. Lists

Learning Python's mutable collection type.

### Topics Include

- Creating lists
- Indexing
- Slicing
- Updating elements
- Adding elements
- Removing elements
- List methods
- Iterating through lists

### Example

```python
numbers = [10, 20, 30, 40]

numbers.append(50)

print(numbers)
```

---

## 9. Tuples

Learning how to work with immutable collections.

### Topics Include

- Creating tuples
- Tuple indexing
- Tuple slicing
- Tuple methods
- Accessing tuple elements
- Immutable data

### Example

```python
student = ("Mahesh", 20, "Software Engineering")

print(student[0])
```

---

## 10. Sets

Learning how Python stores unique values.

### Topics Include

- Creating sets
- Adding elements
- Removing elements
- Unique values
- Set operations
- Set methods

### Example

```python
numbers = {1, 2, 3, 4, 4}

print(numbers)
```

---

## 11. Dictionaries

Learning key-value based data storage.

### Topics Include

- Creating dictionaries
- Keys and values
- Accessing values
- Adding items
- Updating items
- Removing items
- Dictionary methods
- Iterating through dictionaries

### Example

```python
student = {
    "name": "Mahesh",
    "age": 20,
    "program": "Software Engineering"
}

print(student["name"])
```

---

## 12. Functions

Learning how to create reusable blocks of code.

### Topics Include

- Function definition
- Function calling
- Parameters
- Arguments
- Return values
- `print()` vs `return`
- Reusable code
- Basic function design

### Example

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

---

## 13. Modules

Learning how Python programs can be divided into reusable modules.

### Topics Include

- Creating modules
- Importing modules
- Using imported functions
- Organizing code
- Code reuse

### Example

```python
import math

print(math.sqrt(25))
```

---

## 14. Packages

Learning how related Python modules can be organized into packages.

### Topics Include

- Package structure
- Modules inside packages
- Importing from packages
- Organizing related code
- Reusable program components

The repository contains practice with directories such as:

```text
module/
my_package/
parent/
```

---

## 15. File Handling

Learning how Python programs interact with files.

### Topics Include

- Opening files
- Reading files
- Writing files
- Appending data
- File modes
- Closing files
- Working with text files

### Example

```python
file = open("data.txt", "r")

content = file.read()

print(content)

file.close()
```

### Recommended Approach

As I continue learning file handling, I will also practice using `with open()` because it automatically manages the file resource.

```python
with open("data.txt", "r") as file:
    content = file.read()

print(content)
```

---

## 16. JSON

Learning how to work with structured JSON data.

### Topics Include

- JSON structure
- Reading JSON files
- Writing JSON files
- Python dictionaries and JSON
- Loading JSON data
- Saving JSON data

### Example

```python
import json

data = {
    "name": "Mahesh",
    "age": 20
}

with open("student.json", "w") as file:
    json.dump(data, file, indent=4)
```

---

## 17. CSV

Learning how to work with comma-separated data.

### Topics Include

- CSV files
- Reading CSV data
- Writing CSV data
- Processing tabular information
- Working with structured data

The repository contains CSV practice files such as:

```text
contacts.csv
person.csv
```

### Example

```python
import csv

with open("contacts.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
```

---

## 18. Date and Time

Learning how Python works with dates and time.

### Topics Include

- Date objects
- Time objects
- Date and time operations
- Formatting date and time
- Working with Python's date/time functionality

### Example

```python
from datetime import datetime

current_time = datetime.now()

print(current_time)
```

---

## 19. Exception Handling

Learning how to handle errors and exceptional situations.

### Topics Include

- Exceptions
- `try`
- `except`
- `else`
- `finally`
- Runtime errors
- Handling unexpected situations

### Example

```python
try:
    number = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

### Complete Example

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ValueError:
    print("Please enter a valid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Result:", result)

finally:
    print("Program execution completed.")
```

---

## 20. Simple Projects

This section contains small projects created to apply Python concepts in practical situations.

The purpose of these projects is to combine multiple concepts rather than practicing each concept independently.

### Project Areas

- Calculator
- Number guessing game
- Contact management
- Student management
- File-based applications
- Small automation scripts
- Beginner-friendly Python projects

### Example Project Workflow

```text
Problem
   ↓
Plan the solution
   ↓
Write Python code
   ↓
Run the program
   ↓
Test different inputs
   ↓
Find and fix errors
   ↓
Improve the solution
   ↓
Commit to GitHub
```

---

# 📂 Repository Structure

The repository contains individual Python programs, supporting data files, modules, packages, and small projects.

```text
python-fundamentals/
│
├── README.md
├── .gitignore
│
├── Python practice programs/
│   ├── basics/
│   ├── data_types/
│   ├── numbers/
│   ├── conditions/
│   ├── loops/
│   ├── strings/
│   ├── lists/
│   ├── tuples/
│   ├── sets/
│   └── dictionaries/
│
├── functions/
├── module/
├── my_package/
├── parent/
│
├── file_handling/
├── json/
├── csv/
├── date_time/
├── exception_handling/
│
├── Simple_Project/
│
├── .py files
├── .txt files
├── .csv files
└── .json files
```

> **Note:** The repository structure may evolve as my Python knowledge and project organization improve.

---

# 🛠️ Technologies & Tools

| Tool / Technology | Purpose |
|---|---|
| **Python** | Programming language |
| **Python Interpreter** | Running Python programs |
| **Git** | Version control |
| **GitHub** | Repository hosting and code management |
| **VS Code** | Writing and managing code |
| **Command Line / Terminal** | Running and testing programs |

---

# ▶️ How to Run

## 1. Check Python Installation

Open your terminal or command prompt and run:

```bash
python --version
```

If your system uses `python3`, run:

```bash
python3 --version
```

---

## 2. Clone the Repository

Clone the repository using Git:

```bash
git clone https://github.com/mahesh-kumar-dev/python-fundamentals.git
```

Move into the repository:

```bash
cd python-fundamentals
```

---

## 3. Run a Python Program

For example:

```bash
python program.py
```

Or:

```bash
python3 program.py
```

---

## 4. Run a Program from a Folder

If the program is inside a folder:

```bash
python folder_name/program.py
```

---

# 📈 Learning Progress

My learning approach follows a gradual progression:

```text
Python Basics
      ↓
Data Types
      ↓
Numbers
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
Date & Time
      ↓
Exception Handling
      ↓
Simple Projects
      ↓
Advanced Python
```

---

# 📊 Current Learning Areas

| Area | Status |
|---|---|
| Python Basics | 🟢 Learning / Practicing |
| Data Types | 🟢 Practicing |
| Numbers | 🟢 Practicing |
| Conditional Statements | 🟢 Practicing |
| Loops | 🟢 Practicing |
| Strings | 🟢 Practicing |
| Collections | 🟢 Practicing |
| Functions | 🟢 Practicing |
| Modules | 🟢 Practicing |
| Packages | 🟢 Practicing |
| File Handling | 🟢 Practicing |
| JSON | 🟢 Practicing |
| CSV | 🟢 Practicing |
| Date & Time | 🟢 Practicing |
| Exception Handling | 🟢 Practicing |
| Projects | 🟡 Developing |
| Advanced Python | 🔵 Planned |

---

# 🚀 Future Learning

Planned areas of further study include:

- Object-Oriented Programming
- Advanced functions
- List, dictionary, and set comprehensions
- Iterators and generators
- Decorators
- Advanced exception handling
- Virtual environments
- Python libraries
- Data Structures and Algorithms
- Automation
- Data analysis
- APIs
- Database connectivity
- Testing
- Larger Python projects

---

# 📚 Learning Philosophy

I believe programming is learned through **consistent practice and implementation**.

My approach is:

```text
Learn the concept
       ↓
Understand the concept
       ↓
Write the code
       ↓
Run and test the code
       ↓
Find errors
       ↓
Debug the program
       ↓
Practice variations
       ↓
Build projects
       ↓
Improve the code
       ↓
Commit to GitHub
```

The goal is not simply to collect code, but to understand **how and why the code works**.

This repository represents that learning process.

---

# 🔄 My Practice Cycle

For every new concept, I try to follow a practical cycle:

1. **Learn** — Understand the concept and syntax.
2. **Understand** — Study how and why it works.
3. **Write** — Implement the concept myself.
4. **Run** — Execute the program and observe the output.
5. **Test** — Try different inputs and situations.
6. **Debug** — Find and fix errors.
7. **Practice** — Create variations of the program.
8. **Improve** — Make the solution cleaner and better.
9. **Document** — Organize the code in the repository.
10. **Commit** — Save the progress using Git and GitHub.

---

# 🌱 Why I Created This Repository

I created this repository to make my Python learning journey visible and organized.

Instead of keeping programs scattered across different folders on my computer, I use GitHub to:

- Store my programs
- Track changes
- Review older code
- Practice Git
- Learn GitHub
- Organize programming exercises
- Share my progress
- Build my programming portfolio

Every program represents a step in my learning journey.

---

# 💡 What I Am Trying to Improve

Through this repository, I am working on improving:

- Programming fundamentals
- Logical thinking
- Problem-solving
- Debugging skills
- Code organization
- Code readability
- Understanding of Python syntax
- Ability to write reusable code
- Ability to work with files and data
- Git and GitHub skills
- Project-building skills

---

# 🚀 Long-Term Goal

My long-term goal is to move from basic Python programming toward building practical and real-world applications.

My planned progression is:

```text
Python Fundamentals
        ↓
Advanced Python
        ↓
Object-Oriented Programming
        ↓
Data Structures & Algorithms
        ↓
Libraries & Frameworks
        ↓
APIs & Databases
        ↓
Automation
        ↓
Data Analysis
        ↓
Real-World Projects
        ↓
Professional Software Development
```

---

# 👨‍💻 Author

## Mahesh Kumar

**Computer Science / Software Engineering Student**

I am building my programming skills through continuous practice, implementation, problem-solving, and project development.

GitHub: **@mahesh-kumar-dev**

---

# ⭐ Repository Status

**Status: 🟢 Active**

This repository is actively evolving as I continue learning and practicing Python.

New programs, exercises, concepts, and projects will be added over time.

> **Consistency → Practice → Problem Solving → Projects → Growth**

---

# ⭐ If You Find This Repository Useful

If this repository helps you understand Python concepts or gives you useful examples for your own learning, feel free to explore the code and follow the learning journey.

---

<p align="center">
  <b>🐍 Learning Python one program at a time.</b>
</p>

<p align="center">
  <b>Learn → Code → Practice → Debug → Improve → Build</b>
</p>
