# -*- coding: utf-8 -*-

import operator
import collections


text = '''A leader of the Jammu Kashmir Peoples Democratic Party has made a shocking statement, a day after the Central government amended several laws and allowed people from across the country to buy land in the union territory of Jammu and Kashmir.

Surinder Chaudhary, PDP leader and close associate of party chief Mehbooba Mufti, caused outrage with his remarks when he suggested that rapes will increase in Jammu and Kashmir if Indians from rest of the country come to settle here after changes in land laws.

“Jammu has a rich Dogra culture and legacy; we have given sacrifices for the country. We are not saying they (outsiders) will start coming crimes like rapes as soon as they come to settle here. What we are saying is also being said by Assam and Maharashtra etc, that people should not come from outside as they will snatch jobs,” Chaudhary told Times Now.

“Today, the Jammu region is very peaceful. Here, women come from different villages to study in Jammu. You can see as to what happened in Faridabad, where a girl was shot dead, and also what happened in Hathras,” he added.

“Rape cases are increasing. All this is being shown on national TV,” the PDP leader went on to add.'''

stopwords = ['i', 'me', 'my', 'myself', 'we', 'The', 'This', 'It', 'Also', 'also', 'it', 'the', 'this', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
tokens = text.split(' ')


# print(len(tokens))

temp = []
for item in tokens:
	if item not in stopwords:
		temp.append(item)



counter = {}

for item in temp:
	if item in counter:
		counter[item] = counter[item] + 1
	else:
		counter[item] = 1

temp = []
for i in sorted(counter.items(), key=operator.itemgetter(1), reverse=True)[0: 10]:
	temp.append(i[0])

print(' '.join(temp))
