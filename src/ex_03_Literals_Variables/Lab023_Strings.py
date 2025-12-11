#Python always have strings, no concept of characters

value = input("Enter the value")
print(value)
print(type(value)) #type will be string

# Strings
name = "Sudhakar"
# Bunch of char
c = 'C'
c1 = "C"
print(type(c)) # <class 'str'>
print(type(c1)) # <class 'str'>

print(len(name)) #8 (length always starts from 1
print(name.upper()) # SUDHAKAR
print(name.lower()) # sudhakar