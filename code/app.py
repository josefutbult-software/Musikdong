from flask_handler import create_app
from flask import Flask, request, render_template, abort
import sys, os
import default_config
import SQL_handler

def create_app():
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_mapping(
		SECRET_KEY = 'dev',
		DATABASE = os.path.join(app.instance_path, 'flaskr.sqlite'),
	)

	# Routes for the flask aplication
	@app.route('/')
	def home():
		products = []
		productIds = SQL_handler.getAllProductId()
		for productId in productIds:
			products.append(SQL_handler.getProductFromDatabase(productId))

		return render_template('home.html', args={'products': products})



	@app.route('/article/<id>')
	def article(id):
		try:
			product = SQL_handler.getProductFromDatabase(id)
			return render_template('article.html', args={'product': product})

		except SQL_handler.NotInDatabase:
			abort(404)


	@app.route('/test')
	def test():
		return render_template('test.html', args={'name': 'Test', 'article': '12321'})

	@app.route('/category/<id>')
	def category():
	

		return render_template('categories.html', args={'products': ["Guma drive", "Bassslapper"]})
		
	return app


if __name__ == "__main__":

    app = create_app()
    app.run(host='0.0.0.0')
