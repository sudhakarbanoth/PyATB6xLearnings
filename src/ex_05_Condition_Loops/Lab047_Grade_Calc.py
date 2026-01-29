# Grade Calculator:
# Write a program that calculates and displays the letter grade
# for given number scopre (e.g., A, B, C, D, or F)
# Based on the following grading scale
#
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

# Logic Buidling Formula

# 1-> User inputs - score -> int
# 2 -> o/p --> str -> A,B

score = int(input("Enter your score: "))
if score < 0 or score > 100:
    print("Enter a valid score")

else:
    if 90 <= score <= 100:
        print("Grade A")
    elif 80 <= score <= 89:
        print("Grade B")
    elif 70 <= score <= 79:
        print("Grade C")
    elif 60 <= score <= 69:
        print("Grade D")
    else:
        print("Grade F")

# if user enter float or string then handle with try-catch


