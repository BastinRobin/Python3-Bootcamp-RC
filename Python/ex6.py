"""
OBJECT ORIENTED PROGRAMMING
(OR) OOPS CONCEPT
"""

class Calculator:

	# def __init__(self, x, y):
	# 	self.x = x
	# 	self.y = y

	def addition(self, x, y):
		return x + y

	def subtraction(self, x, y):
		return x - y

	def multiplication(self, x, y):
		return x * y

	def division(self, x, y):
		return x / y



class XCalculator:

	# Constructor
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def addition(self):
		return self.x + self.y

	def subtraction(self):
		return self.x - self.y

	def multiplication(self):
		return self.x * self.y

	def division(self):
		return self.x / self.y



# calc = Calculator()

# a = calc.addition(10, 20)
# print(a)

# b = calc.subtraction(10, 20)
# print(b)

# c = calc.multiplication(10, 20)
# print(c)

# d = calc.division(10, 20)
# print(d)


# xcalc = XCalculator(10, 30)
# print(xcalc.addition())
# print(xcalc.subtraction())
# print(xcalc.multiplication())
# print(xcalc.division())















