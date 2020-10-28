"""
Functions of a calculator
	- Addition
	- Subtraction
	- Multiplication
	- Division
"""

def addition(x, y):
	return x + y

def subtraction(x, y):
	return x - y

def multiplication(x, y):
	return x * y

def division(x, y):
	return x / y



# Write a function which is able to print all the odd numbers from 1 to 100
def is_odd(n):
	if n%2 !=0:
		return True
	else:
		return False

for i in range(101):
	if not is_odd(i):
		print(i)
