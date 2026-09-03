# my_package/text_utils.py 
def count_words(text):
    return len(text.split())

def reverse_string(string):
    return string[::-1]

def is_palindrome(text):
    clean = text.lower().replace(" ","")
    return clean == clean[::-1]

if __name__ == "__main__":
    print("Testing text utils.....")
    print(f"Count words: {count_words("Hello Jon Snow")}")
    print(f"Reverse string: {reverse_string("Python")}")
    print(f"Is Palindrome: {is_palindrome("racecar")}")

