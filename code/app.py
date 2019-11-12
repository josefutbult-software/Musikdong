import os
from flask import Flask, request, render_template

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


	@app.route('/test')
	def test():
		return render_template('test.html', args={'name': 'Test', 'article': '12321'})



	return app


if __name__ == "__main__":

    app = create_app()
    app.run(host='0.0.0.0')
