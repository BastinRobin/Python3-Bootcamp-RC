
''' 
# Inbuilt functions
	print()
	len()
	range()
	xrange()
	int()
	str()
	float()
	bool()
'''
# print()

a = [1,2,3,4,5,6,7]
# temp = 0
# for i in a:
# 	temp = i + temp
# print(temp)

"""
Function with return type
"""
def addition(x):
	temp = 0
	for i in x:
		temp = i + temp
	return temp

"""
Function without return type
"""
def addition1(x):
	temp = 0
	for i in x:
		temp = i + temp
	print(temp)



first = addition(a)
second = addition1(a)

print(first) #28
print(second) # None




