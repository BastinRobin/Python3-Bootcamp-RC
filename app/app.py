from flask import Flask, request, url_for, redirect,flash, render_template
from textblob import TextBlob
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/analyse')
def analyse():
	text = request.args.get('content')
	score = TextBlob(text).polarity
	if score > 0:
		sentiment = 'POSITIVE' 
	elif score == 0:
		sentiment = 'NEUTRAL'
	elif score < 0:
		sentiment = 'NEGATIVE'

	flash(sentiment)
	return redirect(url_for('index'))




if __name__ == '__main__':
	app.run(debug=True)

