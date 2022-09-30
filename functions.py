def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%d:%02d:%02d" % (hour, minutes, seconds)

# Driver program
n = 12345
print(convert(n))

import os
import sys
from PIL import Image

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        im = Image.open(sys.argv[1])
        target_name = sys.argv[1] + ".jpg"
        rgb_im = im.convert('RGB')
        rgb_im.save(target_name)
        print("Saved as " + target_name)
    else:
        print(sys.argv[1] + " not found")
else:
    print("Usage: convert2jpg.py <file>")
'''
Find specific files on your system
Often, you forget the names or location of files on your system. This is not only annoying but also consumes time navigating through different folders. While there are programs that help you search for files, you need one that can automate the process. 
'''
import fnmatch
import os

rootPath = './'
pattern = '*.pyc'
print('Searching...')
#print(list(os.walk(rootPath)))

for root, dirs, files in os.walk(rootPath):
    for filename in fnmatch.filter(files, pattern):
        print( os.path.join(root, filename))
        
import string
from random import *

print('random paswword')
characters = string.ascii_letters + string.punctuation  + string.digits
password =  "".join(choice(characters) for x in range(randint(8, 16)))
print (password)
'''
Removing items from a list
You’ll often have to modify lists on your projects. Python enables you to do this using the Insert() and remove() methods. Here is a script you can use to achieve this.
'''
# Declare a fruit list
fruits = ["Mango","Orange","Guava","Banana"]

# Insert an item in the 2nd position
fruits.insert(1, "Grape")

# Displaying list after inserting
print("The fruit list after insert:")
print(fruits)

# Remove an item
fruits.remove("Guava")

# Print the list after delete
print("The fruit list after delete:")
print(fruits)
'''
Count list items
Using the count() method, you can print how many times a string appears in another string. You need to provide the string that Python will search. Here is a script to help you do so.
'''
# Define the string
string = 'Python Bash Java PHP PHP PERL'
# Define the search string
search = 'P'
# Store the count value
count = string.count(search)
# Print the formatted output
print("%s appears %d times" % (search, count))