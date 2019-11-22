# This is a dummy database, in case mySql isnt implemented localy

from database_handler import *

products = [
	Product({'id': '0', 'name': 'Guma Drive', 'price': 300, 'description': 'This is a dummy product', 'imageUrl': 'None', 'category': 'Overdrive'}),
	Product({'id': '1', 'name': 'Comp ma Swamp', 'price': 200, 'description': 'This is a dummy product', 'imageUrl': 'None', 'category': 'Compressor'}),
	Product({'id': '3', 'name': 'Josefs oskuld', 'price': -40, 'description': 'This is a dummy product', 'imageUrl': 'None', 'category': 'Sexual Favor'})
]

def getAllProductId():
	return ['0', '1', '2']

def getProductFromDatabase(id):
	return products[(int)(id)]

def getCategories():
	return ['Overdrive', 'Compressor', 'Sexual Favor']

def getProductByCategoryFromDatabase(id):
	return [product for product in products if product.category == id]