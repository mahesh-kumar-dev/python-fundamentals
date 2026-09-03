# my_package/validator.py 
# Input validation module

def is_valid_email(email):
    """Simple Email Validation"""
    return '@' in email and '.' in email

def is_valid_age(age):
    """Age Validation"""
    try:
        age_num = int(num)
        return 0 <= age_num <= 120
    except ValueError:
        return False

def is_strong_password(password):
    """Password strength check"""
    if len(password) < 8:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.lower() for c in password)
    has_number = any(c.isdigit() for c in password)
    return has_lower and has_number and has_upper

if __name__ == "__main__":
    # Quick test
    print("Testing Validator.......")
    print(f"payal23@gmail.com: {is_valid_email("payal23@gmail.com")}")
    print(f"Age 25: {is_valid_age('25')}")
    print(f"Password 'Pass123!': {is_strong_password('Pass123!')}")

