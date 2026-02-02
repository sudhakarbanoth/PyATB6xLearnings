# An API sometimes fails due to network delays.
#
# Write a program to retry the API call 3 times until the response code becomes 200.
#
# If it still fails after 3 tries, print a failure message.
#
# Hint: Use a while loop with a counter.
# Hint: Use a while loop with a counter.
#
# Expected Output Example:
#
# Attempt 1: Response 500
#
# Attempt 2: Response 200
#
# ✅ Test Passed

counter = 1
max_attempts = 3
while counter <= max_attempts:
    response = int(input(f"Enter response code for Attempt {counter}: "))

    print(f"Attempt {counter}: Response {response}")

    if response == 200:
        print("✅ Test Passed")
        break
    counter += 1

else:
    print("❌ Test Failed after 3 attempts.")

