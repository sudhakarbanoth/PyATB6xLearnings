# Write a program to take a user input and let him know if he can go to club
# age limit is 21

age = int(input("What is your age?"))

if age >=21:
    print("Yes, can go club")
else:
    print("No, can't go club")


## Edge cases has to be covered such as
# Negative values, non-numeric values, Very big values
# -1,ABC,130

age = int(input("What is your age?"))

if age<=0 or age>130:
    print("Enter a valid age")
else:
    if age >=21:
        print("Yes, can go club")
    else:
        print("No, can't go club")