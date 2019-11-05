import os
from flask import Flask, request, render_template

def main():
	app = create_app()

def create_app():
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_mapping(
		SECRET_KEY = 'dev',
		DATABASE = os.path.join(app.instance_path, 'flaskr.sqlite'),
	)


	@app.route('/')
	def home():
		return render_template('home.html', name='home')


	@app.route('/article')
	def article():
		return render_template('article.html', name='article')



	return app


if __name__ == '__main__':
	main()
