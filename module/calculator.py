# calculator.py module
def add(a,b):
    return a + b

def sub(a, b):
    return a - b


# This code is run when testing this module directly
if __name__ == "__main__":
    # Test the functions
    print("Testing Calculator......")
    print(f"5 + 6 = {add(5,6)}")
    print(f"5 - 3 = {sub(5,3)}")
    print("Test completed.")

print(f"Module name: {__name__}")