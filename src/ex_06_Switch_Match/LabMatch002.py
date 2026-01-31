# Use this when you have more than 20 conditions. otherwise use If-Else condition

print("Enter the which Test you want to run")
test_type = input("Enter the Test Type : API, UI, Performance, Security: ").strip()

match test_type:
    case "API":
        print("We are running a POSTMAN API Testcase.")
    case "UI":
        print("We are running a Selenium Testcase.")
    case "Performance":
        print("We are running a Performance Testcase.")
    case "Security":
        print("We are running a Security Testcase.")
    case _: #Default case if nothing is matched
        print("Invalid Type.")

# Same code in IF-ELSE condition
# test_type = input("Enter the test type: ").strip()
#
# if test_type == "API":
#     print("We are running a POSTMAN API Testcase.")
# elif test_type == "UI":
#     print("We are running a Selenium Testcase.")
# elif test_type == "Performance":
#     print("We are running a Performance Testcase.")
# elif test_type == "Security":
#     print("We are running a Security Testcase.")
# else:
#     print("Invalid Type.")