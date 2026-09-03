# TUPLES IN PYTHON
#  tuple is like a list that cannot be changed
fruit_list = ["apple", "banana", "grape"]
print(f"Original List: {fruit_list}")
fruit_list[1] = "blueberry"
print(f"Modified List: {fruit_list}")

fruits_tuple = ("apple", "banana", "cherry")
# fruits_tuple[1] = "blueberry"  # ERROR! Cannot change tuple
print(fruits_tuple)
string = " | ".join(fruit_list)
print(string)

# Use tuples for: Days of week, months of year,
# coordinates, constant data that never changes.

# CREATING TUPLES
# basic tuple creation
colors = ("red","green","blue")
print(colors)

# Without parenthesis (tuple packing)
coordinates = 10,20,30
print(coordinates)
print(type(coordinates))

# empty and single-item tuples
empty = ()
print(empty)


# Single item tuple must have comma at the end
single = (4,)
print(single)
print(type(single))

# Without parentheses also needs comma
single1 = 3,
print(single1)
print(type(single1))

# Creating tuples from other type
# from list
my_list = [1,2,3]
my_tuple = tuple(my_list)
print(my_tuple)

# From string
char_tuple = tuple("Hi, Mahesh")
print(char_tuple)

# from range 
range_tuple = tuple(range(7))
print(range_tuple)


# ACCESSING TUPLE ITEMS
# Indexing same as List
colours = ("red","green", "brown","blue","white")

# Positive indexes
print(colours[0])
print(colours[1])
print(colours[2])
print(colours[3])
print(colours[4])

# Negative Indexes
print(colours[-1])
print(colours[-2])
print(colours[-3])
print(colours[-4])


# Slicing same as list
numbers = (0,1,2,3,4,5,6,7,8,9)

# get items from 2 to 5
print(numbers[2:6])

# get first 3 items
print(numbers[:3])

# get last 3 items
print(numbers[-3:])

# Every second item
print(numbers[::2])

# Reverse tuple
print(numbers[::-1])


# TUPLE UNPACKING
# assigning tuple values to multiple variables
person = ("Mahesh Kumar",20,"Karachi")
name,age,city = person
print(name)
print(age)
print(city)

# swap variables using tuple unpacking
a = 5
b = 12
print("a: ",a,"\tb: ",b)
a,b = b,a
print("a: ",a,"\tb: ",b)

# Unpacking with * (rest operator)
number =(1,2,3,4,5)
first , *rest = number
print(first)
print(rest)

first , second , *rest = number
print(first, second)
print(rest)


# TUPLE OPERATIONS
# getting length
mirrors = ("concave","convex","flat")
print(len(mirrors))

# Check if item exist
print("concave" in mirrors)
print("planoconcave" in mirrors)

# Combining tuples
tuple1 = (1,2,3)
tuple2 =(4,5,6)

# Use + to create new tuple
combined = tuple1 + tuple2
print(combined)

# use * operator to repeat
repeat = (1,2)*3
print(repeat)


# TUPLE METHODS
# .count() – Count occurrences
numbers = (1,2,3,2,4,5,2)
count_of_2 = numbers.count(2)
print("Count 2: ", count_of_2)

count_of_6 = numbers.count(6)
print("Count 6: ",count_of_6)

# index() – Find position of value
birds = ("parrot","peacock","sparrow","mockingbird", "parrot")
# first occurence
pos = birds.index("parrot")
print("Index of parrot: ",pos)

# find with start position
pos = birds.index("sparrow",1)
print("Sparrow index: ", pos)


# LOOPING THROUGH TUPLES
pents = ("cargo","chinos","skinny","baggy")

for pent in pents:
    print(pent)

for i,pent in enumerate(pents):
    print(f"{i}: {pent}")


# Tuple vs List
# Good for tuples (fixed data)
days_of_week = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday",  "Sunday")
months = ("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec")
seasons = ("Winter","Summer","Spring","Autumn")

# Good fro tuple (return multiple values)
def get_user():
    name = "Mahesh"
    age = 20
    city = "Karachi"
    return name,age,city 

user_info = get_user()
print("User Information: ", user_info)

# Good for Dictionary keys (List cannot be keys)
location = {(10,12):"Point A", (21,9):"Point B"} # Tuple as key
print(location[(10,12)])

# When To Use list
# Good for list (changing data)
shopping_cart = []
shopping_cart.append("Apple")
shopping_cart.append("banana")
print(shopping_cart)

# Good for list (Unknown size)
scores = []
while True:
    score = input("Enter score (or quit): ")
    if score == "quit":
        break
    scores.append(int(score))
print(scores)

# CONVERTING BETWEEN TUPLE AND LIST
# Tuple to List
laptop_tuple = ("Dell","HP","Lenovo")
laptop_list = list(laptop_tuple)
print(laptop_list)

# We can also modify it
laptop_list.append("Asus")
print(laptop_list)

# List To Tuple
organs_list = ["Liver","Brain","Lungs","Stomach"]
organs_tuple = tuple(organs_list)
print(organs_tuple)

# It cannot be modified now
# organs_tuple.append("spleen")  ! ERROR

# NAMED TUPLES
# Named Tuple gives names to each position, making code more readable.
from collections import namedtuple

# define named tuple type
Person = namedtuple("Person",["name","age","city"])

# Create instances
mahesh = Person(name="Mahesh",age=20,city="Karachi")
asma = Person("Asma","19","Thatta")

# Access by index
print(mahesh[0])
print(mahesh[1])

# Access by name
print(asma.name)
print(asma.age)
print(asma.city)

name,age,city = asma
print(name," ",age," ",city)

# mahesh.age=23 Still immutable

# Practice Questions
# Student Grade
# Each student is tuple (name,grade)
students = [
    ("Mahesh",89),
    ("Asma",98),
    ("Sitara",79),
    ("Sana",45),
    ("Aqsa",89)
    ]
# Calculate Average
total = 0

for name,grade in students:
    total +=grade
average = total/len(students)
print(f"Class Average: {average:.1f}")

# Find Top Student
top_student = max(students,key=lambda s:s[1])
print(f"Top Student: {top_student[0]} with {top_student[1]}")


# Find failing student
failing = [(name,grade) for name , grade in students if grade <80]
print(f"Failing: {failing}")


# Coordinate System (Tuples as points)
# points as tuple (x,y)
points = [
    (0,0),
    (1,9),
    (3,8),
    (7,13)
]

# Calculate distance from origin
import math
for x,y in points:
    distance = math.sqrt(x**2 + y**2)
    print(f"({x},{y}) -> distance: {distance:.1f}")

# Dictionary with tuple keys
locations = {
    (0, 0): "Home",
    (10, 20): "School",
    (30, 40): "Work"
}
print(locations[(10,20)])


# Multiple return values
def get_min_max(numbers):
    """Return both minimum and maximum as tuple"""
    return min(numbers),max(numbers)

scores = [85,87,60,70,90,56]

# Unpack the tuple
lowest, highest = get_min_max(scores)
print(f"Lowest: {lowest}, Highest: {highest}")

# Or keep it as tuple 
result = get_min_max(scores)
print(f"Range: {result[0]} to {result[1]}")