# This is the module for 06_py
# Fibonacci module
def fib(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else :
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence