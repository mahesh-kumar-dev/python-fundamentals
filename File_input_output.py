# File Input Output -> Reading & Writing Files
# File I/O (Input/Output) is how programs read from and write
# to files on your computer. 

# Real-life example: A text editor saves your document to a file. 
# When you open it again, it reads from that file.

'''
    Features:
	Save data permanently -> Data stays after program ends
	Load configuration -> Read settings from files
	Process large data -> Read files line by line
	Share data -> Export/import data between programs
	Log information -> Save error messages and activity
'''

# OPENING FILE
# The open() Function
# Opening a file for reading ("r" mode)

file = open("data.txt","r")
content = file.read()
print(content)
file.close()

'''
File Modes
Mode	 Description	        File exists?	    File missing?
"r"	     Read (default)	        Opens	            Error
"w"	     Write (overwrites)	    Overwrites	        Creates
"a"	     Append (add to end)    Adds to end	        Creates
"x"      Exclusive creation	    Error	            Creates
"r+"	 Read and write	        Opens	            Error
"w+"     Write and read	        Overwrites	        Creates
'''

# Read mode (file must exists)
file = open("existing.txt","r")
print("\n\n",file.read())
file.close()

# Write mode (created or overwrite)
file = open("new.txt","w")
file.write("Welcome to Python File handling.\n")
file.write("Here, you can read, write, append, overwrite.")
file.close()


# Append mode (adds to end of the file)
''' 
file = open("log.txt","a")
file.write("It means whenever you write it would be appended at the end in the file.")
file.close()
'''

# The 'with' statement
# The with statement automatically closes the file for you.

# Without 'with' ( needs to close the file manually )
file = open("metaphysics.txt","r")
text = file.read()
print("\n\n",text)
file.close()

# With 'with' (auto-closes)
with open("new.txt","w") as file:
    file.write("with statement is used to auto-closes the file.")
    


# READING FILES
# read() -> read entire file
with open("new.txt","r") as file :
    print("\n\n", file.read())


# readline() – Read One Line at a Time
with open("metaphysics.txt","r") as file:
    line1 = file.readline()
    line2 = file.readline()

    print(f"Line 1: {line1}")
    print(f"Line 2: {line2}")


# readlines() – Read All Lines as List
with open("log.txt","r") as file:
    lines = file.readlines()
    print(lines)


# Looping through lines (Most common)
# Best way to read file (memory efficient)
with open("new.txt","r") as file:
    for lines in file:
        print(lines.strip())


# Reading  mode examples

# Method 1: read()
with open("log.txt","r") as f:
    print("\n\n",f.read())

# Method 2: readlines()
with open("log.txt","r") as f:
    fruits = f.readlines()
    for fruit in fruits:
        print(fruit.strip())

# Method 3: Loop through file (best for large files)
with open("log.txt","r") as f:
    for fruit in f:
        print(fruit.strip())

# WRITING FILES
# w" : Erases the whiteboard completely and starts writing from line 1.
# write() – Write String to File

# Write a single string
with open("demo.txt","w") as file:
    file.write("This is Write mode of File Handling.")

# Write with multiple strings
with open("demo.txt","w") as file:
    file.write("Through write mode we can write single string.\n")
    file.write("Write mode enable multiple strings.\n")

    
# writelines() – Write List of Strings
lines = ["Fruits List:\n","Apple\n","Banana\n","Cherry\n"]
with open("demo.txt","w") as file:
    file.writelines(lines)

# Write vs Append
# Write mode ("w") - overwrite entire file
line = ["Name:\t","Mahesh\t","Kumar"]
with open("demo.txt","w") as file:
    file.writelines(line)

# Append mode ("a"): adds to end of the file
with open("demo.txt","a") as f:
    f.write("\nThis is Programming world.\n")
    f.write("Here you will learn best ever Python fundamental content.")


# COMMON FILE OPERATIONS
# Checking if file exists
import os

if os.path.exists("demo.txt"):
    print("File Exists.")
else:
    print("File not found.")

# Checks if it's a file (not directory)
if os.path.isfile("new.txt"):
    print("It's File.")
else:
    print("Not a file")

# Check if it's directory
if os.path.isdir("module"):
    print("Its directory")
else:
    print("Not a directory.")


# Getting file information
import os
import time

# Get file size
size = os.path.getsize("metaphysics.txt")
print(f"Size: {size} bytes")

# Get last modified time
modified = os.path.getmtime("metaphysics.txt")
print(f"Last Modified: {time.ctime(modified)}")


# Creating Directories 

# Create a single directory
# os.mkdir("new_folder")

# Get nested directories
os.makedirs("parent/child/grandchild",exist_ok=True)

# Create a file

# Define your file path
file_path = r"new_file.txt"

# Flags explained:
# os.O_CREAT -> Creates the file if it does not exist
# os.O_WRONLY -> Opens the file in Write-Only mode
flags = os.O_CREAT | os.O_WRONLY

# Open the file descriptor (low-level file reference)
file_descriptor = os.open(file_path, flags)

# Convert the string content into raw bytes
content = "This file was created using the os module.".encode()

# Write the bytes to the file descriptor
os.write(file_descriptor, content)

# Always close the file descriptor when finished
os.close(file_descriptor)

print("File created successfully using OS module!")


# Check if directory exists
# if os.path.exists("new_folder"):
#    print("Folder exist.")


# Deleting files and directories
if os.path.exists("delete.txt"):
    os.remove("delete.txt")

# Delete empty directory
# os.rmdir("new_folder")

# Delete directory and all content
import shutil
shutil.rmtree("parent/child/grandchild")


# Working with different File types

# Text Files (.txt)
# Writing text files
with open("notes.txt","w") as f:
    f.write("1.Learning Basic Python.")
    f.write("2.Learning Intermediate Python")

# Reading Text files
with open("notes.txt", "r") as f:
    for line in f:
        print(line.strip())



# CSV Files (Comma Separated Values)
import csv

# Writing csv
data = [
    ["Name","Age","City"],
    ["Sitara", 21,"Naushero"],
    ["Mahesh", 20,"Ghotki"],
    ["Vijay", 21, "Umerkot"]
]

with open("person.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Reading CSV
with open("person.csv","r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)



# JSON Files (JavaScript Object Notation)
import json

# Data to save
person = {
    "name":"Mahesh Kumar",
    "age": 20,
    "city": "Ghotki",
    "hobbies":["reading","gossiping","playing games","dancing"],
    "languages": ["English","Urdu","Sindhi","Marwari"]
}


# Writing JSON
with open("myself.json","w") as f:
    json.dump(person,f,indent=2)

# Reading JSON
with open("myself.json","r") as f:
    loaded = json.load(f)
    print(f"Name: ,{loaded["name"]}")
    print(f"Age: {loaded["age"]}")
    print(f"City: {loaded["city"]}")
    print(f"Hobbies: {',  '.join(loaded["hobbies"])}")
    print(f"Languages: {',  '.join(loaded["languages"])}")
    
# Exceptional Handling with file

# Handling file ERRORS
try:
    with open("new.txt","r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("File NOT found.")
except FileExistsError:
    print("File doesn't Exist.")
except PermissionError:
    print("Don't have permission to read this.")
except Exception as e:
    print(f"An error occured: {e}")


# Safe file operation
def safe_read(filename):
    """Read File safely, return None if error"""
    try:
        with open("log.txt","r") as f:
            return f.read()
    except FileExistsError:
        print(f"File {filename} doesn't Exist.")
        return None
    except FileNotFoundError:
        print(f"File {filename} NOT found.")
        return None
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return None

def safe_write(filename, content):
    """Write File safely"""
    try:
        with open("log.txt","w") as f:
            f.write(content)
            return True
    except Exception as e:
        print(f"Error writing to {filename}: {e}")
        return False

print("Reading File: ",safe_read("demo.txt"))
print(safe_write("demo.txt","Now Iam able to easily write something in the file."))


# Practice Questions
# TO DO LIST  with file Storage
import os

todo_file = "task.txt"

def load_task():
    """Load the task from file"""
    tasks = []
    if os.path.exists(todo_file):
        with open(todo_file,"r") as f:
            for line in f:
                tasks.append(line.strip())
    return tasks

def save_task(tasks):
    """Save Tasks to file"""
    with open(todo_file,"w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_task(tasks):
    """Display All the Tasks"""
    if not tasks:
        print("No tasks")
    else:
        for i, task in enumerate(tasks,1):
            print(f"{i}: {task}")

# Main pg
tasks = load_task()

while True:
    print("\n------TO DO LIST--------")
    print("1. View Task")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Quit")

    choice = input("Choose: ")

    if choice == "1":
        show_task(tasks)
    elif choice == "2":
        task = input("Enter Task: ")
        tasks.append(task)
        save_task(tasks)
        print("Task Added.")
    elif choice == "3":
        show_task(tasks)
        if tasks:
            num = int(input("Task number to remove: "))
            removed = tasks.pop(num - 1)
            save_task(tasks)
            print(f"Removed: {removed}")
    elif choice == "4":
        print("Thanks For Your Time 😊")
        break


# Contact Book with CSV 
import csv
import os

contact_file = "contacts.csv"

def load_contacts():
    """Load Contacts from CSV"""
    contacts = []
    if os.path.exists(contact_file):
        with open(contact_file,"r") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if row:
                    contacts.append({"first_name": row[0], "last_name": row[1],
                    "phone_number":row[2], "email":row[3]})
    return contacts

def save_contact(contacts):
    """Save Contacts to CSV file"""
    with open(contact_file,"w",newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["First Name","Last Name","Phone Number","Email"])
        for contact in contacts:
            writer.writerow([contact["first_name"], contact["last_name"],
            contact["phone_number"],contact["email"]])


def add_contact(contacts):
    """Add a new Contact"""
    f_name = input("First Name: ")
    l_name = input("Last Name: ")
    p_number = input("Phone Number: ")
    email = input("Email: ")
    contacts.append({"first_name": f_name , "last_name": l_name ,
    "phone_number":p_number , "email":email})
    save_contact(contacts)
    print("Contact Added!")

def search_contact(contacts):
    """Search for Contact"""
    search = input("Enter search contact: ").lower()
    found = [c for c in contacts if search in c["first_name"].lower()
    or search in  c["last_name"].lower()]
    if found:
        print("\nFound:")
        for contact in found:
            print(f" First Name: {contact['first_name']}")
            print(f" Last Name: {contact['last_name']}")
            print(f" Phone Number: {contact['phone_number']}")
            print(f" Email: {contact['email']}")
    else:
        print("No Contact Found!")

def list_contact(contacts):
    """List All Contacts"""
    if not contacts:
        print("No Contacts!")
    else:
        print("\nAll Contacts: ")
        for i, contact in enumerate(contacts,1):
            print(f"{i}. {contact['first_name']} - {contact['last_name']} - {contact['phone_number']}")

# Main program : Working
contacts = load_contacts()

while True:
    print("\n-------Contact Book------")
    print("1. List Contacts")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Quit")

    choice = input("Choice: ")

    if choice == "1":
        list_contact(contacts)
    elif choice == "2":
        add_contact(contacts)
    elif choice == "3":
        search_contact(contacts)
    elif choice == "4":
        print("Thanks For Using my Service 😊")
        break



# LOG FILE WRITER

import datetime

def write_log(message, level="INFO"):
    """Write a message To Log File"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("app.log","a") as f:
        f.write(f"[{timestamp}] [{level}] {message}\n")

def read_log():
    """Read and Display  the log file"""
    try:
        with open("app.log","r") as f:
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print("No log file found.")

def clear_log():
    """Clear the log file"""
    with open("app.log","w") as f:
        f.write()
    print("Log Cleared!")


# Main Execution
write_log("Application started.")
write_log("User logged in", " INFO")
write_log("Database connection failed","ERROR")
write_log("Retrying connection","WARNING")
write_log("Application shutting down","INFO")

print("------LOG CONTENT-----")
read_log()



# WORD COUNTER FROM FILE
def count_word(filename):
    """Count words in Text File"""
    try:
        with open(filename,"r") as f:
            text = f.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        print(f"File {filename} NOT found.")
        return 0

def count_lines(filename):
    """Count lines in text file"""
    try:
        with open(filename,"r") as f:
            lines = f.readlines()
            return len(lines)

    except FileNotFoundError:
        print(f"File {filename} NOT found.")
        return 0

def analyze_file(filename):
    """Analyze text file"""
    try:
        with open(filename,"r") as f:
            content = f.read()

            chars = len(content)
            words = len(content.split())
            lines = content.count("\n") + 1

            print(f"File: {filename}")
            print(f"Characters: {chars}")
            print(f"Words: {words}")
            print(f"Lines: {lines}")
    except FileNotFoundError:
        print(f"File {filename} NOT found.")

analyze_file("metaphysics.txt")
word_count = count_word("metaphysics.txt")
line_count = count_lines("metaphysics.txt")

print("Word Count: ",word_count)
print("Line Count: ",line_count)

# Simple program
name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")

with open("user_info.txt","w") as f:
    f.write(f"Name: {name}")
    f.write(f"Age: {age}")
    f.write(f"City: {city}")
print("Saved to user_info successfully.....")



# Copy the file 
source = input("Source file: ")
destination = input("Destination file: ")

try:
    with open(source,"r") as s:
        content = s.read()
    with open(destination,"w") as dst:
        dst.write(content)
    
    print(f"Copied from {source} to {destination}")

except FileNotFoundError:
    print("Source file NOT found.")