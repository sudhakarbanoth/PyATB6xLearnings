# Write a Python program to calculate the
# area of a circle given its radius using the formula
# ``` area=π×r^2``` ( Take pie as 3.14)

# i/p - r -float
# o/p -->String formatted output of area

import math
radius = float(input("Enter radius: "))
area = math.pi* pow(radius,2)

# string formatting, python f-strings
print(f"The area of the circle is:{area:.2f}")
