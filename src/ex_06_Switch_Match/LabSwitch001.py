# Use this when you have more than 20 conditions. otherwise use If-Else condition
# no break point
# Match-Case
day = int(input("Enter the day: "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _: #Default case if nothing is matched
        print("Day is invalid")