#Find the number is even or odd

num=int(input("Enter a number:"))
if num >=0:
    if num%2==0:
        print("The number is even")
    else:
        print("The number is odd")
else:
    print("The number is Negative")

# You can write short one-liner conditions using ternary operator:
if num >=0:
        print(" even" if num%2==0 else " odd")
else:
    print("The number is Negative")