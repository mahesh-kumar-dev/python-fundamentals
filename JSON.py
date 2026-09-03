# Python JSON
# JSON (JavaScript Object Notation) is a text format for storing and exchanging 
# data. It's easy for humans to read and write, and easy for computers to parse.

'''
    Features:
	APIs -> Most web services send/receive data in JSON
	Configuration files -> Store settings in readable format
	Data exchange -> Share data between different programs
	Serialization -> Save Python objects to file and load later
	Lightweight -> Simpler and smaller than XML
'''

# JSON vs Python Types
'''
JSON	            Python

object	            dict
array	            list
string	            str
number (integer)	int
number (real)	    float
true	            True
false	            False
null	            None
'''

import json

# Python dictionary
python_data = {
    "name":"Mahesh",
    "age":20,
    "is_student":True,
    "scores":[99,92,87],
    "address":None
}

# Convert to JSON String
json_string = json.dumps(python_data)
print(json_string)


# Converting Python To JSON (Serialization)
# json.dumps() – Convert to String
import json

person = {
    "name":"Asma",
    "age":19,
    "city":"Thatta",
    "is_student":False,
    "hobbies":["reading","swimming","communication"],
    "address":{
        "street":"dr gali ward no 10",
        "zip":"66002"
    }

}

json_string = json.dumps(person)
print(json_string)



# Pretty Print (INDENTATION)
# With indentation (easy to use)
json_string = json.dumps(person, indent=2)
print(json_string)



# Other 'dumps' Operation
import json 

data = {"name":"Shafali Verma", "age":26}

# Sort keys alphabetically 
json_string = json.dumps(data, sort_keys=True , indent=2)
print(json_string)


# Remove whitespaces (smaller file size)
json_string = json.dumps(data, separators=(",",":"))
print(json_string)




# json.dump() – Write to File
import json

person = {
    "cricketer":"Virat Kohli",
    "age":37,
    "spouse": "Anushka Sharma",
    "childrens":3,
    "Ambassador": "MRF"

}

# Write into a file 
with open("myself.json","w") as f:
    json.dump(person,f,indent=2)

print("Saved to myself.json!!!!!!")



# Convert JSON to Python (Deserialization)

# json.loads() – Parse from String
import json

# JSON string
json_string = '{"name":"Anup", "age": 28, "city":"Mumbai"}'

# Convert to python Object
person = json.loads(json_string)

print(person["name"])
print(person["age"])
print(type(person))



# json.load() – Read from File
import json 

# Read from file
with open("myself.json","r") as f:
    person = json.load(f)

print(person)


# Parsing JSON array

import json 

# JSON array
json_array = '["Bumrah","Shami","Siraj"]'

# Convert to python List
bowlers = json.loads(json_array)
print(bowlers)
print(bowlers[0])
print(type(bowlers))



# Working with JSON Files
# Writing JSON Data

import json 

# Data to save
students = [
    {"name":"Payal","grade":87},
    {"name":"Rani","grade":75},
    {"name":"Renuka","grade":97},
]


# Save to file
with open("students.json","w") as f:
    json.dump(students,f,indent=2)

print("Saved to students.json")


# Reading JSON data
import json

# Read from file
with open("myself.json","r") as f:
    vk = json.load(f)

print(vk)

with open("students.json", "r") as f:
    students = json.load(f)

# Process the data
for student in students:
    print(f"{student["name"]} : {student["grade"]}")



# Appending to JSON file 
import json

def append_to_json(filename, new_data):
    """Append Data to json Array in file"""
    # Read Existing file
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            print(data)
    except FileNotFoundError:
        data = []


    # Append new data
    data.append(new_data)

    # Write back
    with open(filename, "w") as f:
        json.dump(data, f , indent=2)

# Usage 
append_to_json("students.json",{"name": "Urmila", "grade":77})




# Handling Complex Data Type
# These types CAN be converted to JSON:
# - dict, list, str, int, float, bool, None

# These types CANNOT be converted directly:
# - datetime, set, custom objects


# Custom Encoding (Convert non-JSON types)
import json
from datetime import datetime

