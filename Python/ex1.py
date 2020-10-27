# Learn the alphabets
# Learn words
# Learn to form sentences
# Learn to form grammer 


# Alphabets - Basic data types

# 1 - Integer
# 2 - Integer
# 101010101010101 - Integer
# 10.5 - Float
# 0.1 - Float
# 9109090.0100 - Float
# -0.10 - Float
# "A" - Character
# "10" - Character
# '10' - Character
# "Robin" - String # collection of characters are string
# "I am going to play today from morning" - String
# True - Boolean
# False - Boolean
# true - undefined variable
# false - undefined variable



first_name = "Bastin" # first_name is variable, Bastin, String
# print('first_name', type(first_name))
last_name = "Robin" # last_name is varible, Robin, String
# print('last_name', type(last_name))
age = 31 # age is variable, 32, Integer
# print('age', type(age))
is_completed = True # is_completed, True, Boolean
# print('is_completed', type(is_completed))
height = 80.1 # height, 80.1, float
# print('height', type(height))
grade = "A" # grade, A, String
# print('grade', type(grade))

# Example1 
subjects = ['English', 'Math', 'Science', 'Social', 'Computer']

items = [1, 10, 0.5, True, first_name, last_name, age]
# items, list, 7 items,
# print("Print all", items)
# print("First", items[0])
# print("Type of First", type(items[0]))

# print("Second", items[1])
# print("Type of Second", type(items[1]))

# print("Third", items[2])
# print("Type of Third", type(items[2]))
items[3] = False
# print(items)

# Swapping Operations
temp = items[4]
items[4] = items[5]
items[5] = temp
# print(items)

# Adding new item into the list `items`
items.append("10")
# print(items)

items.append("Robin")
# print(items)

del items[0]
# print(items)

del items[4]
# print(items)

colors = ("red", "yellow", "green", "blue")
# tuple 

# print(colors[0])
# print(colors[1])
# print(colors[2])
# print(colors[3])

# List []
# Tuple ()
# Dictionary {} 
students = {
	"first_name": first_name,
	"last_name" : last_name,
	"dept": "CSE",
	"subjects": subjects,
	"colors": colors,
}

# print(students["first_name"])
# print(students["last_name"])
# print(students['dept'])
# print(students['colors'][0])
# print(students['colors'][1])
# print(students['subjects'][2])

# <Request>
# https://facebook.com/bastinrobin

# username = "bastinrobin"

# - Connect to database
# - Find the record which is matching the `username` column == 'Bastinrobin'
# - `SELECT * FROM users where username=username;
# experience = 'experience'

# students['education'][0]['title']
# students['education'][1]['title']
# students['experience'][0]['org']['name']


# <Response> JSON
response = {
	"id": '10230910390020',
	"fname": 'Bastin',
	"lname": 'Robin',
	"is_online": True,
	"is_blocked": False,
	"latitude": 19209.1920,
	"longitude": 139.19300,
	"education": [
		{
			"id": 1001,
			"title": 'Bachelor in Computer',
			"created": 1101012010,
			"updated": 1012900001,
			"years": 3, 
			"institution": {
				"id": 199179,
				"name" : "XYZ institution",
				"address": 'Lorem ipsum',
				"departments": [

					{
						"id": 10,
						"name": 'Science',
						"rank": 10
					},
					{
						"id": 190,
						"name": "CSE",
						"rank": 8
					},
					{
						"id": 18,
						"name": 'Math',
						"rank": 6
					}

				]
			}
		},
		{
			"id": 1019,
			"title": 'Master in Computer',
			"created": 191018919,
			"updated": 1921928991,
			"years": 2
		}

	],
	"experiences": [
		{
			"id" : 191671,
			"title": 'Software engineer',
			"years": 5,
			"created": 19917930,
			"updated": 179902902,
			"org": {
				"name": 'Microsoft',
				"address": 'Microsoft Campus, Domlur'
			}
		},
		{
			"id" : 19167113,
			"title": 'Senior Software engineer',
			"years": 2,
			"created": 19917930,
			"updated": 179902902,
			"org": {
				"name": 'Microsoft',
				"address": 'Microsoft Campus, Domlur'
			}
		}	
	]
}

'''
Write code for getting the following things from the given `response`
dictionary
	
	- Print the firstname # String
	- Find the total educations years #Int 
	- Calcuate the total experiences, # Int
	- Print organizations worked - ['MS', 'Facebook']
'''
	



