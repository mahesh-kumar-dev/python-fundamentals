# PYTHON SETS
# set is a collection that stores unique items with no particular order.
# Use sets for: Removing duplicates, checking membership, mathematical set operations (union, intersection).
'''
    CHARACTERISTICS: 
    No duplicates -> Each item appears only once
    Unordered -> You cannot access by index (no position)
	Fast -> Very quick to check if an item exists
	Changeable -> You can add or remove items

'''

# CREATING SETS
# By curly braces {}
genders = {"Male","Female","Gay","Transgender","Lesbian"}
print(genders)

# Duplicate are automatically deleted 
numbers = {1,2,3,1,1,3,2}
print(numbers)

# Mixed type possible but not common 
mixed = {1,"Mahi",3.14,True}
print(mixed)

# Creating empty sets
# wrong this creates dictionary not set 
empty = {}
print(type(empty))

# Correct: use set() constructor
empty_set = set()
print(type(empty_set))
print(empty_set)

# Creating sets from other types
# From list ( remove duplicate automatically)
my_list = [1,2,2,3,3,3,4]
my_set = set(my_list)
print(my_set)

# From string (unique characters)
text = "Hello"
unique_char = set(text)
print(unique_char)

# From tuple 
my_tuple = (1,2,2,3,4,3)
my_set = set(my_tuple)
print(my_set)

# ADDING AND REMOVING ITEMS
# .add() – Add one item
fruits = {"apple", "banana"}

# add new item
fruits.add("cherry")
print(fruits)

# adding existing item doesnot change (no error)
fruits.add("apple")
print(fruits)

# .update() – Add multiple items
# add from another set
fruits.update({"date","blueberry"})
print(fruits)

# add from list 
fruits.update(["elderberry","fig"])
print(fruits)

# add from tuple 
fruits.update(("grapes","honeydew"))
print(fruits)

# .remove() – Remove item (error if not found)
tree = {"roots","leaf","flower","nodes"}
tree.remove("roots")
print(tree)

# removing non-existing cause error 
# tree.remove("shoot")

# discard() – Remove item (no error if not found)
tree.discard("leaf")
print(tree)

tree.discard("adventituous roots") # does nothing no error
print(tree)

# pop() – Remove and return arbitrary item
colors  = {"red","blue","green"}
# remove random items (because set are unordered )
removed = colors.pop()
print(f"Removed: {removed}")
print(f"Remaining: {colors}")

# clear() – Remove all items
colors.clear()
print(colors)


# ACCESSING SET ITEMS
# Check if items exits (fast)
acids = {"Hydrochloric Acid","Sulphuric Acid","Nitric Acid"}
print("Sulphuric Acid" in acids)
print("Hydrogen" in acids)

# Looping through sets
# output could be any order
for acid in acids:
    print(acid)

# Getting set length
print(len(acids))

# Converting to List for order
names = {"Mahesh", "Asma","Aqsa"}

# Convert to list (order may still random)
names_list = list(names)
print(names_list)

# Get sorted List
sorted_names = sorted(names)
print(sorted_names)


# SET OPERATIONS (MATHEMATICAL)
# Union (| or union()) – All items from both sets
set_a = {1,2,3}
set_b = {3,4,5}
# Using |(union operator) for union operation
union_set = set_a | set_b
print(union_set)

# Using Union Method
union_set = set_a.union(set_b)
print(union_set)

# Multiple sets
set_c = {5,6,7}
union_all = set_a | set_b | set_c
print(union_all)

# Intersection (& or intersection()) – Common items only
set_a = {1,2,3,4}
set_b = {3,4,5,6}

# Using operator
common = set_a & set_b
print(common)

# Using method
common = set_a.intersection(set_b)
print(common)

# Difference (- or difference()) – Items in first but not second
# Using operator: Items in A but not in B
diff = set_a - set_b
print(diff)

# Items in B not in A
diff = set_b - set_a
print(diff)

# Using method 
diff = set_a.difference(set_b)
print(diff)

# Symmetric Difference (^ or symmetric_difference()) – Items in either, not both
#  Using operator
# Items that are in one not in both
sym_diff = set_a ^ set_b
print(sym_diff)

# using method
sym_diff = set_a.symmetric_difference(set_b)
print(sym_diff)


# SUBSET AND SUPERSET
# issubset() – All items in set are in another
set_x = {1,2,3}
set_y = {1,2,3,4,5}
set_z = {1,2,6}

print(set_x.issubset(set_y))
print(set_z.issubset(set_y))

# using operator <=
print(set_x <= set_y)

# issuperset() – Contains all items of another
print(set_x.issuperset(set_y))
print(set_x.issuperset(set_z))

# Using operator >=
print(set_x >= set_y)

# isdisjoint() – No common items
set_p = {1,2,3}
set_q = {4,5,6}
set_r = {3,4,5}
print(set_p.isdisjoint(set_q))
print(set_p.isdisjoint(set_r))


#  SET COMPREHENSION
# square of numbers 0-9
square = {x**2 for x in range(10)}
print(square)

# Even number only 
evens = {x for x in range(20) if x%2 == 0}
print(evens)

# Convert String to uppercase
words = ["Hello","Assu","Baba"]
upper_set =  {word.upper() for word in words }
print(upper_set)


# Frozenset (Immutable Set)
# A frozenset is a set that cannot be changed (immutable). It can be used as a dictionary key.
frozen = frozenset([1,2,3])
print(frozen)

# frozen.add(4) # Attribute ERROR  cannot change

# Used as dictionary key
locations = {
    frozenset([1,2]): "Point A",
    frozenset([3,6]): "Point B"
}
print(locations[frozenset([1,2])])


# Practice Questions 
# Removing duplicate from List
numbers = [1,1,2,2,2,3,3,4,4,4,5,5]
# Original list with duplicate
print(f"Original List: {numbers}")

# Remove duplicate using set 
unique = list(set(numbers))
print(f"Unique: {unique}")

# Preserve original order (Advance)
seen = set()
unique_ordered = []
for num in numbers:
    if num not in  seen:
        unique_ordered.append(num)
        seen.add(num)
print(f"Unique: (preserving order) {unique_ordered}")


# Finding common element 
# Two group of students
group_a = {"Mahesh","Sitara","Erum","Sana"}
group_b = {"Asma","Sana","Mahesh","Bakhtawar"}

# Students in both group 
both = group_a & group_b
print(f"Student in both: {both}")

# Students only in A
std_in_a = group_a - group_b
print(f"Only in A: {std_in_a}")

# Student only in B
std_in_b = group_b - group_a
print(f"Only in B: {std_in_b}")

# All Students (no duplicates)
all_students = group_a | group_b
print(f"All Student: {all_students}")


# Finding Unique Letters
sentence = "the quick brown fox jumps over a lazy dog."

# Convert to set of letters ( ignore spaces)
letters = {chars for chars in sentence.lower() if chars.isalpha()}
print(f"Unique Letters: {sorted(letters)}")

# check if sentence is pangram (contain all letters)
alphabet = set("abcdefghijklmnopqrstuvwxyz")
is_pangram = alphabet.issubset(letters)
print(f"Is Pangram: {is_pangram}")



# Tag System
# Blog post tags
post1_tags = {"python","programming","beginner"}
post2_tags = {"python","advance","tutorial"}
post3_tags = {"java","prgramming","beginner"}

# All tags across all posts 
all_tags = post1_tags | post2_tags | post3_tags
print(f"All tags: {all_tags}")

# tags used in multiple posts
common_tags = (post1_tags & post2_tags ) | (post1_tags & post3_tags) |         (post2_tags & post3_tags)
print(f"Popular tags: {common_tags}")

# Tags unique to python posts
python_posts_tags = post1_tags | post2_tags
other_tags = post3_tags
unique_python_tags = python_posts_tags - other_tags
print(f"Unique Python Tags: {unique_python_tags}")



# Two strings are anagrams (same letters and different order)
def are_anagram(str1, str2):
    return set(str1.lower()) == set(str2.lower())

print(are_anagram("listen","silent"))
print(are_anagram("hello","world"))


# Find all unique vowels
sentence = "The quick brown fox jumps over a lazy dog."
vowels = set("aeiou")
found_vowels = {char for char in sentence.lower() if char in vowels}
print(f"Vowel found: {sorted(found_vowels)}")