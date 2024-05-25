# Write a Python program for simple interest, and compound interest by taking user input.

def si(p,r,t):
    return (p*r*t)/100

def ci(p,r,t,n):
    amount = p*(1+(r/(n*100)))**(n*t)
    return amount - p

p = float(input('Enter the principal amount: '))
r = float(input('Enter the rate of interest (in %): '))
t = float(input('Enter the time period (in years): '))
n = float(input("Enter the number of times interest is compounded per year: "))


simple_interest = round(si(p,r,t),2)
compound_interest = round(ci(p,r,t,n),2)

print(f'Simple interest = {simple_interest}')
print(f'Compound interest = {compound_interest}')