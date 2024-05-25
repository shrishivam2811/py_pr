# Write a Python program to multiply all the items in a list, to Reverse a linked list, to find smallest number in a list, and to find largest number in a list.

my_list = [1,2,3,4,5]

# Multiplying all the items in a list
def multiply_list(my_list):
    result = 1
    for i in my_list:
        result *= i
    return result

print(f'Multiplying all the items in a list: {multiply_list(my_list)}')

# Finding the smallest number in a list
print(f'Smallest number in a list: {min(my_list)}')

# Finding the largest number in a list
print(f'Largest number in a list: {max(my_list)}')