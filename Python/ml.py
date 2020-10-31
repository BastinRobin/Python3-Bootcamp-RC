import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score



df = pd.read_csv('heart.csv')
df['ca'].fillna(df['ca'].mean(), inplace=True)
df['thal'].fillna(df['thal'].mean(), inplace=True)


y = df['target'].values.ravel()
X = df.iloc[:, df.columns != 'target']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=45)

clf = LogisticRegression(solver = 'newton-cg', max_iter=1000, n_jobs=2)
# Train the model mean teach 70% examples
clf.fit(X_train, y_train)
prediction = clf.predict(X_test)

print("Accuracy of our model prediction heart diseases", accuracy_score(y_test, prediction)*100)

