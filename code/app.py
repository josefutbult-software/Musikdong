from flask_handler import create_app
from flask import Flask, request, render_template

(app, db, migrate) = create_app()

@app.route('/')
def home():
	return render_template('home.html', name='home')


@app.route('/article')
def article():
	return render_template('article.html', name='article')


@app.route('/test')
def test():
	return render_template('test.html', args={'name': 'Test', 'article': '12321'})
