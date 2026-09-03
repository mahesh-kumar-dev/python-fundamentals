# my_package/math_utils.py 
# Double the number
def double(x):
    return x * 2

# Triple the number
def triple(x):
    return x * 3

def sqr(num):
    return num ** 2

def is_prime(num):
    if num < 2:
        return False
    for i in range(2,int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def even_odd(numbers):
    evens = []
    odds = []
    for i in numbers:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    return evens, odds

def cube(x):
    return x**3

def factorial(n):
    """Calculate Factorial"""
    if n < 0:
        return "Factorial of Negative number is not defined."
    if 0 <= n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    """ Generate first n Fibonacci numbers"""
    result = []
    a,b = 0,1
    for _ in range(n):
        result.append(a)
        a,b = b, a + b
    return result

# Test when run directly
if __name__ == "__main__":
    print("Testing mymath module...")
    print(f"is_prime(17): {is_prime(17)}")
    print(f"factorial(5): {factorial(5)}")
    print(f"fibonacci(10): {fibonacci(10)}")
