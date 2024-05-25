# Write a Python program for simple interest, and compound interest by taking user input.

def si(p,r,t):
    return (p*r*t)/100

def ci(p,r,t,n):
    return p*(1+(r/n))**(n*t)

p = int(input('Enter the principal amount: '))
r = int(input('Enter the rate of interest: '))
t = int(input('Enter the time period: '))
n = int(input("Enter the number of times interest is compounded per year: "))


simple_interest = si(p,r,t)
compound_interest = ci(p,r,t,n)

print(f'Simple interest = {simple_interest}')
print(f'Compound interest = {compound_interest}')