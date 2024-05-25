# 2.	Write a Python program to calculate the length of a string, to split and join a string, to demonstrate various ways of accessing the string.

string = 'Hi, my name is Shivam.'

# Length of a string
print(f'Length of the string: {len(string)}')

# Splitting a string
split_string = string.split()
print(f'Splitting the string: {string.split()}')

# Joining a string
print(f'Joining the string: {" ".join(split_string)}')

# Accessing the string
print(f'Accessing the string: {string[0:]}')
print(f'Accessing the string: {string[:-1]}')
print(f'Accessing the string: {string[:len(string)]}')

