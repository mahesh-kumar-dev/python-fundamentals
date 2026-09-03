# LIST IN PYTHON: 
# list is a collection that can hold multiple items in a single variable. 

# list can hold different types
mixed = ['Alice', 23, 3.142,True]
print(mixed)

'''
    Store multiple items -> All your groceries, all student names
	Keep things in order -> First place, second place, third place
	Change items -> Update, add, remove
	Loop through items -> Process each item one by one
'''

# CREATING LIST

# empty list
empty1 = []
empty2 = list()

print(empty1)
print(empty2)

# list with items
# String
fruits = ["apple", "banana","cherry"]
print(fruits)

# Numbers
scores = [98,89,67,78,50]
print(scores)

# List inside list
matrix = [[1,2],[3,4],[5,6]]
print(matrix)


# List with Repeated Values
zeros = [0]*3
print(zeros)

repeated = ["hi"]*3
print(repeated)


# ACCESSING LIST
# indexing (like strings)

# Positive indexes (0-length-1)
print(fruits[0])
print(fruits[1])
print(fruits[2])

# Negative indexes from end
print(fruits[-1])
print(fruits[-2])
print(fruits[-3])


# SLICING LIST
num = [0,1,2,3,4,5,6,7,8,9]
# Get items from 2 to 5
print(num[2:6])

# First 3 items
print(num[:3])

# last 3 items
print(num[-3:])

# All items (copy)
print(num[:])

# Every second item
print(num[::2])

# Reverse Items
print(num[::-1])


# LIST OPERATIONS
# getting list length
print(len(fruits))
print(len(empty1))

# Check id item exits
fruits = ["apple", "banana","cherry"]
print("banana" in fruits)
print("grape" in fruits)

# checking before accessing
if "grape" in fruits:
    print(fruits.index("grape"))
else: 
    print("Grape not found.")


# Combining list
list1 = [1,2,3]
list2 = [4,5,6]
combined = list1 + list2
print("List 1: ", list1)
print("List 2:", list2)
print("Resultant: ",combined)

list1.extend(list2)
print("Now list 1: ", list1)

#  ADDING ITEMS TO LIST
# append() – Add ONE item to the end
fruit = ["orange", "mango"]
fruit.append("grape")
print(fruit)

# Append adds whole item (doesn't unpack)
fruit.append(["dates", "elderberry"])
print(fruit)


# insert() – Add item at specific position
vegetables = ["potato", "carrot"]
vegetables.insert(0,"broccoli")
print(vegetables)

# extend() – Add MULTIPLE items to the end
students = ["Ali","Hussain","Danish"]
students.extend(["Saud","Prem"])
print(students)


# REMOVING ITEMS FROM LIST
# remove() – Remove by VALUE (first occurrence)
products = ["keyboard","Mouse","Joystick","Mouse"]
products.remove("keyboard")
print(products)

# pop() – Remove by INDEX (returns removed item)
# remove last item (default)
last = products.pop()
print(last)

# remove at specific index
second = products.pop(1)
print(second)

# clear() – Remove ALL items

products.clear()
print(products)

# del – Delete by index or slice
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# Delete one item
del fruits[1]
print(fruits)

# Delete slice
del fruits[1:2]
print(fruits)

# Delete entire list
del fruits


# FINDING ITEMS IN THE LIST
# index() – Find position of value
animals = ["buffalo","cow","goat","horse","cow"]
cow_pos= animals.index("cow")
print(cow_pos)

# Find with start position
cow_pos = animals.index("cow",2)
print(cow_pos)

# count() – Count occurrences
count_cows = animals.count("cow")
print(count_cows)

count_buff = animals.count("buffalo")
print(count_buff)

# SORTING AND REVERSING 
# sort() – Sort list (modifies original)
numbers = [3,0,1,4,9,2,5,7]
numbers.sort()
print(numbers)

# Reverse Order
numbers.sort(reverse=True)
print(numbers)

# Sort by alphabetically
words = ["hi", "alas","Sorrow","belligerent"]
words.sort()
print(words) # Upper case first

words.sort(key=str.lower)
print(words)

# reverse() – Reverse list (modifies original)
words.reverse()
print(words)

# sorted() – Return new sorted list (original unchanged)
number = [3,1,4,9,6]
sorted_num = sorted(number)
print(sorted_num)
print(number) # unchanged

# descending
sorted_des = sorted(number,reverse=True)
print(sorted_des)

# COPYING LIST
# copy() – Shallow copy
original = [1,2,3]
copied = original.copy()

copied[0] = 99
print(original)
print(copied)

copy2 = original[:]
copy3 = list(original)


# LOOPING THROUGH LIST
# for loop
names = ["Mahi", "Assu","saku","Nami"]
for nm in names:
    print(nm)

# Loop with index
for i in range(len(names)):
    print(f"{i}: {names[i]}")

# Using enumerate
for i, name in enumerate(names):
    print(f"{i}: {names[i]}")


# LIST COMPREHENSION (CREATING LIST FROM LOOPS)
sqr = []
for i in range(5):
    sqr.append(i**2)
print(sqr)

# List comprehension (shorter, faster)
sqr = [i ** 2 for i in range(5)]
print(sqr)  

# With condition 
even = [i for i in range(10) if i%2 ==0]
print(even)

doubled = [i*2 for i in [1,2,3]]
print(doubled)

lis = list(range(6))
print(lis)

# Largest in list
numbers = [2,4,7,9,2,1,5,6,4]
largest = numbers[0]
for n in numbers:
    if n>largest:
        largest = n
print(f"Largest in list: {largest}")


# Remove dublicates
items = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique = []
for item in items:
    if item not in unique:
        unique.append(item)
print(unique)




# Practice Questions

# To Do List
tasks = []

while True:
    print("\n------To Do List------")
    print("1. Add Task")
    print("2. View Task")
    print("3. Remove Task")
    print("4. Quit")

    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print(f"Added: {task}")
    elif choice == "2":
        if not tasks:
            print("No Task.")
        else:
            for i,task in enumerate(tasks,i):
                print(f"{i}: {task}")
    elif choice == "3":
        if not tasks:
            print("No task to remove.")
        else:
            num = int(input("Task number to remove: "))
            removed = tasks.pop(num - 1)
            print(f"Removed: {removed}")
    elif choice == "4":
        break


# Grade Calculator
grades = []

while True:
    grade = input("Enter grade: (or done to finish it.)")
    if grade.lower() == "done":
        break
    else:
        grades.append(float(grade))

# Calculate Statistics
if grades:
    average = sum(grades)/len(grades)
    highest = max(grades)
    lowest = min(grades)

    print("\n----Grade Report----")
    print(f"Number of grades: {grades}")
    print(f"Average: {average}")
    print(f"Maximum: {highest}")
    print(f"Minimum: {lowest}")

    # for sorted display
    grades.sort()
    print(f"Sorted display: {grades}")
else:
    print("No grades entered.")


# Number Filter
numbers = [1,2,3,4,5,6,7,8,9]
evens = [n for n in numbers if n%2 == 0]
print(f"Even numbers: {evens}")

# filter number greater than 6
big_num = [n for n in numbers if n > 6]
print(f"Greater than 6: {big_num}")

# Double the number
double = [n*2 for n in numbers ]
print(f"Doubled: {double}")

# Square all the number
square = [n**2 for n in numbers]
print(f"Squares: {square}")

