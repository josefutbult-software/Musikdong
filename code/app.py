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


def create_app():
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_mapping(
		SECRET_KEY = 'dev',
		DATABASE = os.path.join(app.instance_path, 'flaskr.sqlite'),
	)


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

	return app


if __name__ == "__main__":

    app = create_app()
    app.run(host='0.0.0.0')
