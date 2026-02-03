from tokenize import blank_re

n=int(input("Enter the number to find the factorial:"))
if n==0:
    print("Factorial is 1")
elif n>0:
    fact = 1
    for i in range(1,n+1):
        fact=fact*i
    print("Factorial is ",fact)
else:
    print("Factorial is not defined for negative numbers")


# Edge Cases:
# Large Integer
# string
# boolean
# alphanumeric
# blank
# symbol
# special character
# decimal(float)
