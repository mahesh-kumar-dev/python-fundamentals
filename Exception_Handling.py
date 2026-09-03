# Python Exception Handling
# Exceptions are errors that occur when your program is running. 
# Exception handling allows your program to continue running instead of crashing.

'''
    Features:
	Prevent crashes - Keep program running when errors occur
	User-friendly messages - Show helpful error messages instead of technical gibberish
	Clean up resources - Close files/database connections even if errors happen
	Retry operations - Try again if something fails temporarily
	Log errors - Save error information for debugging
'''

# BASIC TRY-EXCEPT

# The 'try' and 'except'  Block
try:
    # Code that might cause error
    number = int(input("Enter a number: "))
    print(f"You have entered: {number}")
except ValueError:
    # Code that will run if ValuError occur
    print("That wasn't a valid number.")

print("Program continues........")

# Catching Specific Exceptions
try: 
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1/num2
    print(f"Result: {result}")
except ValueError:
    print("Please enter valid number")
except ZeroDivisionError:
    print("Cannot divided by zero.")


'''
Common Exception Types
Exception	        When it happens	            Example
ValueError	        Wrong value type	        int("hello")
ZeroDivisionError	Divide by zero	            10 / 0
TypeError	        Wrong operation type	    "5" + 5
IndexError	        List index out of range	    [1,2,3][10]
KeyError	        Dictionary key missing	    {"a":1}["b"]
FileNotFoundError	File doesn't exist	open    ("missing.txt")
NameError	        Variable not defined	    print(unknown_var)
AttributeError	    Object has no attribute	    "hello".unknown()

'''


# Examples of Different Exceptions
# ValueError
try:
    num = int("Hello")
    print(num)
except ValueError:
    print("Cannot convert 'Hello' to number.")


# ZeroDivisionError
try:
    result = 9/0
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero.")

# IndexError
try:
    my_list = [1,2,3]
    value = my_list[3]
    print(value)
except IndexError:
    print("Index out of range.")

# KeyError
try:
    my_dict = {"name":"Guru"}
    value = my_dict["age"]
    print(value)
except KeyError:
    print("Key is NOT found.")

# FileNotFoundError
try:
    with open("log.txt","r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("File NOT found.")



# Checking Multiple Exceptions
# Multiple excepts Blocks
try:
    num_1 = int(input("Enter first number: "))
    num_2 = int(input("Enter second number: "))
    res = num_1/num_2
    print(f"Result: {res}")
except ValueError:
    print("Please enter valid number!")
except ZeroDivisionError:
    print("Cannot divide by ZERO!")


# One except for Multiple Exceptions
try:
    num_1 = int(input("Enter first number: "))
    num_2 = int(input("Enter second number: "))
    res = num_1/num_2
    print(f"Result: {res}")
except (ValueError,ZeroDivisionError) as error:
    print(f"Error: {error}")


# Catching Any Exception
# This catches EVERYTHING (including typos etc)
try:
    num = int(input("Enter number: "))
    result = 100/num
    print(result)
except Exception as e:
    print(f"Something went wrong: {e}")

# Better to catch specific EXCEPTIONS
try:
    num_1 = int(input("Enter first number: "))
    res = 100/num_1
    print(f"Result: {res}")
except ValueError:
    print("Please enter valid number!")
except ZeroDivisionError:
    print("Cannot divide by ZERO!")


# The 'else' Block 
# The else block run if no exceptions occurs. 
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("That's not a number.")
else:
    # This runs only no error occured
    print(f"Good! You entered {num}")
    square = num*num
    print(f"Square: {square}")


# The 'finally' Block
# The finally block always run whether error occur or not.
try:
    file = open("open.txt","r")
    content = f.read()
    print(content)
except FileNotFoundError:
    print("File not found.")
finally:
    # Always runs
    print("Cleaning up....")
    if 'file' in locals():
        file.close()


# Practical Use of finally
def divide_numbers():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        res = a/b
        return res
    except ValueError:
        print("Input is INVALID!")
    except ZeroDivisionError:
        print("Cannot divide by ZERO!")
    else:
        print(f"First number square: {a**2}")
        print(f"Second number square: {b**2}")
    finally:
        print("Division attempt complete. ")
result = divide_numbers()
print(f"Result: {result}")


# Raising Exceptions
# The 'raise' Keyword
# We can create our own exception using raise
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if age > 120:
        raise ValueError("Age cannot be greater than 120")
    return age
try:
    age = int(input("Enter your age: "))
    age = set_age(age)
    print(f"Age set to: {age}")
except ValueError as e:
    print(f"Error: {e}")


# Raising different exceptions
def validate_password(password):
    if len(password) < 8:
        raise ValueError("Password too short (minimum 8 characters)")
    if not any(c.isupper for c in password):
        raise ValueError("Password needs uppercase.")
    if not any(c.islower() for c in password):
        raise ValueError("Password needs lowercase.")
    if not any(c.isdigit() for c in password):
        raise ValueError("Password needs a number.")
    return True


try:
    pwd = input("Enter password: ")
    validate_password(pwd)
    print("Password Accepted.")
except ValueError as e:
    print(f"Invalid password: {e}")


# Creating Custom Exceptions
# We can create our own exception type for the different programs

# Define a custom exception
class InSufficientFundsError(Exception):
    """Raised When Account has insufficient Funds"""
    def __init__(self, balance, amount, message="Insufficient Fund"):
        self.balance = balance
        self.amount = amount
        self.message = f"{message}. Balance: {balance}, tried to withdraw: {amount}"
        super().__init__(self.message)
class NegativeAmountError(Exception):
    """Raised when amount is negative"""
    def __init__(self, amount , operation):
        self.amount = amount
        self.operation = operation
        super().__init__(f"Invalid {operation} amount: {amount}, Amount must be > 0")

class BankAccount:
    def __init__(self, owner , balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        if amount <= 0:
            raise NegativeAmountError(amount, "deposit")
        self.balance += amount
        print(f"Deposited: {amount} , New_Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise NegativeAmountError(amount, "withdrawal")
        if amount >= self.balance:
            raise InSufficientFundsError(self.balance,amount)
        self.balance -= amount
        print(f"Withdrew: {amount} , New_Balance: {self.balance}")

# --------Testing-----------
account = BankAccount("Mahesh", 1000)
while True:
    try:
        deposit_amount = float(input("Amount to deposit: $"))
        account.deposit(deposit_amount)
        withdraw_amount = float(input("Amount to withdraw: $"))
        account.withdraw(withdraw_amount)
    except NegativeAmountError as e:
        print(f"Error: {e}")
        print("Please enter psoitive amount.")
    except InSufficientFundsError as e:
        print(f"Error: {e}")
        try_again = input("Try different amount (yes/no): ").lower()
        if try_again != "yes":
            break
    except ValueError:
        print("Please enter a valid number.")



# Practice Questions
# Safe Calculator
def safe_calculator():
    print("Simple Calculator")
    print("Enter quit to exit: ")

    while True:
        try:
            # Get User Input
            num1_str = input("\nFirst number: ")
            if num1_str.lower() == "quit":
                break
                
            num2_str = input("\nSecond number: ")
            if num2_str.lower() == "quit":
                break

            # Convert to number
            num1 = float(num1_str)
            num2 = float(num2_str)

            # Get operation
            op = input("Operations: (+,-,*,/)")

            # Calculate result
            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "/":
                result = num1 / num2

            else:
                print("Invalid Operation")
                continue
            print(f"{num1} {op} {num2} = {result}")

        except ValueError:
            print("Please enter valid number.")
        except ZeroDivisionError:
            print("Cannot divided by ZERO")
        except Exception as e:
            print(f"An error occured: {e}")
safe_calculator() 


# Robust File Reader
def read_file_safely(filename):
    """Read file with multiple fallback options"""
    try:
        # try normal read
        with open(filename,"r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"File {filename} NOT found.")
    

    # Try with .txt extension
    try:
        with open(filename + ".txt","r") as f:
            print(f"Found as {filename}.txt")
            return f.read()
    except FileNotFoundError:
        print(f"Also not found as {filename}.txt")

        # Create default file
        print("Creating default file......")
        with open(filename + ".txt","w") as f:
            f.write("Default content")
        return "Default content"
    except PermissionError:
        print(f"Donot have persmission to read '{filename}'")
        return None
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return None


# Use the Functions
filename = input("Enter filename to read: ")
content = read_file_safely(filename)
if content:
    print(f"\nFile Content: \n {content}")



# Input Validation with Retry
def get_valid_number(prompt, min_val = None, max_val = None):
    """Get a Valid Number from user with retries"""
    max_attempts = 3
    attempt = 0
    while max_attempts > attempt:
        try:
            value = float(input(prompt))
            
            if min_val is not None and value < min_val:
                print(f"Number must be at least {min_val}")
                attempt += 1
                continue
            if max_val is not None and value > max_val:
                print(f"Number must be at most {max_val}")
                attempt += 1
                continue
            return value

        except ValueError:
            print(f"Please enter a valid number.")
            attempt +=1
    print(f"Too many invalid attempts. Using default value.")
    return 0

# Use function
age = get_valid_number("Enter your age: ",min_val=0,max_val=120)
print(f"Age: {age}")

score = get_valid_number("Enter score (0-100): ", min_val = 0 , max_val = 100)
print(f"Score: {score}")



# Database Like Operation
class DataStore:
    """Simple data store with error handling"""
    
    def __init__(self, filename="data.txt"):
        self.filename = filename
        self.data = {}
        self.load()
    
    def load(self):
        """Load data from file"""
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    if ":" in line:
                        key, value = line.strip().split(":", 1)
                        self.data[key] = value
            print(f"Loaded {len(self.data)} records")
        except FileNotFoundError:
            print(f"No existing data file. Starting fresh.")
        except Exception as e:
            print(f"Error loading data: {e}")
    
    def save(self):
        """Save data to file"""
        try:
            with open(self.filename, "w") as f:
                for key, value in self.data.items():
                    f.write(f"{key}:{value}\n")
            print("Data saved successfully")
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def get(self, key):
        """Get value by key"""
        try:
            return self.data[key]
        except KeyError:
            return None
    
    def set(self, key, value):
        """Set key-value pair"""
        self.data[key] = value
        self.save()

# Use the data store
store = DataStore("my_data.txt")

while True:
    print("\n--- Data Store ---")
    print("1. View data")
    print("2. Add/update data")
    print("3. Get data")
    print("4. Quit")
    
    choice = input("Choose: ")
    
    if choice == "1":
        if store.data:
            for key, value in store.data.items():
                print(f"  {key}: {value}")
        else:
            print("No data")
    
    elif choice == "2":
        key = input("Key: ")
        value = input("Value: ")
        store.set(key, value)
        print("Saved!")
    
    elif choice == "3":
        key = input("Key to lookup: ")
        value = store.get(key)
        if value:
            print(f"Value: {value}")
        else:
            print("Key not found")
    
    elif choice == "4":
        print("Goodbye! 😊🙌")
        break

        
# practice
def safe_int(value):
    try:
        return int(value)
    except ValueError:
        return 0

print(safe_int("123"))   
print(safe_int("hello")) 
print(safe_int("45.6"))  




# FileNotFoundError exception usage
filename = input("Enter filename: ")

try:
    with open(filename, "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print(f"File '{filename}' not found!")
    create = input("Create it? (yes/no): ").lower()
    if create == "yes":
        with open(filename, "w") as f:
            f.write("")
        print(f"Created {filename}")


# ToYoungError custom exception
class TooYoungError(Exception):
    pass

def validate_age(age):
    if age < 18:
        raise TooYoungError(f"Age {age} is too young (must be 18+)")
    return True

try:
    age = int(input("Enter your age: "))
    validate_age(age)
    print("Access granted!")
except TooYoungError as e:
    print(f"Access denied: {e}")
except ValueError:
    print("Please enter a valid number")
