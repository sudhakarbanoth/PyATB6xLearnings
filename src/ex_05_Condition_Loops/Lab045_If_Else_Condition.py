# Find the max of 2 numbers without using inbuilt function

num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))

# if num1 > 0 and num2 > 0:
#     print("Number should be positive")

if num1 >= num2:
    print("Maximum", num1)
else:
    print("Maximum", num2)

# num1 == num2 ->  Handled.