#find max of 3 numbers

num1 = int(input("Enter the num1\n"))
num2 = int(input("Enter the num2\n"))
num3 = int(input("Enter the num3\n"))

if num1 >= num2 and num1 >= num3:
    print("Maximum", num1)
elif num2 >= num3:
    print("Maximum", num2)
else:
    print("Maximum", num3)
