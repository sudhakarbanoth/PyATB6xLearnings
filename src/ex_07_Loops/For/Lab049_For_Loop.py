print("Print Loop 1")
for i in range(0,10,1): # Output will be 0 to 9
    print(i)

print("Print Loop 2")
for i in range(0,10,2): # Output will be 0,2,4,6,8
    print(i)

print("Print Loop 3")
for i in range(0,10,3): # Output will be 0,3,6,9
    print(i)

# Step type should be only integer.
# for other type use other loop types
#for i in range(0,10,1.5): throws syntax error becuase step cant be float
#    print(i)