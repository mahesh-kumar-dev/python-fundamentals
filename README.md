# 🐍 Python Fundamentals
 
A structured collection of Python programs, exercises, examples, and practice projects created as part of my journey to build a strong foundation in Python programming.
 
This repository contains my hands-on practice covering fundamental Python concepts such as variables, data types, conditional statements, loops, functions, collections, modules, packages, file handling, JSON, exception handling, and basic projects.
 
> **Learn → Understand → Code → Practice → Improve**
 
---
 
## 📖 About This Repository
 
This is a learning repository created to organize my Python programming practice in one place.
 
The purpose of this repository is to document my progress through practical implementation rather than only studying programming concepts theoretically.
 
The programs and examples in this repository demonstrate my practice with:
 
- Python syntax
- Programming logic
- Problem solving
- Data structures and collections
- Functions
- File handling
- Modules and packages
- Exception handling
- Data processing
- Basic project development
 
As I continue learning Python, this repository will continue to grow with new concepts, exercises, and projects.
 
---
 
## 🎯 Learning Goals
 
The main goals of this repository are to:
 
- Build strong Python programming fundamentals
- Improve programming logic and problem-solving skills
- Understand Python syntax and core concepts
- Practice writing reusable and readable code
- Understand Python collections and data handling
- Learn file and data processing
- Understand modules and packages
- Practice exception handling
- Develop small Python projects
- Build a consistent programming portfolio
- Prepare for advanced Python programming
- Eventually apply Python to Data Structures and Algorithms, automation, data analysis, and software development
 
---
 
# 🧠 Topics Covered
 
## 1. Python Basics
 
Programs and examples covering the fundamental structure of Python programs.
 
Topics include:
 
- Python syntax
- Comments
- Printing output
- Variables
- Basic expressions
- User input
- Basic program structure
 
Example:
 
```python
name = input("Enter your name: ")
print("Hello", name)
```

## 2. Data Types

Practice with Python's fundamental data types.

Topics include:

- Integers
- Floating-point numbers
- Strings
- Boolean values
- Type conversion
- Type checking

### Example

```python
age = 20
height = 5.8
name = "Mahesh"
is_student = True
```
---

## 3. Numbers

Programs demonstrating operations and concepts related to numerical values.

Topics include:

- Integers
- Floating-point numbers
- Arithmetic operators
- Numerical expressions
- Mathematical calculations
- Basic numerical operations

### Example

```python
a = 10
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
```
## 4. Conditional Statements

Programs demonstrating decision-making and logical conditions in Python.

Conditional statements allow a program to execute different blocks of code depending on whether a condition is true or false.

Topics include:

- if
- if-else
- elif
- Nested conditions
- Comparison operators
- Logical operators
- Multiple conditions
- Decision-making
### Example
```
marks = 75

if marks >= 50:
    print("Pass")
else:
    print("Fail")
```
### Multiple Conditions
```
marks = 85

if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
else:
    print("Needs Improvement")

print(type(age))
print(type(height))
print(type(name))

print(type(is_student))
```

## 5. Loops

Programs demonstrating repetition and iteration in Python.

Loops are used to execute a block of code repeatedly until a particular condition is satisfied.

Topics include:

- for loops
- while loops
- Iteration
- range()
- Nested loops
- Loop conditions
- break
- continue
- Repeated execution
### for Loop Example
```
for number in range(1, 6):
    print(number)
```
### while Loop Example
```
number = 1

while number <= 5:
    print(number)
    number += 1
```
### Loop Control Example
```
for number in range(1, 11):

    if number == 5:
        break

    print(number)
```

## 6. Strings

Programs and examples for working with text data in Python.

Strings are sequences of characters used to represent text.

Topics include:

- Creating strings
- String indexing
- String slicing
- String concatenation
- String repetition
- String comparison
- String formatting
- String operations
### Example
```
name = "Python"

print(name[0])
print(name[1])
print(name[1:4])
```
### String Concatenation
```
first_name = "Mahesh"
last_name = "Kumar"

full_name = first_name + " " + last_name

print(full_name)
```

### String Formatting
```
name = "Mahesh"
age = 20

print(f"My name is {name} and I am {age} years old.")
```

## 7. String Methods

Programs demonstrating Python's built-in methods for manipulating and working with strings.

String methods provide useful operations for modifying, searching, checking, and processing text.

Topics include:

- upper()
- lower()
- capitalize()
- title()
- strip()
- replace()
- split()
- join()
- find()
- count()
- startswith()
- endswith()
- String checking methods
### Example
```
text = "hello python"

print(text.upper())
print(text.lower())
print(text.title())
```
### Replacing Text
```
text = "I am learning Java"

new_text = text.replace("Java", "Python")

print(new_text)
```
### Splitting Text
```
text = "Python is easy to learn"

words = text.split()

print(words)
```
