

students = [
	{"fname": "Jack", "lname": "Doe", "age": 40, "salary": 20000},
	{"fname": "James", "lname": "Doe", "age": 32, "salary": 30000},
	{"fname": "Daniel", "lname": "Doe", "age": 43, "salary": 20000},
	{"fname": "John", "lname": "Doe", "age": 22, "salary": 50000},
	{"fname": "Suresh", "lname": "Doe", "age": 41, "salary": 60000},
	{"fname": "krishna", "lname": "Doe", "age": 44, "salary": 80000},
	{"fname": "Mike", "lname": "Doe", "age": 53, "salary": 250000}
]


for student in students:
	if student['age'] > 20 and student['age'] <=25:
		print(student['fname'], 'Junior')
	elif student['age'] > 25 and student['age'] <= 35:
		print(student['fname'], 'Middle')
	elif student['age'] > 35:
		print(student['fname'], 'Senior')

