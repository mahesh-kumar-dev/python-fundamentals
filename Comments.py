# comments are text in code which is completely ignored
# Single line comment:
# starts with hash symbol (#) everything after it can be ignored
print("Welcome to Python World") # this is single line comment

'''
Multi-Line Comments:
we can make multi-line comments by using triple quoted """,''' 
'''
'''
print("Hello dear, you are my user")

"""
Docstrings: official documentation for functions, classes , modules.
            they are written in triple quotes

"""

def greet():
    """
    This function prints a greeting.
    This text will be saved as documentation.
    """
    print("Hello!")

# You can see the docstring with:
print(greet.__doc__)

# Special First Line: Shebang (Unix/Linux/macOS)
# The very first line of a script can tell the computer which program to use:
#!/usr/bin/env python3
# This tells Linux/Mac to use Python 3

# Rules:
# Use space after #
# use complete explanatory sentences


def function():
    """Docstring - official documentation"""
    pass

