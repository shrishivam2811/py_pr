# Python program for file operations such as opening a file, reading from it, writing into it, closing it, renaming a file, deleting a file, and various file methods

import os
# Opening a file
file = open("file.txt", "w")

# Writing into the file
file.write("Hello, World!\n")
file.write("This is a sample file.")

# Closing the file
file.close()

# Opening the file for reading
file = open("file.txt", "r")

# Reading from the file
content = file.read()
print(content)

# Closing the file
file.close()

# Renaming a file
os.rename("file.txt", "new_file.txt")

# Deleting a file
os.remove("new_file.txt")

# Checking if a file exists
if os.path.exists("new_file.txt"):
    print("File exists")
else:
    print("File does not exist")