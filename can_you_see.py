from flask import Flask, render_template, request
from flask.ext.pymongo import PyMongo
import random

app = Flask(__name__)
mongo = PyMongo(app)


@app.route('/')
def home():
	return render_template('home.html')

@app.route('/view')
def view():
	category = "website"
	image = 'youtube.jpg'
	candidates = [
		'YouTube',
		'Vimeo',
		'Amazon',
		'eBay',
		'Google Search',
		'Facebook',
		'LinkedIn',
		'Stack Overflow',
		'Yahoo'
	]
	random.shuffle(candidates)
	return render_template('view.html', category=category, image=image, candidates=candidates)

@app.route('/guess', methods=['POST'])
def guess():
	return request.form['guess']


if __name__ == '__main__':
	app.debug = True
	app.run()
