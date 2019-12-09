import sys, os
from flask import Flask, request, redirect, render_template, abort, session, flash, url_for
from datetime import datetime
from random import randint, seed
import default_config
from database_handler import *
import user_handler

if not default_config.USEDUMMYDATABASE:
	import SQL_handler
else:
	import dummy_database as SQL_handler

def create_app():
	seed(datetime.now())
	app = Flask(__name__, instance_relative_config=True)
	app.secret_key = os.urandom(24)


	@app.route('/')
	def home():

		products = []
		productIds = SQL_handler.getAllProductId()
		for productId in productIds:
			products.append(SQL_handler.getProductFromDatabase(productId))

		return render_template('home.html', args={'categories': SQL_handler.getCategories(), 'user': user_handler.get_user()})


	@app.route('/product/<id>', methods = ['GET', 'POST'])
	def product(id):
		try:
			product = SQL_handler.getProductFromDatabase(id)
			
			if request.method == 'POST':
				SQL_handler.add_to_cart(user_handler.get_user(), product)

			return render_template('product.html', args={'product': product, 'user': user_handler.get_user()})

		except NotInDatabase:
			abort(404)


	@app.route('/category/<id>')
	def category(id):

		return render_template('categories.html', args={'products': SQL_handler.getProductsByCategoryFromDatabase(id), 'user': user_handler.get_user()})
		

	@app.route('/login', methods = ['GET', 'POST'])
	def login():

		if request.method == 'POST':
			if user_handler.login_parse(request.form['username'], request.form['password']):
				flash('Welcome %s' % user_handler.get_user().alias)
				return redirect('/')

			else:
				flash('Invalid username or password')

		return render_template('login.html', args={'user': user_handler.get_user()})


	@app.route('/logout')
	def logout():
		if user_handler.get_user() is None:	
			abort(404)

		user_handler.logout_parse()
		flash("You've been logged out")
		return redirect('/')


	@app.route('/signup', methods = ['GET', 'POST'])
	def signup():

		if request.method == 'POST':
			if user_handler.signup_parse(request.form['username'], request.form['password']):
				user_handler.login_parse(request.form['username'], request.form['password'])
				flash('Welcome %s' % user_handler.get_user().alias)
				return redirect('/')

			else:
				flash('Invalid username or password')

		return render_template('login.html', args={'user': user_handler.get_user()})

	@app.route('/cart', methods = ['GET', 'POST'])
	def cart():
		currentUser = user_handler.get_user()
		if currentUser is None:	
			abort(404)

		if request.method == 'POST':
			if request.form["submit"] == "Delete":
				SQL_handler.clear_cart(currentUser)
			elif request.form["submit"] == "+":
				SQL_handler.updatecart_amount(currentUser, SQL_handler.getProductFromDatabase(request.form["productId"]), 1)
			elif request.form["submit"] == "-":
				SQL_handler.updatecart_amount(currentUser, SQL_handler.getProductFromDatabase(request.form["productId"]), -1)
			else:
				SQL_handler.place_order(currentUser)
				flash('Your order is placed.')


		return render_template('cart.html', args={'user': currentUser, 'products': SQL_handler.get_cart(currentUser)})


	@app.route('/manager', methods = ['GET',])
	def manager():
		if user_handler.get_user() is None or user_handler.get_user().clearance > 1:	
			abort(404)

		return render_template('manager.html', args={'users': SQL_handler.getAllUsers(), 'user': user_handler.get_user(), 'products': SQL_handler.getAllProducts(), 'orders': SQL_handler.get_orders(), 'categories': SQL_handler.getCategories()})

	@app.route('/manageUser/<id>', methods = ['GET', 'POST'])
	def manageUser(id):
		if user_handler.get_user() is None or user_handler.get_user().clearance > 1:	
			abort(404)

		userToManage = SQL_handler.getUserById(id)

		if request.method == 'POST':

			if request.form['formtype'] == 'userconfig':
				userToManage.alias = request.form['alias']

				if user_handler.get_user().clearance == 0:
					userToManage.clearance = request.form['clearance']
		
				if request.form['password'] != "":
					user_handler.update_password(userToManage, request.form['password'])
				
				SQL_handler.update_user(userToManage)
			else:
				if request.form["submit"] == "+":
					SQL_handler.updatecart_amount(userToManage, SQL_handler.getProductFromDatabase(request.form["productId"]), 1)
				elif request.form["submit"] == "-":
					SQL_handler.updatecart_amount(userToManage, SQL_handler.getProductFromDatabase(request.form["productId"]), -1)


		return render_template('manageUser.html', args={'users': SQL_handler.getAllUsers(), 'user': user_handler.get_user(), 'userToManage': userToManage, 'userToManageCart': SQL_handler.get_cart(userToManage)})


	@app.route('/addProduct', methods = ['GET', 'POST'])
	def addProduct():

		productBuffer = {
			'name': '',
			'price': '',
			'description': '',
			'category': '',
			'imageUrl': 'None',
			'id': SQL_handler.generate_productId()
		}

		if request.method == 'POST':
			productBuffer['name'] = request.form['name']
			productBuffer['price'] = request.form['price']
			productBuffer['description'] = request.form['description']
			productBuffer['category'] = request.form['category']

			if not '' in (productBuffer['name'], productBuffer['price'], productBuffer['description'], productBuffer['category']):
				try:
					SQL_handler.insertProductIntoDatabase(Product(productBuffer))
					flash("Added product")
					return redirect(url_for('.manager'))
				except:
					flash("Could not add product")
			else:
				flash("Empty fields")

		return render_template('addProduct.html', args={'user': user_handler.get_user(), 'categories': SQL_handler.getCategories(), 'productBuffer': productBuffer})


	@app.route('/manageProduct/<id>', methods = ['GET', 'POST'])
	def manageProduct(id):
		productToManage = SQL_handler.getProductFromDatabase(id)

		if user_handler.get_user() is None or user_handler.get_user().clearance > 1 or SQL_handler.getProductFromDatabase(id) is None:	
			abort(404)

		if request.method == 'POST':
			try:
				if request.form['button'] == 'delete':
					SQL_handler.delete_product(id)
					return redirect(url_for('.manager'))

				int(request.form['price'])

				productToManage.name = request.form['name']
				productToManage.price = request.form['price']
				productToManage.description = request.form['description']
				productToManage.category = request.form['category']

				SQL_handler.updateProductIntoDatabase(productToManage)
				
			except Exception as e:
				print(e)

		return render_template('manageProduct.html', args={'users': SQL_handler.getAllUsers(), 'categories': SQL_handler.getCategories(), 'user': user_handler.get_user(), 'productToManage': productToManage})


	@app.route('/manageOrder/<id>', methods = ['GET', 'POST'])
	def manageOrder(id):

		order = SQL_handler.get_order(id)

		if request.method == 'POST':
			
			if request.form["type"] == "orderitem":
				if request.form["submit"] == "+":
					SQL_handler.updateorder_amount(order, SQL_handler.getProductFromDatabase(request.form["productId"]), 1)
				elif request.form["submit"] == "-":
					SQL_handler.updateorder_amount(order, SQL_handler.getProductFromDatabase(request.form["productId"]), -1)
			elif request.form["type"] == "delete":
				SQL_handler.delete_order(order.id)
				return redirect(url_for('manager'))
			elif request.form["type"] == "order":
				try:
					order.payed = request.form.get("payed") == 'on'
					order.processed = request.form.get("processed") == 'on'
					order.orderdate = datetime.strptime(request.form.get("orderdate"), "%Y-%m-%d")
				
					SQL_handler.updateorder(order)
				except:
					pass

		return render_template('manageOrder.html', args={'user': user_handler.get_user(), 'orderUser': SQL_handler.getUserById(order.userId), 'order': order, 'orderitems': SQL_handler.get_orderitems_by_id(id)})


	@app.route('/manageCategory/<name>', methods = ['GET', 'POST'])
	def manageCategory(name):

		if not name in SQL_handler.getCategories():
			abort(404)

		if request.method == 'POST':
			
			if request.form["submit"] == "Delete":
				SQL_handler.deleteCategory(name)
				return redirect('/manager')
			else:
				SQL_handler.updateCategory(oldname=name, newname=request.form["name"])
				return redirect(f'/manageCategory/{request.form["name"]}')

		return render_template('manageCategory.html', args={'user': user_handler.get_user(), 'category': name})


	@app.route('/addCategory', methods = ['GET', 'POST'])
	def addCategory():
		
		if request.method == 'POST':
			name = request.form["name"]
			try:
				SQL_handler.addCategory(request.form["name"])
				return redirect('/manager')
			except:
				flash("Cant add Category")
		else:
			name = ""

		return render_template('/addCategory.html', args={'user': user_handler.get_user(), 'category': name})

	return app

	

if __name__ == "__main__":

    app = create_app()
    app.run(host='0.0.0.0', debug=default_config.DEBUG)
