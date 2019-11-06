from flask_handler import create_app
from flask import Flask, request, render_template
import sys

# Allowing a custom config file to overwrite the default configuration
try:
	config = __import__(sys.argv[1].replace('.py', ''))
except (IndexError, ModuleNotFoundError) as e:
	print(e)
	print("Using default config")

	import default_config as config


# Creating a flask application
app = create_app()


# Routes for the flask aplication
@app.route('/')
def home():
	return render_template('home.html', name='home')


@app.route('/article')
def article():
	return render_template('article.html', name='article')


@app.route('/test')
def test():
	return render_template('test.html', args={'name': 'Test', 'article': '12321'})
