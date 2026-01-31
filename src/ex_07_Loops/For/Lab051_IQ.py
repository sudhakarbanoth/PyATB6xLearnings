print("Print Loop 1")
for i in range(1, 10): # Output will be 1 to 9
    print(i)

print("Print Loop 2")
for i in range(10): # Output will be 0 to 9
    print(i)

print("Print Loop 3")
for i in range(-1,-10,-1): # Output will be -1 to -9
    print(i)

print("Print Loop 4") # No output (no error)
for i in range(1, 10,-1):
    print(i)