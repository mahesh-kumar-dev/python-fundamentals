
# All String Methods Tutorial
# How to use methods : string.methods()

# Part 1: Case Methods
print("-------Case Methods-------")
# .upper() to convert UPPPERCASE
text4 = "Hello World"
print("Original Case: ",text4)
print("Uppercase: ",text4.upper())

user_input = "yes"
if user_input.upper()=="YES":
    print("User agreed.")

# .lower() convert to lowercase
text5 ="IBA SUKKUR"
print("Original: ",text5)
print("lower case: ", text5.lower())

# . capitalize() – First letter uppercase, rest lowercase
print("Capitalize: ",text5.capitalize())

# . title() – Each Word Capitalized
text6 = "welcome to python world"
print("Original: ", text6)
print("Title: ",text6.title())

# . swapcase() – Swap uppercase/lowercase

print("Original: ", text4)
print("Swapcase: ",text4.swapcase())

print("\n-------Search Methods--------")
# . find() – Find position of text
sen = "my father is sewing cloth, He is hardworking person"

# Find position of is
pos = sen.find("is")
print(pos)

# find with starting position
pos = sen.find("is",6)
print(pos)

# Not found -1 return 
pos = sen.find("at")
print(pos)

# Find last occurrence
pos = sen.rfind("son")
print(pos)

# . index() – Like find but raises error if not found
email = "mahesh.kumar@iba.com"
at_pos = email.index("@")
print("Email: ",email)
print("Pos of @: ",at_pos)

# . count() – Count how many times something appears
text = "abracadabra"
count_a = text.count("a")
print("Text: ",text)
print("a count: ",count_a)

# Count with range
text = "abc abc abc"
print(text.count("abc",2,8))

# . startswith() – Check how string begins
filename = "image.jpg"
print("File name: ",filename)
print("Starts with image: ",filename.startswith("image"))
print("Starts with photo: ",filename.startswith("photo"))

# Check multiple possibilities
print(filename.startswith(("image", "photo", "pic")))  # True


# Useful for filtering
files = ["doc.txt", "image.jpg", "photo.png", "file.pdf"]
images = [f for f in files if f.startswith(("image", "photo"))]
print(images)  



# . endswith() – Check how string ends
filenames = "document.pdf"
print(filenames.endswith(".pdf"))
print(filenames.endswith(".txt"))

# Check if multiple extensions
if filenames.endswith((".pdf",",.txt",".doc")):
    print("It\'s a document.")

# Practical Uses
files = ["data.csv","report.pdf","notes.txt","image.png"]
csv_file = [f for f in files if f.endswith(".csv")]
print(csv_file)

print("\n--------Cleaning methods---------")
# . strip() – Remove characters from both ends
fault = "  Gomind  "

# Remove spaces from both sides
correct = fault.strip()
print("Original: ",fault)
print("Correct: ",correct)

# Remove specific characters
text = "***Hello***"
print(text.strip("*"))

# Remove multiple different characters
text = " \t Hi \n "
print(text.strip())

# Remove from left and right
text = "  Mahesh  "
print(text.rstrip())
print(text.lstrip())

# . lstrip() – Remove from left side only
text1 = "  Jai  "
print(f"'{text1.lstrip()}'")

# Remove specific characters from left
text9 = "0000345"
print("Original: ",text9)
print("Modified: ",text9.lstrip())


# . rstrip() – Remove from right side only
text2 = "  Universe  "
print("Original: ",text2)
print("Correct: ",f"'{text2.rstrip()}'")

# Remove trailing zeros
text2 = " 19.900000"
print("Original: ",text2)
print("New: ",f"{text2.rstrip()}")

# . removeprefix() – Remove from beginning (Python 3.9+)
file_name = "img_photo.jpg"
print(file_name.removeprefix("img_"))

# Only remove if exist
print(file_name.removeprefix("video_"))


# . removesuffix() – Remove from end (Python 3.9+)
fileName = "document.pdf"
print(fileName.removesuffix(".pdf"))

# Only remove if exists
print(fileName.removesuffix(".txt"))

print("\n-----Split and Joining methods-----")
# . split() – Break string into list
sentence = "A quick brown fox "
words = sentence.split()
print(words)

# Split by specific characters
sentence1 = "goat,horse,dog"
animals = sentence1.split(",")
print(animals)

# Limit number of splits
counting = "one,two,three,four"
print(counting.split(",",3))

# Split by any whitespace (tab, newline, space)
char = "a  b\tc \nd"
print(char.split())

# . rsplit() – Split from right side

# Like split works from end
path = "home/user/document/files.txt"
print(path.rsplit("/",1))

# Get file Extension
file = "archive.tar.zip"
name , extension = file.rsplit(".",1)
print(f"Name: {name}, Extension: {extension}")


# . splitlines() – Split by line breaks
mul_line = "line1\nline2\r\nline3"
lines = mul_line.splitlines()
print(lines)

# Keep Line breaks
lines = mul_line.splitlines(True)
print(lines)

# Works with different line endings
txt = "Hello\nPython\'s\nWorld"
print(txt.splitlines())

# . join() – Join list into string (IMPORTANT!)
# Join with spaces
wordings = ["Hi","Laila"]
result = " ".join(wordings)
print(result)

# Join With Commas
fruits = ["Apples","Banana","Grapes"]
res = " ".join(fruits)
print(res)

# Join with nothing
print("".join(wordings))

# Numbers must be string first
numbers = [1,2,3]
num_str = "-".join(str(n) for n in numbers)
print(num_str)

# join is FASTER than using + in loops


print("\n-------Padding Methods (Adding Characters)-----------")
# . center() – Center text in given width
msg = "Hemlata"
print(f"|{msg.center(11)}|")
print(f"|{msg.center(11,"*")}|")

# Create practical Banner
tile = "Welcome"
print(f"{tile.upper().center(50,"=")}")

# . ljust() – Left justify (pad on right)
greet ="Hi Dear"
print(f"|{greet.ljust(15)}|")
print(f"|{greet.ljust(15,"+")}|")

# . rjust() – Right justify (pad on left)
print(f"|{greet.rjust(15)}|")
print(f"|{greet.rjust(15,"+")}|")

# useful for alining numbers
for i in range(1,6):
    print(str(i).rjust(3), str(i**2).rjust(3))

# . zfill() – Pad with zeros on left
# Add zeros to make string certain length
print("29".zfill(7))
print("-49".zfill(6))

# Useful for creating numbered files
for i in range(1,10):
    filename = f"image_{str(i).zfill(3)}.jpg"

print("\n------Checking Methods----------")
# . isalpha() – All letters?
print("123".isalpha())
print("hello".isalpha())
print("hello0012".isalpha())
print("".isalpha())
print("Vaibhav Sooryavanshi".isalpha())


# . isdigit() – All digits?
print("456".isdigit())
print("0012abc".isdigit())
print("".isdigit())
print("12.23".isdigit())
print("-12".isdigit())

# . isalnum() – Letters or digits only?
print("Employee01".isalnum())
print("Harry!".isalnum())
print("123".isalnum())
print("".isalnum())


# . isspace() – All whitespace?
print("  ".isspace())
print("\t\n".isspace())
print("  a".isspace())
print("".isspace())


# . isupper() – All uppercase?
print("HONEY".isupper())
print("".isupper())
print("Hey123".isupper())
print("hurrah".isupper())

# . islower() – All lowercase?
print("yah".islower())
print("Doremon".islower())
print("IRONMAN".islower())
print("Captain01".islower())

# . istitle() – Title case (each word capitalized)?
print("Marvel Studio".istitle())
print("Thor mjonor".istitle())
print("bLACK pANTHER".istitle())

# . isprintable() – All characters printable?
print("Melody".isprintable())
print("Modi\n".isprintable())

# . isascii() – All characters ASCII? (Python 3.7+)
print("Deepak".isascii())
print("Shaktim@an".isascii())
print("000".isascii())
print("café".isascii())


print("\n-----Replacement Methods-------")
# . replace() – Replace text

# Replace all occurrences
name = "Calf Hamstring"
print(name.replace("a","@"))


# Replace with limit
pent = "baggy baggy baggy"
print(pent.replace("ba","sh",3))

# Remove text (replace with empty)
actor = "Yash-Raj"
print(actor.replace("-"," "))

# Chain replacements
alpha = "a,b,c"
print(alpha.replace(",","|").replace("|",";"))

print("\n-----Translation Methods------")
# .maketrans() – Create translation table
trans_table = str.maketrans("abc","123")

data = "a b c"
print(data.translate(trans_table))

# Remove characters   (third arguements)
trans_tab = str.maketrans("","","aeiou")
texts = "Iam Mother of Dragon."
print(texts.translate(trans_tab))


# Simple cipher (ROT13)
def rot13(text7):
    trans = str.maketrans(
       'ABCDEFGHIJKLMabcdefghijklm',
       'NOPQRSTUVWXYZnopqrstuvwxyz'

    )
    return text7.translate(trans)

print(rot13("Universe-Bose"))

print("\n------Other Useful Methods---------")
# . format() – Format string 
name1 = "Ifra Mahboob"
age = 19
print("Name: {} Age: {} ".format(name1,age))

# . format_map() – Format with dictionary
data1 = {"name": "Zikra", "age": 21}
print("Name: {name}, Age: {age}".format_map(data1))


# . expandtabs() – Expand tab characters
mess = "Programming\tWorld"
print(mess.expandtabs(5))

# . partition() – Split into three parts
name = "Mahesh Kumar"
parts = name.partition(" ")
print(parts)

# . rpartition() – Partition from right
numberings = "one.two.three"
print(numberings.rpartition("."))

'''# . translate() – Apply translation table
import string
# Remove punctuations
text7 = "Hello, Asma! How are you dear?"
tran_tab = str.maketrans("","",string.punctuation)
clean = text7.translate(tran_tab)
print(clean)

'''

print("\------Practice Questions-------")
user_input = input("Enter your name: ").strip().lower()
print(f"Cleaned: {user_input}")

sentence2 = input("Enter a sentence: ")
word_count = len(sentence2.split())
print(f"Word Count: {word_count}")

text8 = input("Enter any text: ").lower().replace(" ","")
if text8 == text[::-1]:
    print("Palindrome!")
else: 
    print("Not Palindrome!!!!!")


email_ = input("Enter your email: ")
domain = email.split("@")[1]
print(f"Domain: {domain}")
