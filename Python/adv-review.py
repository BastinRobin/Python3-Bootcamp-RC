import pandas as pd
import numpy as np
from textblob import TextBlob

data = pd.read_csv('../review.csv')


def sentiment(text):
	score = TextBlob(text).polarity
	if score > 0:
		return 'POSTIVE'
	elif score == 0:
		return  'NEUTRAL'
	elif score < 0:
		return 'NEGATIVE'

def scoring(text):
	return TextBlob(text).polarity


data['sentiment'] = data['Review'].apply(sentiment)
data['polarity'] = data['Review'].apply(scoring)


data.to_csv('update_review.csv', index=False)
