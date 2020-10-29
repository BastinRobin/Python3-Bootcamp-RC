# -*- coding: utf-8 -*-

import operator

class NewSummarize:

	def __init__(self, text):
		self.stopword = ['i', 'me', 'my', 'myself', 'we', 'The',
		 'This', 'It', 'Also', 'also', 'it', 'the', 'this', 'our',
		 'ours', 'ourselves', 'you', "you're", "you've", "you'll",
		 "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he',
		 'him', 'his', 'himself', 'she', "she's", 'her', 'hers',
		 'herself', 'it', "it's", 'its', 'itself', 'they', 'them',
		 'their', 'theirs', 'themselves', 'what', 'which', 'who',
		 'whom', 'this', 'that', "that'll", 'these', 'those', 'am',
		 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have',
		 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a',
		 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 
		 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about',
		 'against', 'between', 'into', 'through', 'during', 'before', 
		 'after', 'above', 'below', 'to', 'from',\
		 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again',
		 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why',
		 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other',
		 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than',
		 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should',
		 "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't",
		 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 
		 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', 
		 "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't",
		 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won',
		 "won't", 'wouldn', "wouldn't"]
		self.text = text.split(' ')


	def remove_stopword(self):
		return [item for item in self.text if item not in self.stopword]



	def count_frequency(self):
		text = self.remove_stopword()
		counter = {}
		for item in text:
			if item in counter:
				counter[item] = counter[item] + 1
			else:
				counter[item] = 1
		return counter


	def sort_by_frequency(self):
		counter = self.count_frequency()
		return [i[0] for i in sorted(counter.items(),\
		 key=operator.itemgetter(1), reverse=True)[0: 10]]


	def summarize(self):
		text = self.sort_by_frequency()
		return ' '.join(text)








