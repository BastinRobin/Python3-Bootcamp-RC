import os
from textblob import TextBlob


def sentiment(text):
	score = TextBlob(text).polarity
	if score > 0:
		return (score,  'POSTIVE')
	elif score == 0:
		return (score, 'NEUTRAL')
	elif score < 0:
		return (score, 'NEGATIVE')




f = open('../review.csv', 'r')
for index, line in enumerate(f.readlines()):
	items = line.strip().split(',')
	if index > 0:
		score = sentiment(items[4])
		items.append(score[0])
		items.append(score[1])
		print(items)

	
# customers = Customers('reviews.csv')
# customers.get_customer(phone='iphone7')
# customers.get_customer(age=45)
# customers.get_customer(review='positive')