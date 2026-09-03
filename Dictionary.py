# Python Dictionary 
# Dictionary is a collection of key-value pairs.
'''
    Use dictionaries for: 
    Storing related data about an item, 
    fast lookups by name/id, 
    configuration settings, counting occurrences.
'''
# CREATING DICTIONARY
# empty dictionary
empty = {}
print(type(empty))

# dictionary with data
person = {
    "name":"Mahesh Kumar",
    "age": 20,
    "city": "Karachi"
}
print(person)

# Dictionary with different types
mixed = {
    "name":"Asma",
    "score":98,
    "is_active":True,
    "grades":[85,89,90]
}
print(mixed)

# Using dict() Constructor
# From keyboard arguments
person = dict(name="Saud",age=23,city="Ghotki")
print(person)

# From list of tuples
pairs = [("name","Jai Kumar"),("age",16),("city","ghotki")]
person = dict(pairs)
print(person)

# Empty dictionary 
empty = dict()
print(empty)

# Dictionary Comprehension
# Create dictionary with squares 
squares = {x:x**2 for x in range(10)}
print(squares)

# With conditions 
even_squares = {x:x**2 for x in range(20) if x%2 == 0}
print(even_squares)


# ACCESSING DICTIONARY ITEMS
# Access by Key (Using [])
student = {"name":"Payal","age":19,"city": "sukkur"}
print(student["name"])
print(student["age"])
print(student["city"])

# Accessing missing element cause errors

# Access by Key (Using get() – Safe!)
animal = {"name": "Dog","age": 7}
# Safe access - return None if key missing 
print(animal.get("name"))
print(animal.get("age"))

# With default values
print(animal.get("breed","labardor"))
print(animal.get("age",0))

# Get all Keys
footballer = {"name":"Lionel Messi","age":41,"city":"Argentina"}
key = footballer.keys()
print(key)
print(list(key))

# Get all Values
value = footballer.values()
print(value)
print(list(value))

# Get all key: value pairs
item = footballer.items()
print(item)
print(list(item))


# ADDING AND CHANGING ITEMS
# Adding new items
cricketer = {"name":"Vaibhav Sooryavanshi","age":15}

# Add new key:value pair
cricketer["city"] = "Bihar"
print(cricketer)

# Add another
cricketer["country"] = "India"
print(cricketer)


# Changing Existing Items
actress = {"name":"Alice","age":25,"city":"New York"}

# Change Value
actress["name"] = "Alicent"
print(actress)

# Change another
actress["city"] = "Boston"
print(actress)


# Using update() – Add/Update Multiple Items
adult = {"name":"Ashok","age":34}

# Update with another dictionary 
adult.update({"city":"Ghotki","age":24})
print(adult)

# Update with keyboard arguments
adult.update(country= "Pakistan",zip="65110")
print(adult)


# Using setdefault() – Add Only If Key Missing
hacker = {"name":"Varun","age":19}

# If key exist return value and does nothing
result = hacker.setdefault("age",99)
print(result)
print(hacker)

# If key missing adds it and return new values
result = hacker.setdefault("city","Mirpur")
print(result)
print(hacker)


# REMOVING ITEMS
# pop() – Remove by key and return value
baby = {"name":"Hritik","age":4,"city":"Pano Aqil"}

# remove existing key
name = baby.pop("name")
print(name)
print(baby)

# remove with default (no error)
country = baby.pop("country","Not Found")
print(country)
print(baby)

# popitem() – Remove and return last item (Python 3.7+)
key,value = baby.popitem()
print(f"Removed: {key} = {value}")


# del – Delete by key
del baby["age"]
print(baby)

# delete the key that doesnot exits cause an error

# clear() – Remove all items
baby.clear()
print(baby)


# LOOPING THROUGH DICTIONARY
# loop through keys
actor = {"name":"Jon Snow","age":26,"city":"Moscow"}

# Method 1:  Direct Iteration (default key)
for key in actor:
    print(key)

# Method 2: Using keys()
for key in actor.keys():
    print(key)

# Loop Through Values

for value in actor.values():
    print(value)


# Loop through key-value pair
for key,item in actor.items():
    print(f"{key}: {item}")


# CHECKING EXISTENCE
# Check if Key exist
toys = {"toy":"Race Car","size":"Medium"}

print("toy" in toys)
print("size" in toys)
print("color" in toys)

# Check if Values exist
print("Race Car" in toys)
print("Medium" in toys)
print("Blue" in toys)


# NESTED DICTIONARY
user = {
    "asma":{
        "age":19,
        "email":"asmak781@gmail.com",
        "city":"thatta"        
    },
    "mahi":{
        "age":20,
        "email":"mahesh709@gmail.com",
        "city":"Daharki"
    }
}

# Access nested values
print(user["asma"]["email"])
print(user["mahi"]["city"])

# Modify nested values
user["mahi"]["city"] = "Hyderabad"
print(user["mahi"]["city"])

# Add to nested dictionary 
user["mahi"]["phone"] = "555-2311"
print(user["mahi"])

# Looping through nested dictionary 
users = {
    "hari":{
        "age":35,
        "city":"ghotki"
    },
    "shiv":{
        "age":23,
        "city":"sukkur"
    },
    "dheeraj":{
        "age":22,
        "city":"Rahim yar khan"
    }
}

for username, info in users.items():
    print(f"\nUser: {username}")
    print(f" Age: {info["age"]}")
    print(f" City: {info["city"]}")


# DICTIONARY OPERATIONS
# Getting length
female = {"name":"Alicent","age":23,"city":"london"}
print(len(female))

# Copying dictionary
original = {"name":"Nevand","age":47}

# Shallow copy
copied = original.copy()

copied["age"] = 30
print(original)
print(copied)

# Assignment doesnot copy 
copy2  = original
copy2["age"] = 23
print(original)


# Merging Dictionary
dict1 = {"a":1,"b":2}
dict2 = {"c":3,"d":4}

# Using operator |
merged = dict1 | dict2
print(merged)

# dict2 overwrite dict1 for same keys
dict1 = {"a":1, "b":2}
dict2 = {"b":99 ,"c":3}
merged = dict1 | dict2
print(merged)

# For older python 
merged = {**dict1 , **dict2}
print(merged)


# DICTIONARY VIEW (DYNAMIC)
# Dictionary views (keys(), values(), items()) are dynamic 
# – they update when the dictionary changes
driver = {"name":"Ramu Kaka","age":78}
key = driver.keys()
value = driver.values()

print(list(key))
print(list(value))

# add new items
driver["Car"] = "Civic"

# View automatically update
print(list(key))
print(list(value))



# Practice Questions
# Student GradeBook

# Gradebook dictionary
gradebook = {
    "Jon":[87,77,94],
    "Bob":[88,67,72],
    "Alice":[60,74,81]
}

# Add new student
gradebook["Diana"] =[82,80,99]

# Calculate average
for student, grades in gradebook.items():
    average = sum(grades)/len(grades)
    print(f"{student} : {average:.1f}")

# Find Top Student
top_student = None
top_avg = 0
for student, grades in gradebook.items():
    avg = sum(grades)/len(grades)
    if avg > top_avg:
        top_avg = avg
        top_student = student

print(f"\nTop Student: {top_student} :{top_avg:.1f}")


# Word Counter
# Count how many times each word appears
sentence = "the quick brown fox jumps over a lazy dog."
words = sentence.split()

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] +=1
    else:
        word_count[word] = 1
print("Word counts: ")
for word, counts in word_count.items():
    print(f" {word}: {counts}")

# Using get()  (shorter version)
word_count = {}
for word in words:
    word_count[word] = word_count.get(word,0)+1



# PhoneBook
phone_book = {}
while True:
    print("\n-------Phone Book-------")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. List all Contact")
    print("5. Quit")


    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        phone_book[name] = phone
        print(f"Added: {name}")
    elif choice == "2":
        name = input("Name to search: ")
        if name in phone_book:
            print(f"{name}: {phone_book[name]}")
        else:
            print("Not found.")

    elif choice == "3":
        name = input("Name to delete: ")
        if name in phone_book:
            del phone_book[name]
            print(f"Deleted: {name}")
        else:
            print("Not found.")
    elif choice == "4":
        if not phone_book:
            print("No Contact")
        else:
            for name,phone in phone_book.items():
                print(f"{name} : {phone}")
    elif choice == "5":
        break




# Character Frequency
# count frequency of each character in string 
text = input("Enter text: ").lower()
char_count = {}
for char in text:
    if char.isalpha():
        char_count[char] = char_count.get(char,0)+ 1    

# Display sorted by frequency
for char, count in sorted(char_count.items(),  key= lambda x:x[1], reverse= True):
    print(f" {char}: {count}")