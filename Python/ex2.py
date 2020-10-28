"""
Loops
	- For
	- While
	
	Syntax:

		for index in range(10):
			print(index)

"""

# for item in ["sam", "james", "doe", "kevin"]:
# 	print("My Name is "+ item)
	
# for item in range(10):
# 	print(item)

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
		},
		{
			"id": 1019,
			"title": 'Master in Computer',
			"created": 191018919,
			"updated": 1921928991,
			"years": 2
		},
		{
			"id": 1019,
			"title": 'Master in Computer',
			"created": 191018919,
			"updated": 1921928991,
			"years": 2
		},
		{
			"id": 1019,
			"title": 'Master in Computer',
			"created": 191018919,
			"updated": 1921928991,
			"years": 2
		},
		{
			"id": 1019,
			"title": 'Master in Computer',
			"created": 191018919,
			"updated": 1921928991,
			"years": 2
		},{
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
		},
		{
			"id" : 19167113,
			"title": 'Lead Software engineer',
			"years": 1,
			"created": 19917930,
			"updated": 179902902,
			"org": {
				"name": 'Google',
				"address": 'Google Campus'
			}
		},
		{
			"id" : 19167113,
			"title": 'Lead Software engineer',
			"years": 4,
			"created": 19917930,
			"updated": 179902902,
			"org": {
				"name": 'Google',
				"address": 'Google Campus'
			}
		},
		{
			"id" : 19167113,
			"title": 'Lead Software engineer',
			"years": 4,
			"created": 19917930,
			"updated": 179902902,
			"org": {
				"name": 'Google',
				"address": 'Google Campus'
			}
		},
		{
			"id" : 19167113,
			"title": 'Lead Software engineer',
			"years": 4,
			"created": 19917930,
			"updated": 179902902,
			"org": {
				"name": 'Google',
				"address": 'Google Campus'
			}
		},
		{
			"id" : 19167113,
			"title": 'Lead Software engineer',
			"years": 4,
			"created": 19917930,
			"updated": 179902902,
			"org": {
				"name": 'Google',
				"address": 'Google Campus'
			}
		},
		{
			"id" : 19167113,
			"title": 'Lead Software engineer',
			"years": 4,
			"created": 19917930,
			"updated": 179902902,
			"org": {
				"name": 'Google',
				"address": 'Google Campus'
			}
		},	
		{
			"id" : 19167113,
			"title": 'Lead Software engineer',
			"years": 4,
			"created": 19917930,
			"updated": 179902902,
			"org": {
				"name": 'Google',
				"address": 'Google Campus'
			}
		}
	]
}


temp=0
for item in response['education']:
	temp = temp + item['years']

print(temp)


temp=0
for item in response['experiences']:
	temp = temp + item['years']
print(temp)


