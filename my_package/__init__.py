# my_package/__init__.py
# This code runs when the package is imported

print("Loading my_package...")

# Make certain functions available at package level
from .math_utils import double, triple
from .string_utils import shout

# Control what 'from package import *' imports
__all__ = ['double', 'triple', 'shout']

import my_package

print(my_package.double(5))   # 10 (available directly)
print(my_package.shout("hi")) # HI
