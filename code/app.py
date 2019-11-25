import sys, os
from flask import Flask, request, redirect, render_template, abort, session, flash

import default_config
from database_handler import *
import user_handler

if not default_config.USEDUMMYDATABASE:
	import SQL_handler
else:
	import dummy_database as SQL_handler

def create_app():
	app = Flask(__name__, instance_relative_config=True)
	app.secret_key = os.urandom(24)


	@app.route('/')
	def home():

		products = []
		productIds = SQL_handler.getAllProductId()
		for productId in productIds:
			products.append(SQL_handler.getProductFromDatabase(productId))

		return render_template('home.html', user=user_handler.get_user(), args={'categories': SQL_handler.getCategories()})


	@app.route('/login', methods = ['GET', 'POST'])
	def login():

		if request.method == 'POST':
			if user_handler.login_parse(request.form['username'], request.form['password']):
				flash('Welcome %s' % user_handler.get_user().alias)
				return redirect('/')

			else:
				flash('Invalid username or password')

		return render_template('login.html', user=user_handler.get_user(), args={})


	@app.route('/logout')
	def logout():
		user_handler.logout_parse()
		flash("You've been logged out")
		return redirect('/')


	@app.route('/product/<id>')
	def product(id):
		try:
			product = SQL_handler.getProductFromDatabase(id)
			return render_template('product.html', user=user_handler.get_user(), args={'product': product})

		except database_handler.NotInDatabase:
			abort(404)


	@app.route('/category/<id>')
	def category(id):

		return render_template('categories.html', user=user_handler.get_user(), args={'products': SQL_handler.getProductsByCategoryFromDatabase(id)})
		

	@app.route('/getsession')
	def getsession():
		if 'userId' in session:
			return session['userId']

		return None

	return app


if __name__ == "__main__":

    app = create_app()
    app.run(host='0.0.0.0', debug=default_config.DEBUG)
