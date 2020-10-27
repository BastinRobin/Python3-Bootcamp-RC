# cup1 is the variable name [label]
# milk is the content of the cup1 variable so its a value of cup1
# size of the variable means the size of the container

a = "milk"
b = "water"
c = ''
# Swap content of a to b and content of b to a
c = a
print('*'*10)
print(a) # milk
print(b) # water
print(c) # milk
a = b
print('*'*10)

print(a) # water
print(b) # water
print(c) # milk
print('*'*10)
b = c
print(a) # water
print(b) # milk
print(c) # milk