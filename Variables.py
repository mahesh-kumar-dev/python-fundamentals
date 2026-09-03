# Variables:  container to store data
# Python is dynamically Typed Language
name = "Mahesh Kumar"
age = 20
grade = 'A'
is_student = True

print("------Student Information------")
print("Name: ",name)
print("age: ", age)
print("Grade: ", grade)
print("Is Student: ", is_student)

price = 200
quantity = 3
total = price*quantity

print("\n----Shopping details----")
print("Shirt price: ",price)
print("Quantity: ", quantity)
print("Total Price: ", total)

# Multiple variables at Once
x = y = z = 6
print(x,y,z)

item, qty , type_ = "Keyboard", 3, "Gaming"
print("\n------Instruments Details-----")
print("Item: ", item)
print("Quantity: ", qty)
print("Type: ", type_)

print("\n-----Swapping Values----\n")
a = 5
b = 10
print("Before Swapping")
print("a: ", a,"     ", "b: ",b)
a , b = b, a
print("After Swapping")
print("a: ", a,"     ", "b: ",b)

print("----Dynamically Typed------ ")
val = 10
print("Value: ", val)
val = "Hello"
print("Value: ", val)
val = 3.14
print("Value: ", val)
val = True
print("Value: ", val)

print("\n----Checking Type----")
print("Type of name: ",type(name))
print("Type of age: ",type(age))
print("Type of grade: ",type(grade))
print("Type of is_student: ",type(is_student))
print("Type of price: ",type(price))

# Variable scope
# Global variable (outside any function)
message = "Hello"
def greet():
    # local variable (inside function)
    local_msg = "Hi"
    print(message)
    print(local_msg)

greet()
# We can't access local variable (local_msg)

# Deleting variable 
# del keyword is use to delete variable
variable = 10
print(variable)

del variable
# print(variable) # Error ! no longer exist now

a = 5
b = a      # b now points to same 5 as a
c = 5      # 5 is reused (small numbers are shared)

print(a is b)  # True (same object)
print(a is c)  # True (same object for small numbers)

print("\n-----Product Information-----")
# product information 
product_name = "Laptop"
price = 65000.89
qty1 = 3
tax_rate = 0.08

# calculate total 
subTotal = price * qty1
tax_amount = subTotal * tax_rate
total_price = subTotal + tax_amount

# display results
print("\n---- Display Information-----")
print("Product: ", product_name)
print("Quantity: ", qty1)
print("Subtotal $ : ", subTotal)
print("Tax $ : ", tax_amount)
print("Total Price $ : ", total_price)


# Variable Demo in single line

first_name = "Pardeep"
last_name = "Kumar"
age = 21
city = "Mithi"

print("\n\n",first_name, last_name, "is", age, "year old and lives in", city)


# Demo 
product = "Headphone"
price = 99.99
qty = 3
total_msg = product + " : $" + str(price * qty)
print("\n\n",total_msg)