import default_config
import pymysql.cursors
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

def getProductByCategoryFromDatabase(category):
	global connection

	with connection.cursor() as cursor:
		cursor.execute("SELECT * FROM Products WHERE category=%s", (category, ))
		try:
			return Product((dict)(cursor.fetchone())) # Why does this work? This shouldn't be a feature!

		except:
			raise NotInDatabase


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
		cursor.execute("UPDATE `Products` SET `name`=%s, `price`=%s, `description`=%s, `imageUrl`=%s, `category`=%s WHERE `id`=%s", (product.name, product.price, product.description, product.imageUrl, product.category, product.id));
		connection.commit()		


# Returns a list of ids from the database
def getAllProductId():
	global connection

	with connection.cursor() as cursor:		
		cursor.execute("SELECT id FROM Products");
		result = cursor.fetchall()

		return [instance.get("id") for instance in result]


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


print(getCategories())