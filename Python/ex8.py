import operator


class Parser:

	def __init__(self, filename):
		self.text = open(filename, 'r').readlines()


	def get_records(self, col_num=None, op=None, val=None):

		if op=='>':
			operation = operator.gt
		elif op=='<':
			operation = operator.lt
		elif op=='>=':
			operation = operator.ge
		elif op=='<=':
			operation = operator.le


		for index, item in enumerate(self.text):
			if index > 0:
				temp = item.strip().split(',')
				x = []
				if operation(int(temp[col_num]), int(val)):
					x.append(item)

		return x


demo = Parser('../review.csv')
demo.get_records(col_num=1, op='<', val=34)



import pandas as pd 
df = pd.read_csv('../review.csv')
print(df[(df['Age'] < 30) & (df['Gender'] == 'F') ] )




