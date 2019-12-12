import default_config
import pymysql.cursors
from datetime import date
from random import randint
from database_handler import *

# Initiates a connection to the mySql database on run
connection = pymysql.connect(host=default_config.SQLADRESS,
                             user=default_config.SQLUSER,
                             password=default_config.SQLPSWD,
                             db='musikdong',
                             unix_socket='/run/mysqld/mysqld.sock',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


# Returns a product item from the database as a dict
def getProductFromDatabase(id):
	global connection

	with connection.cursor() as cursor:
		cursor.execute("SELECT * FROM Products WHERE id=%s", (id, ))
		try:
			return Product((dict)(cursor.fetchone())) # Why does this work? This shouldn't be a feature!

		except:
			raise NotInDatabase

def getProductsByCategoryFromDatabase(category):
	global connection

	with connection.cursor() as cursor:
		cursor.execute("SELECT * FROM Products WHERE category=%s", (category, ))
		try:
			result = (cursor.fetchall()) # Why does this work? This shouldn't be a feature!
			return [Product(instance) for instance in result]

		except:
			raise NotInDatabase

def getAllProducts():
	global connection

	with connection.cursor() as cursor:
		cursor.execute("SELECT * FROM Products")
		result = cursor.fetchall()
		return [Product(instance) for instance in result]


# Appends a product and its tags in the database
def insertProductIntoDatabase(product: Product) -> None:
	global connection

	if not isinstance(product, Product):
		raise TypeError

	with connection.cursor() as cursor:	

		try:
			cursor.execute("INSERT INTO `Products` (`id`, `name`, `price`, `description`, `imageUrl`, `category`) VALUES (%s, %s, %s, %s, %s, %s)",
			(product.id, product.name, product.price, product.description, product.imageUrl, product.category))
			connection.commit()			
		except:
			raise DuplicationError


# Updates a product and its tags in the database
def updateProductIntoDatabase(product: Product) -> None:
	global connection

	if not isinstance(product, Product):
		raise TypeError

	with connection.cursor() as cursor:		
		cursor.execute("UPDATE `Products` SET `name`=%s, `price`=%s, `description`=%s, `imageUrl`=%s, `category`=%s WHERE `id`=%s", (product.name, int(float(product.price)), product.description, product.imageUrl, product.category, product.id));
		connection.commit()		


# Returns a list of ids from the database
def getAllProductId():
	global connection

	with connection.cursor() as cursor:		
		cursor.execute("SELECT id FROM Products");
		result = cursor.fetchall()

		return [instance.get("id") for instance in result]


def delete_product(id):
	global connection

	with connection.cursor() as cursor:		
		cursor.execute("DELETE FROM Products WHERE `id`=%s", (id, ));
		result = connection.commit()

def generate_productId():
	global connection

	id = str(randint(0, 999999))

	with connection.cursor() as cursor:
		
		while True:
			cursor.execute("SELECT EXISTS(SELECT * FROM Products WHERE id=%s)", (id))
			inDatabase = cursor.fetchone()

			if not inDatabase.get(list(inDatabase.keys())[0]):
				return id

			id = str(randint(0, 999999))


def getProductTagsFromDatabase(product):
	global connection

	if not isinstance(product, Product):
		raise TypeError

	with connection.cursor() as cursor:		
		cursor.execute("SELECT * FROM Tag WHERE `productId`=%s", (product.id, ))

		try:
			result = (list)(cursor.fetchall())
			return [Tag(tag) for tag in result]

		except:
			raise NotInDatabase


def getTagTypesFromDatabase():
	global connection

	with connection.cursor() as cursor:		
		cursor.execute("SELECT * FROM TagTypes")
		result = cursor.fetchall()
		return [instance.get("name") for instance in result]


def getCategories():
	global connection

	with connection.cursor() as cursor:
		cursor.execute("SELECT * FROM Category")
		result = cursor.fetchall()
		return [instance.get("name") for instance in result]


def deleteCategory(name):
	global connection

	with connection.cursor() as cursor:
		cursor.execute("DELETE FROM Category WHERE name=%s", (name, ))
		connection.commit()


def addCategory(name):
	global connection

	with connection.cursor() as cursor:
		cursor.execute("INSERT INTO Category (name) VALUES (%s)", (name, ))
		connection.commit()

def updateCategory(oldname, newname):
	global connection

	with connection.cursor() as cursor:
		cursor.execute("UPDATE Category SET `name`=%s WHERE `name`=%s", (newname, oldname))
		connection.commit()


def getUserById(id):
	global connection

	with connection.cursor() as cursor:
		cursor.execute("SELECT * FROM User WHERE id=%s", (id, ))

		try:
			return User(cursor.fetchone())
		except:
			return None


def getUserByUsername(username):
	global connection

	with connection.cursor() as cursor:
		cursor.execute("SELECT * FROM User WHERE username=%s", (username, ))

		try:
			return User(cursor.fetchone())
		except:
			return None


def getAllUsers():
	global connection

	with connection.cursor() as cursor:
		cursor.execute("SELECT * FROM User")
		result = cursor.fetchall()
		return [User(instance) for instance in result]



def insert_user(user: User) -> None:
	global connection

	if not getUserByUsername(user.username) is None:
		return False

	with connection.cursor() as cursor:
		cursor.execute("INSERT INTO `User` (`id`, `username`, `password`, `alias`, `clearance`) VALUES (null, %s, %s, %s, %s)", (user.username, user.password, user.alias, user.clearance))
		connection.commit()

	return True

def update_user(user: User) -> None:
	global connection

	if getUserByUsername(user.username) is None:
		return False

	with connection.cursor() as cursor:
		cursor.execute("UPDATE `User` SET `username`=%s, `password`=%s, `alias`=%s, `clearance`=%s WHERE `id`=%s", (user.username, user.password, user.alias, user.clearance, user.id))
		connection.commit()

def delete_user(user: User) -> None:
	global connection

	with connection.cursor() as cursor:
		cursor.execute("DELETE FROM `User` WHERE `id`=%s", (user.id))
		connection.commit()



def get_cart(user: User):
	global connection

	# TODO: Make a better SQL quary using subquerys instead of looping
	with connection.cursor() as cursor:
		cursor.execute("SELECT * FROM Cart WHERE `userId`=%s", (user.id, ))
		cart = cursor.fetchall()

		products = []
		for instance in cart:
			cursor.execute("SELECT * FROM Products WHERE id=%s", (instance.get("productId"), ))
			product = Product(cursor.fetchone())
			product.amount = instance.get("amount")
			products.append(product)
		
		return products


def add_to_cart(user: User, product: Product) -> None:
	global connection

	with connection.cursor() as cursor:
		cursor.execute("SELECT EXISTS(SELECT * FROM Cart WHERE userId=%s AND productId=%s)", (user.id, product.id))
		
		inDatabase = cursor.fetchone()
		inDatabase = inDatabase.get(list(inDatabase.keys())[0])

		if inDatabase == 0:
			cursor.execute("INSERT INTO Cart (userId, productId, amount) VALUES (%s, %s, %s)", (user.id, product.id, 1))
		else:
			cursor.execute("UPDATE Cart SET `amount`=%s WHERE `userId`=%s AND productId=%s", (inDatabase + 1, user.id, product.id))
		
		connection.commit()

		
def updatecart_amount(user: User, product: Product, offcet: int) -> None:
	global connection

	with connection.cursor() as cursor:
		cursor.execute("SELECT amount FROM Cart WHERE userId=%s AND productId=%s", (user.id, product.id))
		
		if cursor.fetchone().get("amount") + offcet > 0:
			cursor.execute("SELECT `amount` FROM Cart WHERE `userId`=%s AND `productId`=%s", (user.id, product.id))
			cursor.execute("UPDATE Cart SET `amount`=%s WHERE userId=%s AND productId=%s", (cursor.fetchone()["amount"] + offcet, user.id, product.id))
			
		else:
			cursor.execute("DELETE FROM Cart  WHERE userId=%s AND productId=%s", (user.id, product.id))

		connection.commit()


def clear_cart(user: User) -> Product:
	global connection

	with connection.cursor() as cursor:
		cursor.execute("DELETE FROM Cart WHERE `userId`=%s", (user.id))
		connection.commit()
		

def place_order(user: User) -> Product:
	global connection

	with connection.cursor() as cursor:

		cursor.execute("INSERT INTO Orders (id, userId, orderdate, payed, processed) VALUES (null, %s, %s, %s, %s)", (user.id, date.today().isoformat(), False, False))
		connection.commit()

		cursor.execute("SELECT id FROM Orders")
		orders = cursor.fetchall()
		orderid = max([order.get('id') for order in orders])
		
		cursor.execute("SELECT * FROM Cart WHERE `userId`=%s", (user.id))
		cart = cursor.fetchall()

		for instance in cart:
			cursor.execute("INSERT INTO Orderitems (orderId, productId, amount, price) VALUES (%s, %s, %s, %s)", (orderid, instance.get("productId"), instance.get("amount"), getProductFromDatabase(instance.get("productId")).price))			
			connection.commit()

		cursor.execute("DELETE FROM Cart WHERE userId=%s", (user.id, ))
		connection.commit()


def get_orders():
	global connection

	with connection.cursor() as cursor:

		cursor.execute("SELECT * FROM Orders")
		result = cursor.fetchall()
		orders = [Order(instance) for instance in result]
		for order in orders:
			order.username = getUserById(order.userId).username

		return orders


def get_order(id):
	global connection

	with connection.cursor() as cursor:

		cursor.execute("SELECT * FROM Orders WHERE id=%s", (id, ))
		return Order(cursor.fetchone())

def delete_order(id):
	global connection

	with connection.cursor() as cursor:

		cursor.execute("DELETE FROM Orders WHERE id=%s", (id, ))
		connection.commit()


def get_orderitems_by_id(id):
	global connection

	with connection.cursor() as cursor:

		cursor.execute("SELECT * FROM Orderitems WHERE orderId=%s", (id, ))
		result = cursor.fetchall()
		return [Orderitem(instance, getProductFromDatabase(instance.get("productId"))) for instance in result]


def updateorder(order: Order) -> None:
	global connection

	with connection.cursor() as cursor:
		cursor.execute("UPDATE Orders SET userId=%s, orderdate=%s, payed=%s, processed=%s WHERE id=%s", (order.userId, order.orderdate, order.payed, order.processed, order.id))
		connection.commit()



def updateorder_amount(order: Order, product: Product, offcet: int) -> None:
	global connection

	with connection.cursor() as cursor:
		cursor.execute("SELECT amount FROM Orderitems WHERE orderId=%s AND productId=%s", (order.id, product.id))
		
		if cursor.fetchone().get("amount") + offcet > 0:
			cursor.execute("SELECT `amount` FROM Orderitems WHERE `orderId`=%s AND `productId`=%s", (order.id, product.id))
			cursor.execute("UPDATE Orderitems SET `amount`=%s WHERE orderId=%s AND productId=%s", (cursor.fetchone()["amount"] + offcet, order.id, product.id))
			
		else:
			cursor.execute("DELETE FROM Orderitems WHERE orderId=%s AND productId=%s", (order.id, product.id))

		connection.commit()

# Fick Hjälp av Kitty
def setReview(review: Review) -> None:	
	global connection

	with connection.cursor() as cursor:
		cursor.execute("INSERT INTO Review (userId, productId, rating, review) VALUES (%s, %s, %s, %s) ON DUPLICATE KEY UPDATE rating=%s, review=%s", (review.userId, review.productId, review.rating, review.review, review.rating, review.review))
		connection.commit()


def getReveiw(user: User, product: Product) -> None:
	global connection

	with connection.cursor() as cursor:
		cursor.execute("SELECT * FROM Review WHERE userId=%s AND productId=%s", (user.id, product.id))
		return Review(cursor.fetchone())


def getReviewByProduct(product: Product) -> None:
	global connection

	with connection.cursor() as cursor:
		cursor.execute("SELECT * FROM Review WHERE productId=%s", (product.id, ))
		result = cursor.fetchall()
		return [Review(instance) for instance in result]

