# my_package/register.py 
# Registeration program using validator
import validator

def get_valid_input(prompt, validator_func):
    """Get input until valid"""
    while True:
        value = input(prompt)
        if validator_func(value):
            return value
        print("Invalid input, try again.")

# Use the module
email = get_valid_input("Email: ", validator.is_valid_email)
age = get_valid_input("Age: ", validator.is_valid_age)
password = get_valid_input("Password: ", validator.is_strong_password)

print("\nRegistration successful!")
print(f"Email: {email}")
print(f"Age: {age}")
