# Write a Python program to multiply all the items in a list, to Reverse a linked list, to find smallest number in a list, and to find largest number in a list.

my_list = [1,2,3,4]

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

# Reversing a linked list
class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def reverse_linked_list(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.next = node2
node2.next = node3
node3.next = node4

print("Original Linked List:")
print_linked_list(node1)

reversed_head = reverse_linked_list(node1)
print("Reversed Linked List:")
print_linked_list(reversed_head)