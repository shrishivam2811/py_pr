# 4. Write a Python program to perform the following operations on Dictionaries:  Creating and inserting in the Dictionary, Updating the Dictionary, deleting from the Dictionary, Looping in the Dictionary, and sorting in the Dictionary

# Creating and inserting in the Dictionary
my_dict = {'name':'Shivam','age':20, 'course':'B.Tech'}
print(f'Creating and inserting in the Dictionary: {my_dict}')

# Updating the Dictionary
my_dict['age'] = 19
print(f'Updating the Dictionary: {my_dict}')

# Deleting from the Dictionary
del my_dict['age']
print(f'Deleting from the Dictionary: {my_dict}')

# Looping in the Dictionary
for key, value in my_dict.items():
    print(f'Looping in the Dictionary: {key} : {value}')

# Sorting in the Dictionary
print(f'Sorting in the Dictionary: {sorted(my_dict)}')
print(f'Sorting in the Dictionary: {sorted(my_dict, reverse=True)}')
print(f'Sorting in the Dictionary: {sorted(my_dict.keys())}')
print(f'Sorting in the Dictionary: {sorted(my_dict.values())}')
print(f'Sorting in the Dictionary: {sorted(my_dict.items())}')