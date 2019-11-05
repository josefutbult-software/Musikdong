import os
from flask import Flask

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
		return 'Hello there. General Kenobi'


	return app


if __name__ == '__main__':
	main()
