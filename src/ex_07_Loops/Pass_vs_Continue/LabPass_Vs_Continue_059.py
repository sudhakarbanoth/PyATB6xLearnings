for i in range(5):#skips 3rd iteration and will not print value 3
    if i == 3:
        continue
    print("Number: ", i)

for i in range(5):#prints 3rd iteration and will print value 3
    if i == 3:
        pass
    print("Number: ", i)