from joblib import load


clf = load('model.pkl')

predict = clf.predict([
	[50,0,3,120,219,0,0,158,0,1.6,2,0,3],
	[60,1,4,130,206,0,2,132,1,2.4,2,2,7]])

print("Your prediction is",predict)