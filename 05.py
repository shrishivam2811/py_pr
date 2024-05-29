# Write a Python function to find the maximum and minimum numbers from a sequence of numbers.

# Solution:
def max_min(sequence):
    return max(sequence), min(sequence)

sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f'Maximum number is {max(sequence)} and Minimum number is {min(sequence)}')