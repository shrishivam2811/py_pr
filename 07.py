# Write a program that inputs a text file. The program should print all of the unique words in the file in alphabetical order.

def unique_words(file):
    with open(file, 'r') as f:
        words = f.read().split()
        unique = set(words)
        print(sorted(unique))

file = input('Enter the file path: ')
unique_words(file)