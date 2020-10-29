
employees = (
	{"name": 'James', "age": 40, "total_year": 10, "salary": 50000, "gender": 'male'},
	{"name": 'Suresh', "age": 30, "total_year": 5, "salary": 55000, "gender": 'male'},
	{"name": 'Kishore', "age": 50, "total_year": 2, "salary": 56000, "gender": 'male'},
	{"name": 'Jane', "age": 23, "total_year": 6, "salary": 52000, "gender": 'female'},
	{"name": 'Kevin', "age": 60, "total_year": 10, "salary": 40000, "gender": 'male'},
	{"name": 'Robin', "age": 50, "total_year": 12, "salary": 30000, "gender": 'male'},
	{"name": 'Robert', "age": 41, "total_year": 3, "salary":20000, "gender": 'male'},
	{"name": 'Rose', "age": 23, "total_year": 3, "salary": 60000, "gender": 'female'},
	{"name": 'Jack', "age": 44, "total_year": 5, "salary": 58000, "gender": 'male'},
	{"name": 'Morgan', "age": 55, "total_year": 7, "salary": 51000, "gender": 'female'},
	{"name": 'Ramesh', "age": 40, "total_year": 5, "salary": 10000, "gender": 'male'},
	{"name": 'Jerry', "age": 41, "total_year": 10, "salary": 30000, "gender": 'male'}
)


"""
emp = Employee(item)

Assignment
 - Find all employees who are senior (age > 45) using loops and functions
 - Find all employees who are females and age greater than 40
 - Build a method which should take each employees as input and only print the
 one who is eligible for promotion `criteria total_year greater than 5 and age is above
 40`
"""




class Organization:

	def __init__(self, employees):
		self.employees = employees


	def is_senior(self, age):
		"""
		Determines whether the specified age is senior.
		
		:param      age:  The age
		:type       age:  { type_description }
		
		:returns:   True if the specified age is senior, False otherwise.
		:rtype:     boolean
		"""
		if age > 45:
			return True
		else:
			return False


	def is_promotable(self, employee):
		"""
		Determines whether the specified employee is promotable.
		
		:param      employee:  The employee
		:type       employee:  { type_description }
		
		:returns:   True if the specified employee is promotable, False otherwise.
		:rtype:     boolean
		"""
		if employee['age'] > 40 and employee['total_year']  > 5:
			return True
		else:
			return False



	def is_senior_female(self, age, gender):
		"""
		Determines if senior female.
		
		:param      age:     The age
		:type       age:     { type_description }
		:param      gender:  The gender
		:type       gender:  { type_description }
		
		:returns:   True if senior female, False otherwise.
		:rtype:     boolean
		"""
		if age > 40 and gender == 'female':
			return True
		else:
			return False


	def get_all_seniors(self):
		"""
		Gets all seniors.
		
		:returns:   All seniors.
		:rtype:     { return_type_description }
		"""
		temp = []
		for employee in self.employees:
			if self.is_senior(employee['age']):
				temp.append(employee['name'])
		return temp


	def get_senior_females(self):
		"""
		Gets the senior females.
		
		:returns:   The senior females.
		:rtype:     { return_type_description }
		"""
		temp = []
		for employee in self.employees:
			if self.is_senior_female(employee['age'], employee['gender']):
				temp.append(employee['name'])
		return temp


	def get_eligible_for_promotion(self):
		"""
		Gets the eligible for promotion.
		
		:returns:   The eligible for promotion.
		:rtype:     { return_type_description }
		"""
		temp = []
		for employee in self.employees:
			if self.is_promotable(employee):
				temp.append(employee['name'])

		return temp









org = Organization(employees)
print('Seniors', org.get_all_seniors())
print('Female Seniors', org.get_senior_females())
print('List of Promotions', §org.get_eligible_for_promotion())




