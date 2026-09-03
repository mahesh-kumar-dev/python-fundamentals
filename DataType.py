# Data Types
# Data type tells Python what kind of information a variable holds
print("------Integer DataType-----")
age = 24
temperature = -5
score = 78
population = 100000
print("Score: ", score)
print("Population: ", population)
print(type(population))

a = 10
b = 3
print("a: ", a , "b: ",b)
print("a + b = ", a+b)
print("a - b = ", a-b)
print("a * b = ", a*b)
print("a / b = ", a/b) # float division 
print("a // b = ", a//b) # integer division (floor division - drop decimal)
print("a mod b = ", a%b) 
print("a ** b = ", a**b)


print("\n-----Float DataType-----")
price = 19.99
pi = 3.142
temp = 98.6
negative_float = -0.5
print("Temperature: ", temp)
print(type(temp))

x = 3.5
y = 2.0 
print("x = ", x , "     ", "y = ", y)
print("x + y = ", x+y)
print("x - y = ", x-y )
print("x * y = ", x*y )
print("x / y = ", x/y)
print("x // y = ", x//y) # floor divsion still float 

print("\n----String DataType----")
name = "Mahesh Kumar"
message =  "Hello Dear, "
empty_string = ""
multiline = """This is
a multi-line
string"""

print(multiline)
print(type(name))


# Both work the same
single_quotes = 'Hello'
double_quotes = "Hello"

# Choose based on what's inside
message1 = "It's a nice day"     # Double quotes allow apostrophe
message2 = 'He said "Hello"'     # Single quotes allow double quotes
message3 = 'It\'s a nice day'    # Or use backslash to escape

print(message1)
print(message2)
print(message3)

print("\nString operations: ")
first_name = "Mahesh"
last_name = "Kumar"
full_name = first_name + " " + last_name
print("First Name: ", first_name)
print("Last Name: ", last_name )
print("Full Name: ", full_name)

# Repeat String 
laugh = "Ha"*3
print(laugh)

name = "Python"
print("Python length: ", len(name))

word = "Hello"
print(word)
print(word[0]) # fist character
print(word[1]) # second last
print(word[-1]) #last character

msg = "Age: " + str(24)
print(msg)

print("\n-----Boolean DataType-----")
is_student = True
is_graduate = False
is_active = True
print("Is Student: ", is_student)
print(type(is_active))

# booleans uses for comparison 
c = 10 
d = 20
print(c > d)
print(c < d)
print(c == d)
print(c != d)

age1 = 18 
can_vote = age>=18
print("Can Vote: ", can_vote)

# boolean is conditionals
is_raining = True
if is_raining: 
    print("Take Umbrella. It\'s raining outside.")
else: 
    print("Enjoy the sun!")

if 42:
    print("42 is True")     # This prints

if 0:
    print("0 is True")      # This does NOT print

if "Hello":
    print("Text is True")   # This prints

if "":
    print("Empty is True")  # This does NOT print

print("\n-----None DataType-----")
result = None
print(result)
print(type(result))

value = None 

if value is None:
    print("No value present")
else: 
    print("Value is: ", value)

print("\n----Type Conversion----")
# convert to Integer
print(int("123"))
print(int(3.23))
print(int(True))

# convert to float 
print(float(5))
print(float("3.123"))

# convert to string 
print(str(34))
print(str(3.34))
print(str(True))

# convert to boolean 
print(bool(0))
print(bool(5))
print(bool(""))
print(bool("Hello"))
print(bool(None))

print("\n---User Input-----")
#input() always returns a string:
age = input("Enter your age: ")
print("Your age: ",age)
print(type(age))

age_number = int(age)
next_age = age_number + 1
print("Next year, you\'ll be: ", next_age)

print(isinstance(x,int))
print(isinstance(c,int ))

print("\n-----Practice-----")
name1 = input("What\'s your name? ")
age1 = input("How old you are? ")
age_num = int(age1)
nxt_age = age_num + 1
is_adult = age_num >= 18
msg1 = "Hello "+ name1 + "! You are " + age1 + " year old."
msg2 = "Next year you\'ll be "+ str(nxt_age)+ "."
msg3 = "Adult: "+ str(is_adult)
print(msg1)
print(msg2)
print(msg3)